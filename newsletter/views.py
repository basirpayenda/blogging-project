

from django.shortcuts import render, redirect
from .models import NewsLetterUserList, SendEmailToNewsLetterUser
from .forms import NewsLetterUserListForm, SendEmailToNewsLetterUserForm
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template
from django.utils.safestring import mark_safe


def newsletter_subscribe(request):
    if request.method == 'POST':
        form = NewsLetterUserListForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if NewsLetterUserList.objects.filter(email=instance.email).exists():
                messages.success(request, 'This email is already registered!')
            else:
                instance.save()
                subject, recipient_list = 'Subscribed Successfully', [
                    instance.email]
                from_email = settings.EMAIL_HOST_USER
                with open(settings.BASE_DIR + "\\newsletter\\templates\\newsletter\\email_txt.txt") as f:
                    body = f.read()
                message = EmailMultiAlternatives(
                    subject=subject, body=body, from_email=from_email, to=recipient_list)
                temp = get_template('newsletter/email.html').render()
                message.attach_alternative(temp, 'text/html')
                message.send()
                messages.success(
                    request, 'You successfully subscribed to our newsletter, please check your email')
                return redirect('blog-home')
    else:
        form = NewsLetterUserListForm()
    return render(request, 'blogApp/home.html', {'subscribe_form': form})


def newsletter_unsubscribe(request):
    form = NewsLetterUserListForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsLetterUserList.objects.filter(email=instance.email).exists():
            NewsLetterUserList.objects.filter(email=instance.email).delete()
            messages.success(
                request, 'We\'re sad to see you go :(')
            return redirect('blog-home')
        else:
            messages.success(request, 'Email doesn\'t exists!')

    return render(request, 'newsletter/unsubscribe.html', {'unsubscribe_form': form})


def send_newsletter(request):
    form = SendEmailToNewsLetterUserForm(request.POST or None)
    if form.is_valid():
        instance = form.save()

        if instance.status == 'Published':
            subject = instance.subject
            body = instance.body
            from_email = settings.EMAIL_HOST_USER

            for newsletter_obj in NewsLetterUserList.objects.all():
                msg = EmailMultiAlternatives(
                    subject, body, from_email, [newsletter_obj.email])
                msg.attach_alternative(body, "text/html")
                msg.send()

    return render(request, 'newsletter/send-email.html', {'form': form})
