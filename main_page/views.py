from django.shortcuts import render, redirect
from .models import Team, About, Clients, Portfolio, Service, Footer
from .forms import ContactMessageForm

def main_page(request):
    if request.method == 'POST':
        contact_form = ContactMessageForm(request.POST)
        if contact_form.is_valid():
            return redirect('/')


    contact_form = ContactMessageForm()
    team = Team.objects.all()
    about = About.objects.all()
    clients = Clients.objects.all()
    portfolio = Portfolio.objects.all()
    service = Service.objects.all()
    footer = Footer.objects.all()

    return render(request, 'main_page.html', context={
        'team': team,
        'contact_form': contact_form,
        'about': about,
        'clients': clients,
        'portfolio': portfolio,
        'service': service,
        'footer': footer,


    })


