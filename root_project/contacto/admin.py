from . import models, forms
from django.contrib import admin

class ContactoAdmin(admin.ModelAdmin):
    form = forms.ContactoForm

admin.site.register(models.Contacto, ContactoAdmin)




