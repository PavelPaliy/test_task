from django.shortcuts import render

# Create your views here.
from .models import Main, Contacts, About


def index(request):
    blocks = Main.objects.all()
    return render(request, 'index.html', context={'blocks':blocks})

def about(request):
    blocks = About.objects.all()
    return render(request, 'about.html', context={'blocks':blocks})

def contacts(request):
    blocks = Contacts.objects.all()
    return render(request, 'contacts.html', context={'blocks':blocks})