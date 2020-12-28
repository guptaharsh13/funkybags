from django.shortcuts import render, redirect
from django.contrib import messages

from .tasks import sendEmail

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def shop(request):
    return render(request, 'pages/shop.html')

def purchased(request):

    if request.user.is_authenticated:
        sendEmail.delay('ORDER CONFIRMATION - Funky Bags', 'You have successfully purchased a bag from Funky Bags...\n\nTHANK YOU for shopping with us...\nHave a great day ahead !!', request.user.email)

        storage = messages.get_messages(request)
        storage.used = True
        messages.success(request, 'Your order has been placed !!\nCheck your email for confirmation')
    else:
        storage = messages.get_messages(request)
        storage.used = True
        messages.error(request, 'We are SORRY !! You must be logged in to shop with us...')

    return redirect('index')