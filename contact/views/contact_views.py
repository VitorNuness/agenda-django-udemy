from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from contact.models import Contact

def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos'
        
    }

    return render(
        request,
        'contact/index.html',
        context=context,
    )

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == "":
        return redirect('contact:index')

    contacts = Contact.objects.filter(show=True)\
                              .filter(
                                  Q(first_name__icontains=search_value) |
                                  Q(last_name__icontains=search_value) |
                                  Q(phone__icontains=search_value) |
                                  Q(email__icontains=search_value) |
                                  Q(id__icontains=search_value)
                                  )\
                              .order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Search',
        'seach_value': search_value
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
