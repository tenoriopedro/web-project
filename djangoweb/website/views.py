from django.shortcuts import render
from site_setup.models import SiteSetup
from website.models import FeaturedProducts, WhyGazil
import os
import dotenv

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
    google_api_key = os.environ['API_SECRET_KEY']


    return render(
        request,
        'website/pages/contacts.html',
        {
            'contacts': contacts,
            'google_api_key': google_api_key,
        }
    )

def who_we_are(request):
    return render(
        request,
        'website/pages/who_we_are.html'
    )
