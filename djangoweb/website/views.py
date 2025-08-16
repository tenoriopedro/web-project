import os
import dotenv
from django.http import Http404
from django.core.cache import cache
from django.utils import timezone
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from site_setup.models import SiteSetup
from website.models import FeaturedProducts, WhyGazil
from website.forms import ContactsModelForm


dotenv.load_dotenv()

def home(request):
    site_setup = SiteSetup.objects.first()
    banners = site_setup.banners.filter(is_active=True).order_by('order') if site_setup else []
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

    site_setup = SiteSetup.objects.first()
    contacts = site_setup.contacts.first()
    company_email = os.getenv('EMAIL_RECIPIENT_LIST', '')
    ip = get_client_ip(request)
    time_limit = 300 # 5 minutos

    # Extrair da página
    if request.method == "POST":
        
        form_contact = ContactsModelForm(request.POST)

        # Verificar cache. 
        # O usuário enviar de forma seguida
        # (intervalo de 5 minutos), levanta um erro.
        if cache.get(f"blocked_{ip}"):
            form_contact.add_error(
                None,
                "Aguarde alguns minutos antes de enviar novamente.",
            )

        # Verificação do tempo de envio(Proteção contra bots)
        started_at = request.session.get('form_started_at')
        if started_at:
            elapsed = (timezone.now() - timezone.datetime.fromisoformat(started_at)).total_seconds()

            if elapsed < 5:
                form_contact.add_error(
                    None,
                    'Erro ao processar dados. Tente novamente.'
                )

        if form_contact.is_valid():
            
            first_name = form_contact.cleaned_data['first_name']
            last_name = form_contact.cleaned_data['last_name']
            email = form_contact.cleaned_data['email']
            message = form_contact.cleaned_data['message']

            # Enviar Email
            send_mail(
                subject=f"[Página Contatos] Mensagem de {first_name} {last_name}",
                message=f"Mensagem:\n{message}\n\nEmail de contato: {email}",
                from_email=os.getenv('DEFAULT_FROM_EMAIL', ''),
                recipient_list=[company_email],
                fail_silently=False,
            )

            # Salva no banco de dados
            form_contact.save()

            # Sinaliza que o envio foi válido
            request.session['form_sucesso'] = True

            # Bloqueia IP por 5 minutos, para evitar SPAM
            cache.set(f"blocked_{ip}", True, timeout=time_limit)

            return redirect("website:success_form")

    else:
        form_contact = ContactsModelForm()

        # Armazena hora de abertura do formulário
        request.session['form_started_at'] = timezone.now().isoformat()

    
    return render(
        request,
        'website/pages/contacts.html',
        {
            'contacts': contacts,
            'form_contact': form_contact,
        }
    )


def get_client_ip(request):
    # Função para obter o ip real do visitante
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded_for:
        return forwarded_for.split(',')[0]
    
    return request.META.get('REMOTE_ADDR')


def success_form(request):

    # Verificar a requisição(Tentar acessar a página de forma direta). 
    # Sendo negativa, levanta o erro.
    if not request.session.get('form_sucesso'):
        raise Http404("Página não encontrada.")
    
    del request.session['form_sucesso']

    # Se positiva(formulário enviado com sucesso) renderiza o html
    return render(request, 'website/pages/success_form.html')


def who_we_are(request):
    return render(
        request,
        'website/pages/who_we_are.html'
    )
