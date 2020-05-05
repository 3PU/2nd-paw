from django.shortcuts import render

def index(request):
    """Returns the index.html file"""
    return render(request, 'index.html')

def faq(request):
    """Returns the faq.html file"""
    return render(request, 'faq.html')