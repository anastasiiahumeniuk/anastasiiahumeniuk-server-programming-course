from django.urls import path
from . import views

from .views import (
    BookingReportApiView
)
urlpatterns = [
    path('', views.index),
    path('guests/', views.GuestApiView.as_view()),
    path('guests/<int:pk>/', views.GuestApiView.as_view()),
    path('rooms/', views.RoomApiView.as_view()),
    path('rooms/<int:pk>/', views.RoomApiView.as_view()),
    path('bookings/', views.BookingApiView.as_view()),
    path('bookings/<int:pk>/', views.BookingApiView.as_view()),
    path('payments/', views.PaymentApiView.as_view()),
    path('payments/<int:pk>/', views.PaymentApiView.as_view()),
    path('feedbacks/', views.FeedbackApiView.as_view()),
    path('feedbacks/<int:pk>/', views.FeedbackApiView.as_view()),
    path('services/', views.ServiceApiView.as_view()),
    path('services/<int:pk>/', views.ServiceApiView.as_view()),
    path('service-categories/', views.ServiceCategoryApiView.as_view()),
    path('service-categories/<int:pk>/', views.ServiceCategoryApiView.as_view()),
    path('room-types/', views.RoomTypeApiView.as_view()),
    path('room-types/<int:pk>/', views.RoomTypeApiView.as_view()),
    path('room-maintenance/', views.RoomMaintenanceApiView.as_view()),
    path('room-maintenance/<int:pk>/', views.RoomMaintenanceApiView.as_view()),
    path('bookings/report/', BookingReportApiView.as_view()),
]
