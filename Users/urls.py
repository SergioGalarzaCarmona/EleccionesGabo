from django.urls import path
from .views import logIn, logOut, signUp

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', logIn, name='login'),
    path('logout/', logOut, name='logout'),
    path('signUp/', signUp, name='signup'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)