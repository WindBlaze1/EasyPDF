from django.urls import path, include
from pdf_management import views

urlpatterns = [
    path('',views.index),
    path('pdf/',views.pdf_read,name='pdf_read'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('login/',views.login),
    path('signup/',views.signup),
]