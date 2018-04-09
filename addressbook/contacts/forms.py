from django import forms
from datetime import date
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'cell', 'email', 'address', 'dob')
        widgets = {
            'email': forms.EmailInput(attrs={}),
            'dob': forms.SelectDateWidget(years=range(date.today().year - 100, date.today().year)),
            'address': forms.Textarea(attrs={'cols':50, 'rows':5}),
        }
