from django.db import models

# Create your models here.
class Abc(models.Model):

    task = models.CharField(default="Равна ли С сумме A и B ?", max_length=256,verbose_name="Формулировка задачи")
    a = models.IntegerField(default=0, verbose_name="Значение А")
    b = models.IntegerField(default=0, verbose_name="Значение B")
    c = models.IntegerField(default=0, verbose_name="Значение С")



# python manage.py makemigrations
# python manage.py migrate


# admin.py
# from django.contrib import admin
# # Register your models here.
# from .models import Abc
# admin.site.register(Abc)



# forms.py
# from django.forms import ModelForm
# from .models import Abc
#
# class CreateAbcForm(ModelForm):
#     class Meta:
#         model = Abc
#         fields = ['task', 'a' ,'b' ,'c', 'c_calc']

