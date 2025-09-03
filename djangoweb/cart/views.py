from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views import View
from django.urls import reverse
from django.core.mail import send_mail
from django.core.cache import cache
from django.contrib import messages
from products.models import Products
from cart.models import BudgetRequest
from cart.forms import BudgetRequestModelForm
from utils.mixins import BreadcrumbsMixin
from website.views import get_client_ip
import os
import dotenv


dotenv.load_dotenv()

class CartView(BreadcrumbsMixin, TemplateView):
    template_name = "cart/cart.html"

    def get_breadcrumbs(self):
        return [
            {"name": "Home", "url": reverse("website:home")},
            {"name": "Produtos", "url": reverse("products:index")},
            {"name": "Carrinho", "url": None},
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get("cart", [])
        products = Products.objects.filter(id__in=cart)

        context["products"] = products
        context["form"] = BudgetRequestModelForm()

        # Stores form opening time
        self.request.session['form_started_at'] = timezone.now().isoformat()

        return context
    
    def post(self, request, *args, **kwargs):
        remove_id = request.POST.get("remove")
        form = BudgetRequestModelForm(request.POST)
        cart = request.session.get("cart", [])
        ip = get_client_ip(request)
        time_limit = 600  # 10 min

        # Sending time check (Bot protection)
        started_at = request.session.get('form_started_at')
        if started_at:
            elapsed = (timezone.now() - timezone.datetime.fromisoformat(started_at)).total_seconds()

            if elapsed < 5:
                form.add_error(
                    None,
                    '❌ Erro ao processar dados. Tente novamente.'
                )

        if remove_id:
            cart = request.session.get("cart", [])
            
            if int(remove_id) in cart:
                cart.remove(int(remove_id))
                request.session["cart"] = cart

            messages.info(
                request,
                'ℹ️ Produto foi removido.'
            )
            return redirect(reverse("cart:cart"))

        products = Products.objects.filter(id__in=cart)

        if not products.exists():
            messages.error(
                request,
                "❌ Seu Carrinho está vazio"
            )

        # Check cache.
        if cache.get(f"blocked_{ip}"):
            form.add_error(
                None,
                "❌ Aguarde alguns minutos antes de enviar novamente.",
            )

        if form.is_valid() and products.exists():

            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data.get("message", "")

            product_list = "\n".join([f" - {p.name}" for p in products])

            body = (
                f"Pedido de orçamento de {name}\n"
                f"Telefone: {phone}\nEmail: {email}\n\n"
                f"Produtos:\n{product_list}\n\nMensagem:\n{message}" 
            )

            # Save in database
            budget_request = BudgetRequest.objects.create(
                name=name,
                phone=phone,
                email=email,
                message=message,
            )
            budget_request.products.set(products)

            send_mail(
                subject="[Site Gazil] Novo Pedido de Orçamento",
                message=body,
                from_email=os.getenv('DEFAULT_FROM_EMAIL', ''),
                recipient_list=[os.getenv('EMAIL_RECIPIENT_LIST', '')],
                fail_silently=False,
            )

            messages.success(
                request,
                "✔️ Orçamento enviado com sucesso."
            )

            # Block IP for 10 minutes, to avoid SPAM
            cache.set(f"blocked_{ip}", True, timeout=time_limit)

            request.session["cart"] = []
            return render(
                request,
                self.template_name,
                {
                    "products": [],
                    "form": BudgetRequestModelForm(),
                    "breadcrumbs": self.get_breadcrumbs(),
                }
            )
        
        return render(
            request,
            self.template_name,
            {
                "products": products,
                "form": form,
                "breadcrumbs": self.get_breadcrumbs(),
            }
        )
    

class AddToCartView(View):

    def post(self, request, slug_product):
        product = get_object_or_404(Products, slug_product=slug_product)
        cart = request.session.get("cart", [])
        
        if product.id not in cart:
            cart.append(product.id)
            request.session["cart"] = cart
            messages.success(
                request,
                "✔️ Produto adicionado com sucesso!"
            )
        else:
            messages.info(
                request,
                f"ℹ️ Produto já está no carrinho."
            )

        return redirect(
            request.META.get('HTTP_REFERER', 'products:list_product')
        )
    