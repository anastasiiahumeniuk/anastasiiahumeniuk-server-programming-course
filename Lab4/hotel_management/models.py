from django.db import models
import uuid

class PaymentMethod(models.TextChoices):
    CASH = 'cash', 'Cash'
    CARD = 'card', 'Card'
    ONLINE = 'online', 'Online'


class PaymentStatus(models.TextChoices):
    PAID = 'paid', 'Paid'
    PENDING = 'pending', 'Pending'
    CANCELLED = 'cancelled', 'Cancelled'


class BookingStatus(models.TextChoices):
    ACTIVE = 'active', 'Active'
    COMPLETED = 'completed', 'Completed'
    CANCELLED = 'cancelled', 'Cancelled'


class MaintenanceType(models.TextChoices):
    CLEANING = 'cleaning', 'Cleaning'
    REPAIR = 'repair', 'Repair'
    INSPECTION = 'inspection', 'Inspection'
    OTHER = 'other', 'Other'


class Guest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    passport_series = models.CharField(max_length=10, default='TEMP')
    passport_number = models.CharField(max_length=10, default='0000000000')
    registration_date = models.DateTimeField(auto_now_add=True)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'guest'
        managed = True
        unique_together = ('passport_series', 'passport_number')

    def __str__(self):
        return f"{self.first_name} {self.last_name} | Email: {self.email} | Phone: {self.phone_number} | Passport: {self.passport_series}-{self.passport_number}"


class RoomType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    base_price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'room_type'

    def __str__(self):
        return f"{self.name} | Price: {self.base_price} | {self.description}"


class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    floor_number = models.SmallIntegerField(null=True, blank=True)
    capacity = models.SmallIntegerField()
    price_per_night = models.DecimalField(max_digits=7, decimal_places=2)
    status = models.CharField(max_length=20, default='available')
    description = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'room'

    def __str__(self):
        return f"Room {self.room_number} | Type: {self.room_type.name if self.room_type else 'N/A'} | Floor: {self.floor_number} | Capacity: {self.capacity} | Price/night: {self.price_per_night} | Status: {self.status}"


class ServiceCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'service_category'

    def __str__(self):
        return self.name


class Service(models.Model):
    service_name = models.CharField(max_length=45)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    service_description = models.CharField(max_length=200, null=True, blank=True)
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.SET_NULL, null=True)

    class Meta:
        managed = True
        db_table = 'service'

    def __str__(self):
        return f"{self.service_name} | Category: {self.service_category.name if self.service_category else 'N/A'} | Price: {self.price}"


class Booking(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    booking_status = models.CharField(
        max_length=20, choices=BookingStatus.choices, default=BookingStatus.ACTIVE
    )
    services = models.ManyToManyField(Service, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'booking'

    def total_price(self):
        room_price = self.room.price_per_night if self.room else 0
        services_price = sum(service.price for service in self.services.all())
        return room_price + services_price


def __str__(self):
    return f"Booking #{self.id} | Guest: {self.guest.first_name} {self.guest.last_name} | Room: {self.room.room_number} | Status: {self.booking_status}"


class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=PaymentMethod.choices)
    transaction_code = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    payment_status = models.CharField(max_length=10, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    partial_payment = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'payment'
        managed = True

    def __str__(self):
        return f"Payment #{self.id} | Booking #{self.booking.id} | Amount: {self.amount} | Method: {self.payment_method} | Status: {self.payment_status} | Transaction: {self.transaction_code}"


class Feedback(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    rating = models.SmallIntegerField()
    title = models.CharField(max_length=100, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'feedback'
        managed = True

    def __str__(self):
        return f"Feedback #{self.id} | Guest: {self.guest.first_name} {self.guest.last_name} | Booking #{self.booking.id} | Rating: {self.rating} | Public: {self.is_public}"


class RoomMaintenance(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=200, null=True, blank=True)
    maintenance_type = models.CharField(
        max_length=20, choices=MaintenanceType.choices, default=MaintenanceType.OTHER
    )

    class Meta:
        db_table = 'room_maintenance'
        managed = True

    def __str__(self):
        return f"Maintenance #{self.id} | Room: {self.room.room_number} | Type: {self.maintenance_type} | {self.start_date} → {self.end_date}"


class BookingLog(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    old_status = models.CharField(max_length=20, choices=BookingStatus.choices, null=True)
    new_status = models.CharField(max_length=20, choices=BookingStatus.choices, null=True)
    changed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'booking_log'
        managed = True

    def __str__(self):
        return f"BookingLog #{self.id} | Booking #{self.booking.id} | {self.old_status} → {self.new_status} | Changed at: {self.changed_at}"

