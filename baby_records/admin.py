from django.contrib import admin

# Register your models here.
from .models import Toileting, Feeding

admin.site.register(Toileting)
admin.site.register(Feeding)