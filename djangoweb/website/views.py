from django.shortcuts import render
from site_setup.models import SiteSetup

def home(request):
    site_setup = SiteSetup.objects.first()
    banners = site_setup.banners.filter(is_active=True).order_by('order') if site_setup else []

    return render(
        request,
        'website/pages/home.html',
        {
            'banners': banners,
            'site_setup': site_setup,
        }
    )

def contacts(request):
    return render(
        request,
        'website/pages/contacts.html'
    )

def who_we_are(request):
    return render(
        request,
        'website/pages/who_we_are.html'
    )
