from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', include('account.urls')),
]