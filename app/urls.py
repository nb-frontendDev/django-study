from django.urls import path
from app import views

urlpatterns = [
    pasth('', views.IndexView.as_view(), name='index'),
]