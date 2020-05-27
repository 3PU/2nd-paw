from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
import sweetify


def index(request):
    """Returns the index.html file"""
    return render(request, 'index.html')


def faq(request):
    """Returns the faq.html file"""
    return render(request, 'faq.html')


def contact(request):
    """Returns the contact.html file with the contact form"""
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(
                    subject,
                    message,
                    from_email,
                    ['support@2ndpaws.com']
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            sweetify.sweetalert(
                request,
                """Your message has been sent!
                We aim to reply to you within 24 hours.""",
                icon="success"
            )
            return redirect('index')
    return render(request, "contact.html", {'form': form})
