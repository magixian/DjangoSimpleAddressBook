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

def add(request):
    return render(request, 'contacts/add.html', {'form': ContactForm(),})

def save(request):
    #contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return HttpResponseRedirect(reverse('contacts:detail', args=(contact.id,)))
        else:
            return render(request, 'contacts/add.html', {'form': form, 'error_message': "Pleas enter all the contact information required.",})
    else:
        return render(request, 'contacts/add.html', {'form': ContactForm(), 'error_message': "Please re-enter the contact.",})
