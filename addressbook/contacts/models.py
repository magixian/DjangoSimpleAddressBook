from datetime import date
from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=50)
    cell = models.CharField('Cell', max_length=20)
    email = models.EmailField('Email Address')
    address = models.CharField('Address', max_length=200)
    dob = models.DateField('Date Of Birth')

    def get_age(self):
        return date.today().year - self.dob.year
