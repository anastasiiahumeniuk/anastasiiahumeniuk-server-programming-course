
from .models import Guest, Room, Booking, Payment, Feedback, Service, ServiceCategory, RoomType, RoomMaintenance, BookingService

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

class GuestRepository(BaseRepository):
    def __init__(self):
        super().__init__(Guest)

class RoomRepository(BaseRepository):
    def __init__(self):
        super().__init__(Room)

class BookingRepository(BaseRepository):
    def __init__(self):
        super().__init__(Booking)

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

class BookingServiceRepository(BaseRepository):
    def __init__(self):
        super().__init__(BookingService)

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
        self.booking_services = BookingServiceRepository()

