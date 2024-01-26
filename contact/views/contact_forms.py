from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from contact.forms import ContactForm
from contact.models import Contact

@login_required(login_url='contact:login')
def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        context = {
            'site_title': 'Criar Contato',
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect('contact:update', id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context=context,
        )

    context = {
            'site_title': 'Criar Contato',
            'form': ContactForm(),
            'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context=context,
    )

@login_required(login_url='contact:login')
def update(request, id):
    contact = get_object_or_404(Contact, pk=id, show=True, owner=request.user)
    form_action = reverse('contact:update', args=(id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        context = {
            'site_title': 'Criar Contato',
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context=context,
        )

    context = {
            'site_title': 'Criar Contato',
            'form': ContactForm(instance=contact),
            'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context=context,
    )

@login_required(login_url='contact:login')
def delete(request, id):
    contact = get_object_or_404(
        Contact, pk=id, show=True, owner=request.user
    )
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render(
        request,
        'contact/show.html',
        {
            'contact': contact,
            'confirmation': confirmation,
        }
    )