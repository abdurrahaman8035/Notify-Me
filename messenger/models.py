from django.db import models
from django.urls import reverse
import datetime

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=11)
    id_number = models.CharField(max_length=11)
    # date_added = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #         ordering = ['date_added']

    def __str__(self):
        return f'{self.name} :: {self.id_number.upper()}' 

    def get_absolute_url(self):  # new
        return reverse('home')
        
