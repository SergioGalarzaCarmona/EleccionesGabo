from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterUser
from .models import Profile


# Create your views here.

def logIn(request):
    if request.method == 'GET':
        return render(request, 'Users/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return render(request, 'Users/login.html',{
                'error' : 'Usuario o contraseña incorrectos',
                })

def logOut(request):
    logout(request)
    return redirect('login')


def signUp(request):
    
    if request.method == 'GET':
        return render(request, 'Users/signUp.html', {
            'form': RegisterUser(),
        })
    else:
        form = RegisterUser(request.POST)
        if not form.is_valid():
                return render(request, 'Users/signUp.html', {
                    'form': RegisterUser(request.POST,request.FILES),
                })
        user = form.save()
        Profile.objects.create(user=user)
        login(request, user)
        return redirect('main')