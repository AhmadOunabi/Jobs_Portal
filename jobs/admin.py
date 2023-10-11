from django.contrib import admin
from .models import Jobs,Category
#from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
admin.site.register(Jobs)
admin.site.register(Category)

