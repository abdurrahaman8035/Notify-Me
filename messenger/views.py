from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Contact
from django.urls import reverse, reverse_lazy

# Create your views here.

# class homeView(TemplateView):
#     template_name = 'index.html'
#     model = 'Contact'
#     contacts = Contact.objects.get()


def homeView(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html', {'contacts': contacts})


class createContact(CreateView):
    model = Contact
    fields = ['name', 'phone_number', 'id_number']
    template_name = 'create_contact.html'


class updateContact(UpdateView):
    model = Contact
    fields = '__all__'
    template_name = 'update_contact.html'
    context_object_name = 'contact'


class deleteContact(DeleteView):
    model = Contact
    template_name = 'delete_contact.html'
    success_url = reverse_lazy('home')
    context_object_name = 'contact'


class templateView(TemplateView):
    template_name = 'about_me.html'
