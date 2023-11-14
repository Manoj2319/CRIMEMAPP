from django.urls import path
from .views import patient_complaints

urlpatterns = [
    path('', patient_complaints, name='register_complaint'),
]
