from django.urls import path, include
from .views import (
    home,
    about,
    contact,
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
