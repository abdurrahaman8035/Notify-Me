from django.urls import path
from django.views.generic.base import TemplateView
from .views import homeView, createContact, updateContact, deleteContact, templateView

urlpatterns = [
    path('', homeView, name='home'),
    path('contact/new/', createContact.as_view(), name='contact_new'),
    path('contact/edit/<int:pk>/', updateContact.as_view(), name='edit_contact'),
    path('contact/delete/<int:pk>/', deleteContact.as_view(), name='delete_contact'),
    path('about_me/', templateView.as_view(), name='about_me'),

]
