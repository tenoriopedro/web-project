from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import messages
from products.models import Products
from .models import BudgetRequest
from .forms import BudgetRequestModelForm
import os
import dotenv


dotenv.load_dotenv()

class CartView(View):

    def get(self, request):
        cart = request.session.get("cart", [])
        products = Products.objects.filter(id__in=cart)
        form = BudgetRequestModelForm()

        return render(
            request,
            "cart/cart.html",
            {
                "products": products,
                "form": form,
            }
        )
    
    def post(self, request):
        remove_id = request.POST.get("remove")

        if remove_id:
            cart = request.session.get("cart", [])
            
            if int(remove_id) in cart:
                cart.remove(int(remove_id))
                request.session["cart"] = cart

            return redirect(reverse("cart:cart"))
        
        # SEND BUDGE
        form = BudgetRequestModelForm(request.POST)
        cart = request.session.get("cart", [])

        products = Products.objects.filter(id__in=cart)

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
            BudgetRequest.objects.create(
                name=name,
                phone=phone,
                email=email,
                products=products,
                message=message,
            )


            send_mail(
                subject="[Site Gazil] Novo Pedido de Orçamento",
                message=body,
                from_email=os.getenv('DEFAULT_FROM_EMAIL', ''),
                recipient_list=[os.getenv('EMAIL_RECIPIENT_LIST', '')],
                fail_silently=False,
            )

            

            request.session["cart"] = []
            return render(
                request,
                "cart/cart.html",
                {
                    "products": [],
                    "form": BudgetRequestModelForm(),
                    "success": True,
                }
            )

        return render(
            request,
            "cart/cart.html",
            {
                "products": products,
                "form": form,
            }
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breadcrumbs"] = [
            {"name": "Home", "url": reverse("website:home")},
            {"name": "Produtos", "url": reverse("products:index")},
            {"name": "Carrinho", "url": None},
        ]
        return context
    

class AddToCartView(View):

    def post(self, request, slug_product):
        product = get_object_or_404(Products, slug_product=slug_product)
        cart = request.session.get("cart", [])
        
        if product.id not in cart:
            cart.append(product.id)
            request.session["cart"] = cart
            messages.success(
                request,
                "Produto adicionado com sucesso!"
            )
        else:
            messages.info(
                request,
                f"Produto já está no carrinho."
            )

        return redirect(
            request.META.get('HTTP_REFERER', 'products:list_product')
        )
    