from .views import *
from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register, name='register'),
    path('oportunity/', oportunity, name='oportunity'),
    path('oportunity_detail/', oportunity_detail, name='oportunity_detail'),
    path('profile/',profile, name='profile'),
#    path('pdf/', generatePDF, name='pdf'),
]