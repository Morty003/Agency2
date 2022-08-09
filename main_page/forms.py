from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'id': 'name',
                                'type': 'text',
                                'placeholder': 'Your Name *',
                                'data-sb-validations': 'required',
    }))


    email = forms.CharField(max_length=254,
                            widget=forms.EmailInput({
                                'class': 'form-control',
                                'id': 'email',
                                'type': 'email',
                                'placeholder': 'Your Email *',
                                'data-sb-validations': 'required,email',
                            }))


    phone = forms.CharField(max_length=12,
                            widget=forms.NumberInput({
                                'class': 'form',
                                'id': 'phone',
                                'type': 'tel',
                                'placeholder': 'Your Phone *',
                                'data-sb-validations': 'required',
                            }))


    message = forms.CharField(max_length=500,
                              widget=forms.Textarea({
                                  'class': 'form-control',
                                  'id': 'message',
                                  'placeholder': 'Your Message *',
                                  'data-sb-validations': 'required'
                              }))

    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'phone', 'message')