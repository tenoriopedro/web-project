import os
import dotenv
from django.http import Http404
from django.core.cache import cache
from django.utils import timezone
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse
from site_setup.models import SiteSetup
from website.models import FeaturedProducts, WhyGazil
from website.forms import ContactsModelForm
from utils.mixins import get_website_breadcrumbs


dotenv.load_dotenv()


def home(request):
    site_setup = SiteSetup.objects.first()
    banners = site_setup.banners.filter(is_active=True)\
        .order_by('order') if site_setup else []
    featured_products = FeaturedProducts.objects.all()
    why_gazil = WhyGazil.objects.order_by('id')

    return render(
        request,
        'website/pages/home.html',
        {
            'why_gazil': why_gazil,
            'featured_products': featured_products,
            'banners': banners,
            'site_setup': site_setup,
        }
    )


def contacts(request):

    breadcrumbs = get_website_breadcrumbs(extra=[
        {"name": "Contatos", "url": ""}
    ])
    site_setup = SiteSetup.objects.first()
    contacts = site_setup.contacts.first()
    company_email = os.getenv('EMAIL_RECIPIENT_LIST', '')
    ip = get_client_ip(request)
    time_limit = 300  # 5 min

    # Extract from page
    if request.method == "POST":

        form_contact = ContactsModelForm(request.POST)

        # Check cache.
        # The user sends in succession
        # (5-minute interval), raises an error
        if cache.get(f"blocked_{ip}"):
            form_contact.add_error(
                None,
                "❌ Aguarde alguns minutos antes de enviar novamente.",
            )

        # Sending time check (Bot protection)
        started_at = request.session.get('form_started_at')
        if started_at:
            elapsed = (
                timezone.now() - timezone.datetime.fromisoformat(started_at)).\
                    total_seconds()

            if elapsed < 5:
                form_contact.add_error(
                    None,
                    '❌ Erro ao processar dados. Tente novamente.'
                )

        if form_contact.is_valid():

            first_name = form_contact.cleaned_data['first_name']
            last_name = form_contact.cleaned_data['last_name']
            email = form_contact.cleaned_data['email']
            message = form_contact.cleaned_data['message']

            # Send Email
            send_mail(
                subject=(
                    f"[Página Contatos] Mensagem de {first_name} {last_name}"
                ),
                message=f"Mensagem:\n{message}\n\nEmail de contato: {email}",
                from_email=os.getenv('DEFAULT_FROM_EMAIL', ''),
                recipient_list=[company_email],
                fail_silently=False,
            )

            # Save in database
            form_contact.save()

            # Indicates that the submission was valid
            request.session['form_sucesso'] = True

            # Block IP for 5 minutes, to avoid SPAM
            cache.set(f"blocked_{ip}", True, timeout=time_limit)

            return redirect("website:success_form")

    else:
        form_contact = ContactsModelForm()

        # Stores form opening time
        request.session['form_started_at'] = timezone.now().isoformat()

    return render(
        request,
        'website/pages/contacts.html',
        {
            'contacts': contacts,
            'form_contact': form_contact,
            'breadcrumbs': breadcrumbs,
        }
    )


def get_client_ip(request):
    # Function to get the visitor's real IP
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded_for:
        return forwarded_for.split(',')[0]

    return request.META.get('REMOTE_ADDR')


def success_form(request):

    # Check the request (Try to access the page directly).
    # If negative, raise the error
    if not request.session.get('form_sucesso'):
        raise Http404("Página não encontrada.")

    breadcrumbs = get_website_breadcrumbs(extra=[
        {"name": "Contatos", "url": reverse("website:contacts")},
        {"name": "Sucesso", "url": ""}
    ])

    del request.session['form_sucesso']

    # If positive (form submitted successfully) render the html
    return render(
        request,
        'website/pages/success_form.html',
        {
            "breadcrumbs": breadcrumbs,
        }
    )


def who_we_are(request):
    breadcrumbs = get_website_breadcrumbs(extra=[
        {"name": "Quem Somos", "url": ""}
    ])
    return render(
        request,
        'website/pages/who_we_are.html',
        {
            'breadcrumbs': breadcrumbs,
        }
    )
