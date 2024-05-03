# urls.py

from django.urls import path
from . import views

app_name = 'your_app_name'

urlpatterns = [
    path('blood-type-details/', views.blood_type_details, name='blood_type_details'),
]