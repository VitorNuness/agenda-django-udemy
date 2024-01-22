from django.shortcuts import render, get_object_or_404
from contact.models import Contact

def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[0:10]

    context = {
        'contacts': contacts,
        'site_title': 'Contatos'
        
    }

    return render(
        request,
        'contact/index.html',
        context=context,
    )

def show(request, id):
    contact = get_object_or_404(Contact.objects.filter(pk=id, show=True))

    context = {
        'contact': contact,
        'site_title': f'{contact.first_name} {contact.last_name}'
    }

    return render(
        request,
        'contact/show.html',
        context=context,
    )
