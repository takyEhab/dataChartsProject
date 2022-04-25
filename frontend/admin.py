from django.contrib import admin

from .models import ExpiryDate, Strike

# Register your models here.
admin.site.register(ExpiryDate)
admin.site.register(Strike)
# admin.site.register(Instrument)