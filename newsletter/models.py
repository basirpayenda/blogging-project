from django.db import models

# Create your models here.


class NewsLetterUserList(models.Model):
    email = models.EmailField(max_length=254)
    subscription_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class SendEmailToNewsLetterUser(models.Model):
    EMAIL_STATUS_CHOICES = (
        ("Draft", "Draft"),
        ("Published", "Published")
    )
    subject = models.CharField(max_length=250)
    body = models.TextField()
    status = models.CharField(max_length=10, choices=EMAIL_STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
