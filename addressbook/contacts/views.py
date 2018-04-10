from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Contact
from .forms import ContactForm

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'contacts/index.html'
    context_object_name = 'contacts_list'

    def get_queryset(self):
        return Contact.objects.order_by('id')

class DetailView(generic.DetailView):
    model = Contact
    template_name = 'contacts/details.html'

def add(request, pk=None):
    # Check to see if a key has been sent. If true then allow edit functionality.
    if pk == None:
        form = ContactForm()
    else:
        contact = get_object_or_404(Contact, pk=pk)
        form = ContactForm(request.POST or None, instance=contact)

    return render(request, 'contacts/add.html', {'form': form,})

def add(request, pk=None):
    # Check to see if a key has been sent. If true then allow edit functionality.
    if pk == None:
        return render(request, 'contacts/add.html', {'form': ContactForm(),})
    else:
        contact = get_object_or_404(Contact, pk=pk)
        form = ContactForm(request.POST or None, instance=contact)
        return render(request, 'contacts/add.html', {'form': form, 'contact': contact})

def save(request, pk=None):
    if request.method == "POST":
        # If a key is sent then get the object and dupdate it.
        if pk == None:
            form = ContactForm(request.POST)
        else:
            contact = get_object_or_404(Contact, pk=pk)
            form = ContactForm(request.POST or None, instance=contact)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return HttpResponseRedirect(reverse('contacts:detail', args=(contact.id,)))
        else:
            return render(request, 'contacts/add.html', {'form': form, 'error_message': "Please enter all the contact information required.",})
    else:
        return render(request, 'contacts/add.html', {'form': ContactForm(), 'error_message': "Please re-enter the contact.",})

def delete(request, pk):
    # Check to see if a key has been sent then delete
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return HttpResponseRedirect(reverse('contacts:index'))
