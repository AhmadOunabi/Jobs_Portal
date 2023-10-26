from django.contrib import admin
from .models import Jobs,Category,UserToken,UserProfile
#from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
admin.site.register(Jobs)
admin.site.register(Category)
admin.site.register(UserToken)
admin.site.register(UserProfile)


