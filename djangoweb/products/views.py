from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import (
    Products, ProductsSetup, SobMedidaPortfolio, SobMedidaRequest)
from .forms import SobMedidaRequestModelForm
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.urls import reverse_lazy
import os
from utils.mixins import BreadcrumbsMixin


class ProductsIndexView(BreadcrumbsMixin, TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["categories"] = ProductsSetup.objects.all()
        return context

    def get_breadcrumbs(self):
        return [
            {"name": "Home", "url": reverse("website:home")},
            {"name": "Produtos", "url": reverse("products:index")},
        ]


class ProductsListView(BreadcrumbsMixin, ListView):
    model = Products
    template_name = 'products/list_products.html'
    context_object_name = 'products'
    paginate_by = 8

    def get_queryset(self):
        category_slug = self.kwargs['slug_category']
        self.category = ProductsSetup.objects.get(slug_category=category_slug)

        queryset = Products.objects.filter(
            product_type=self.category
        )

        order = self.request.GET.get('order', 'name')
        if order in ['name', '-name', 'id', '-id']:
            queryset = queryset.order_by(order)

        return queryset

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['current_order'] = self.request.GET.get('order', 'name')
        context['slug_category'] = self.category.slug_category
        context['name_category'] = self.category
        context["is_search"] = False

        return context

    def get_breadcrumbs(self):
        return [
            {"name": "Home", "url": reverse("website:home")},
            {"name": "Produtos", "url": reverse("products:index")},
            {
                "name": self.category.product_type.text,
                "url": self.category.get_absolute_url()
             },
        ]


class ProductDetailView(BreadcrumbsMixin, DetailView):
    model = Products
    template_name = 'products/detail_product.html'
    context_object_name = 'products'
    slug_url_kwarg = "slug_product"

    def get_object(self):

        slug_product = self.kwargs.get("slug_product")

        return get_object_or_404(
            Products,
            slug_product=slug_product
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object

        related_products = (
            Products.objects.filter(
                product_type=product.product_type
            ).exclude(id=product.id)[:4]
        )
        context["related_products"] = related_products
        context["slug_category"] = self.kwargs.get('slug_category')
        context["product"] = product

        return context

    def get_breadcrumbs(self):
        product = self.get_object()
        category = product.product_type
        return [
            {"name": "Home", "url": reverse("website:home")},
            {"name": "Produtos", "url": reverse("products:index")},
            {"name": category, "url": category.get_absolute_url()},
            {"name": product.name, "url": product.get_absolute_url()},
        ]


class ProductsSearchView(ListView):
    model = Products
    template_name = 'products/list_products.html'
    context_object_name = "products"
    paginate_by = 8

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        queryset = Products.objects.all().select_related("product_type")

        if query:

            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(short_description__icontains=query) |
                Q(product_type__slug_category__icontains=query)
            )

        return queryset

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("q", "")
        context["q"] = query
        context["is_search"] = True
        context["breadcrumbs"] = [
            {"name": "Home", "url": reverse("website:home")},
            {"name": "Produtos", "url": reverse("products:index")},
            {"name": f"Pesquisa por '{query}'", "url": None},
        ]
        return context


class CustomMadeView(BreadcrumbsMixin, CreateView):
    model = SobMedidaRequest
    form_class = SobMedidaRequestModelForm
    template_name = 'products/sob_medida_page.html'
    success_url = reverse_lazy('products:custom-made')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery_items'] = SobMedidaPortfolio.objects.all()
        context['page_title'] = 'Projetos Sob Medida'

        return context

    def get_breadcrumbs(self):
        return [
            {"name": "Home", "url": reverse("website:home")},
            {"name": "Produtos", "url": reverse("products:index")},
            {"name": "Projetos Sob Medida", "url": None},
        ]

    def form_valid(self, form):

        client_order = form.save()

        try:
            self.send_custom_quote_email(client_order)
            messages.success(
                self.request,
                'Pedido de orçamento enviado com sucesso!'
            )
        except Exception as e:
            # Caso o email falhe
            messages.error(
                self.request,
                ('O seu pedido foi salvo, mas houve um erro ao enviar a'
                    'notificação.'
                    'Entraremos em contato em breve.')
            )
            # Log erro
            print(f"Erro ao enviar email de pedido sob medida: {e}")

        return super().form_valid(form)

    def form_invalid(self, form):

        messages.error(
            self.request,
            'Formulário inválido. Corrija os erros abaixo.'
        )
        return super().form_invalid(form)

    def send_custom_quote_email(self, order_obj):

        subject = "[Site Gazil] Novo Pedido de Orçamento SOB MEDIDA"

        body = (
            "Novo pedido de orçamento SOB MEDIDA recebido: \n\n"
            f"Cliente: {order_obj.name}\n"
            f"Telefone: {order_obj.phone}\n"
            f"Email: {order_obj.email}\n"
            "---------------------------------------------------\n\n"
            "Descrição do Projeto:\n"
            f"{order_obj.project_description}\n"
        )

        from_email = os.getenv(
            'DEFAULT_FROM_EMAIL', settings.DEFAULT_FROM_EMAIL
        )
        recipient_list = [os.getenv(
            'EMAIL_RECIPIENT_LIST', 'pstsouza10@gmail.com'
            )
        ]

        email = EmailMessage(
            subject=subject,
            body=body,
            from_email=from_email,
            to=recipient_list
        )

        if order_obj.attachment:

            email.attach_file(order_obj.attachment.path)
            body += "\n\nAVISO: Este pedido contém um ficheiro em anexo."

        email.send(fail_silently=False)
