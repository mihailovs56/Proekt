from django.contrib import admin
from django.urls import path
from register.views import signup, signin, logout, pers

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', logout, name='logout'),
    path('pers/', pers, name='pers'),
]
