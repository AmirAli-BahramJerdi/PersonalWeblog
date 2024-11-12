# forms.py
import re
from django.core.exceptions import ValidationError
from django import forms
from .models import Message

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'fname': forms.TextInput(attrs={ 'placeholder':"نام"}),
            'lname': forms.TextInput(attrs={ 'placeholder':"نام خانوادگی"}),
            'email': forms.EmailInput(attrs={ 'placeholder':"ایمیل"}),
            'phone_number': forms.TextInput(attrs={ 'placeholder':"شماره تماس", 'required':True}),
            'service_type': forms.Select(attrs={'class': 'tj-nice-select', }),
            'message': forms.Textarea(attrs={ 'placeholder':"متن"}),
        }
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        phone_regex = r'^09\d{9}$'
        if not re.match(phone_regex, phone_number):
            raise ValidationError("شماره تلفن باید به فرمت صحیح وارد شود.")
        return phone_number
