from django.contrib import admin
from .models import GenericFileUpload


admin.site.register((GenericFileUpload, ))
