
from .models import Guest, Room, Booking, Payment, Feedback, Service, ServiceCategory, RoomType, RoomMaintenance

from django.db.models import Avg, Sum

class BaseRepository:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        return self.model.objects.all()

    def get_by_id(self, id):
        try:
            return self.model.objects.get(id=id)
        except self.model.DoesNotExist:
            return None

    def create(self, **kwargs):
        instance = self.model.objects.create(**kwargs)
        return instance

    def update(self, id, **kwargs):
        obj = self.get_by_id(id)
        if obj:
            for key, value in kwargs.items():
                setattr(obj, key, value)
            obj.save()
        return obj

    def delete(self, id):
        obj = self.get_by_id(id)
        if obj:
            obj.delete()
            return True
        return False

class GuestRepository(BaseRepository):
    def __init__(self):
        super().__init__(Guest)

class RoomRepository(BaseRepository):
    def __init__(self):
        super().__init__(Room)

class BookingRepository(BaseRepository):
    def __init__(self):
        super().__init__(Booking)

    def get_aggregated_report(self):
        total_bookings = self.model.objects.count()
        active_bookings = self.model.objects.filter(booking_status='active').count()
        completed_bookings = self.model.objects.filter(booking_status='completed').count()
        cancelled_bookings = self.model.objects.filter(booking_status='cancelled').count()

        total_revenue = Payment.objects.aggregate(total=Sum('amount'))['total'] or 0
        avg_payment_per_booking = Payment.objects.aggregate(avg=Avg('amount'))['avg'] or 0

        report = {
            'total_bookings': total_bookings,
            'active_bookings': active_bookings,
            'completed_bookings': completed_bookings,
            'cancelled_bookings': cancelled_bookings,
            'total_revenue': total_revenue,
            'average_payment_per_booking': avg_payment_per_booking,
        }
        return report

class PaymentRepository(BaseRepository):
    def __init__(self):
        super().__init__(Payment)

class FeedbackRepository(BaseRepository):
    def __init__(self):
        super().__init__(Feedback)

class ServiceRepository(BaseRepository):
    def __init__(self):
        super().__init__(Service)

class ServiceCategoryRepository(BaseRepository):
    def __init__(self):
        super().__init__(ServiceCategory)

class RoomTypeRepository(BaseRepository):
    def __init__(self):
        super().__init__(RoomType)

class RoomMaintenanceRepository(BaseRepository):
    def __init__(self):
        super().__init__(RoomMaintenance)

class HotelRepository:
    def __init__(self):
        self.guests = GuestRepository()
        self.rooms = RoomRepository()
        self.bookings = BookingRepository()
        self.payments = PaymentRepository()
        self.feedbacks = FeedbackRepository()
        self.services = ServiceRepository()
        self.service_categories = ServiceCategoryRepository()
        self.room_types = RoomTypeRepository()
        self.room_maintenances = RoomMaintenanceRepository()
