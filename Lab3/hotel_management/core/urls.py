from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('guests/', views.guest_list, name='guest_list'),
    path('guests/<int:guest_id>/', views.guest_detail, name='guest_detail'),
]
