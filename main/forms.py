from django.forms import ModelForm
from .models import Abc


class CreateAbcForm(ModelForm):
    class Meta:
        model = Abc
        # fields = '__all__'
        # print('\nfields: ', fields)
        fields = ['task', 'a', 'b', 'c']
        print('\nfields: ', fields)
