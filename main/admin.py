from django.contrib import admin
from .models import Abc
# Register your models here.
@admin.register(Abc)
class Abc(admin.ModelAdmin):
    list_display = ['pk', 'task', 'a', 'b', 'c']
    search_fields = ['task', 'a', 'b', 'c']
    list_filter = ['task', 'a', 'b', 'c']
    list_per_page = 5


# admin.site.register(Abc)
