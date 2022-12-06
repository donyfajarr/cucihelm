from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.layanan)
admin.site.register(models.pelanggan)
admin.site.register(models.pemesanan)
admin.site.register(models.detaillayanan)