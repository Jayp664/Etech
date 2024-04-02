from django.contrib import admin
from .models import Contact,Category,SubCategory,Product,customerOrder

# Register your models here.
admin.site.register((Contact,Category,SubCategory,Product,customerOrder))