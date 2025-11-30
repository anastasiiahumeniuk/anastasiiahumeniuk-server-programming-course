from django.urls import path
from . import views

app_name = "hotel_web"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),


    # Guests
    path('guests/', views.GuestListView.as_view(), name='guest_list'),
    path('guests/add/', views.GuestCreateView.as_view(), name='guest_add'),
    path('guests/<int:pk>/', views.GuestDetailView.as_view(), name='guest_detail'),
    path('guests/<int:pk>/edit/', views.GuestUpdateView.as_view(), name='guest_edit'),
    path('guests/<int:pk>/delete/', views.GuestDeleteView.as_view(), name='guest_delete'),

    # RoomType
    path('roomtypes/', views.RoomTypeListView.as_view(), name='roomtype_list'),
    path('roomtypes/add/', views.RoomTypeCreateView.as_view(), name='roomtype_add'),
    path('roomtypes/<int:pk>/', views.RoomTypeDetailView.as_view(), name='roomtype_detail'),
    path('roomtypes/<int:pk>/edit/', views.RoomTypeUpdateView.as_view(), name='roomtype_edit'),
    path('roomtypes/<int:pk>/delete/', views.RoomTypeDeleteView.as_view(), name='roomtype_delete'),

    # Rooms
    path('rooms/', views.RoomListView.as_view(), name='room_list'),
    path('rooms/add/', views.RoomCreateView.as_view(), name='room_add'),
    path('rooms/<int:pk>/', views.RoomDetailView.as_view(), name='room_detail'),
    path('rooms/<int:pk>/edit/', views.RoomUpdateView.as_view(), name='room_edit'),
    path('rooms/<int:pk>/delete/', views.RoomDeleteView.as_view(), name='room_delete'),

    # ServiceCategory
    path('categories/', views.ServiceCategoryListView.as_view(), name='servicecategory_list'),
    path('categories/add/', views.ServiceCategoryCreateView.as_view(), name='servicecategory_add'),
    path('categories/<int:pk>/', views.ServiceCategoryDetailView.as_view(), name='servicecategory_detail'),
    path('categories/<int:pk>/edit/', views.ServiceCategoryUpdateView.as_view(), name='servicecategory_edit'),
    path('categories/<int:pk>/delete/', views.ServiceCategoryDeleteView.as_view(), name='servicecategory_delete'),

    # Service
    path('services/', views.ServiceListView.as_view(), name='service_list'),
    path('services/add/', views.ServiceCreateView.as_view(), name='service_add'),
    path('services/<int:pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('services/<int:pk>/edit/', views.ServiceUpdateView.as_view(), name='service_edit'),
    path('services/<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='service_delete'),

    # Booking
    path('bookings/', views.BookingListView.as_view(), name='booking_list'),
    path('bookings/add/', views.BookingCreateView.as_view(), name='booking_add'),
    path('bookings/<int:pk>/', views.BookingDetailView.as_view(), name='booking_detail'),
    path('bookings/<int:pk>/edit/', views.BookingUpdateView.as_view(), name='booking_edit'),
    path('bookings/<int:pk>/delete/', views.BookingDeleteView.as_view(), name='booking_delete'),

    # Payment
    path('payments/', views.PaymentListView.as_view(), name='payment_list'),
    path('payments/add/', views.PaymentCreateView.as_view(), name='payment_add'),
    path('payments/<int:pk>/', views.PaymentDetailView.as_view(), name='payment_detail'),
    path('payments/<int:pk>/edit/', views.PaymentUpdateView.as_view(), name='payment_edit'),
    path('payments/<int:pk>/delete/', views.PaymentDeleteView.as_view(), name='payment_delete'),

    # Feedback
    path('feedbacks/', views.FeedbackListView.as_view(), name='feedback_list'),
    path('feedbacks/add/', views.FeedbackCreateView.as_view(), name='feedback_add'),
    path('feedbacks/<int:pk>/', views.FeedbackDetailView.as_view(), name='feedback_detail'),
    path('feedbacks/<int:pk>/edit/', views.FeedbackUpdateView.as_view(), name='feedback_edit'),
    path('feedbacks/<int:pk>/delete/', views.FeedbackDeleteView.as_view(), name='feedback_delete'),

    # RoomMaintenance
    path('maintenances/', views.RoomMaintenanceListView.as_view(), name='roommaintenance_list'),
    path('maintenances/add/', views.RoomMaintenanceCreateView.as_view(), name='roommaintenance_add'),
    path('maintenances/<int:pk>/', views.RoomMaintenanceDetailView.as_view(), name='roommaintenance_detail'),
    path('maintenances/<int:pk>/edit/', views.RoomMaintenanceUpdateView.as_view(), name='roommaintenance_edit'),
    path('maintenances/<int:pk>/delete/', views.RoomMaintenanceDeleteView.as_view(), name='roommaintenance_delete'),

    # BookingLog
    path('logs/', views.BookingLogListView.as_view(), name='bookinglog_list'),
    path('logs/add/', views.BookingLogCreateView.as_view(), name='bookinglog_add'),
    path('logs/<int:pk>/', views.BookingLogDetailView.as_view(), name='bookinglog_detail'),
    path('logs/<int:pk>/edit/', views.BookingLogUpdateView.as_view(), name='bookinglog_edit'),
    path('logs/<int:pk>/delete/', views.BookingLogDeleteView.as_view(), name='bookinglog_delete'),

    # Colleague project
    path('customers-table/', views.customers_table, name='customers-table'),
    path('customers/delete/<int:customer_id>/', views.delete_customer, name='delete-customer'),
]
