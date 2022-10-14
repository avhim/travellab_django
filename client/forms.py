from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    fio_tourist = forms.CharField(label='',
                                  widget=forms.TextInput(
                                      attrs={'placeholder': 'Ваш ФИО', 'class': 'form-control', 'type': 'text'}
                                  ), )
    passport = forms.CharField(label='',
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Серия и номер паспорта', 'class': 'form-control',
                                          'type': 'text'}
                               ), )
    date_birth = forms.DateField(label='',
                                 widget=forms.TextInput(
                                     attrs={'placeholder': 'Дата рождения', 'class': 'form-control', 'type': 'date'}
                                 ), )
    phone_number = forms.CharField(label='',
                                   widget=forms.TextInput(
                                       attrs={'placeholder': 'Ваш телефон', 'class': 'form-control', 'type': 'tel'}
                                   ), )

    class Meta:
        model = Client
        fields = ['fio_tourist', 'passport', 'date_birth', 'phone_number']

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass