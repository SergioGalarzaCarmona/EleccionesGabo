from django.urls import path
from .views import logIn, logOut, signUp

urlpatterns = [
    path('', logIn, name='login'),
    path('logout/', logOut, name='logout'),
    path('signUp/', signUp, name='signup'),
]