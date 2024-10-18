from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('policies/', views.policies, name='policies'),
    path('<int:pk>/', views.cloth_detail, name='cloth_detail'),
]