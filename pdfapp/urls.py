from django.urls import path
from .views import pdf_list

urlpatterns = [
    path('', pdf_list, name='pdf_list'),
]
