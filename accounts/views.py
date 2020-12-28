from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.
def register(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if User.objects.filter(email=email).exists():
            storage = messages.get_messages(request)
            storage.used = True

            messages.error(request, 'Email has already been registered')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            storage = messages.get_messages(request)
            storage.used = True

            messages.error(request, 'Username has already been taken')
            return redirect('register')

        if password != password2:
            storage = messages.get_messages(request)
            storage.used = True

            messages.error(request, 'Passwords do not match')
            return redirect('register')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        user.save
        storage = messages.get_messages(request)
        storage.used = True

        messages.success(request, 'Your account has been created')
        return redirect('login')

    return render(request, 'accounts/register.html')

def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if not User.objects.filter(email=email).exists():
            storage = messages.get_messages(request)
            storage.used = True

            messages.error(request, 'Email is not registered')
            return redirect('login')

        # username = User.objects.filter(email=email)[0].username
        username = get_object_or_404(User, email=email).username

        user = User.objects.filter(email=email)

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('index')
        else:
            storage = messages.get_messages(request)
            storage.used = True

            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    return render(request, 'accounts/login.html')

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('index')