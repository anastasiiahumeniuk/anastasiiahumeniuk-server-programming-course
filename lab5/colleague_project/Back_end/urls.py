from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
import core.views as views


router = DefaultRouter()
router.register(r'agents', views.AgentViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'properties', views.PropertyViewSet)
router.register(r'operations', views.OperationViewSet)
router.register(r'appointments', views.AppointmentViewSet)
router.register(r'rentals', views.RentalViewSet)
router.register(r'payments', views.PaymentViewSet)
router.register(r'commissions', views.CommissionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('report/', views.ReportView.as_view(), name='report'),
]

