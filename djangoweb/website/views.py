from django.shortcuts import render

def home(request):
    return render(
        request,
        'website/pages/home.html'
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
