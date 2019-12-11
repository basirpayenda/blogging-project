from django.contrib import admin
from .models import NewsLetterUserList, SendEmailToNewsLetterUser

admin.site.register(NewsLetterUserList)
admin.site.register(SendEmailToNewsLetterUser)
