from django.contrib import admin
from .models import UploadFile, SubscribedEmail

admin.site.register(UploadFile)
admin.site.register(SubscribedEmail)