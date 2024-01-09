

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import AdoptionForm
from.models import Animale
# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def cat(request):
    animals=Animale.objects.filter(type="chat")
    context={'animals':animals}
    return render(request,'cat.html',context)

def dog(request):
    animals=Animale.objects.filter(type="chien")
    context={'animals':animals}
    return render(request,'dog.html',context)

def ois(request):
    animals=Animale.objects.filter(type="ois")
    context={'animals':animals}
    return render(request,'ois.html',context)

def adoption_form(request):
    if request.method == 'POST':
        form = AdoptionForm(request.POST)
        if form.is_valid():
            # Traitement du formulaire et envoi de l'e-mail de confirmation
            form.save()
            send_mail(
                'Confirmation de demande d\'adoption',
                'Merci pour votre demande d\'adoption. Nous traiterons votre demande sous peu.',
                settings.DEFAULT_FROM_EMAIL,
                [form.cleaned_data['adresse']],
                fail_silently=True,
            )
            return render(request, 'confirmation.html')
    else:
        form = AdoptionForm()
    return render(request, 'adoption_form.html', {'form': form})

