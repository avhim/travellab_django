from django.forms import modelformset_factory, inlineformset_factory
from django import forms
from client.models import Client

ClientFormSet = modelformset_factory(Client, exclude=('email', 'invoice',),
                                     max_num=10, extra=0, min_num=1, validate_min=True,
                                     localized_fields=('date_passport_issue', 'date_passport_exp', 'date_birth',),
                                     widgets={'date_passport_issue': forms.DateInput(attrs={'type': 'date'}),
                                              'date_passport_exp': forms.DateInput(attrs={'type': 'date'}),
                                              'date_birth': forms.DateInput(attrs={'type': 'date'}),
                                              'phone_number': forms.TextInput(attrs={'type': 'tel'}),
                                              },
                                     )
