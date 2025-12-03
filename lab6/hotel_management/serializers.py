from rest_framework import serializers
from .models import Guest, Room, Booking, Payment, Feedback, Service, ServiceCategory, RoomType, RoomMaintenance, BookingLog

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'passport_series', 'passport_number', 'date_of_birth']

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['id', 'name', 'base_price']

class RoomSerializer(serializers.ModelSerializer):
    room_type = RoomTypeSerializer(read_only=True)
    room_type_id = serializers.PrimaryKeyRelatedField(
        queryset=RoomType.objects.all(), source='room_type', write_only=True
    )

    class Meta:
        model = Room
        fields = ['id', 'room_number', 'room_type', 'room_type_id', 'floor_number', 'capacity', 'price_per_night', 'status']

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ['id', 'name']

class ServiceSerializer(serializers.ModelSerializer):
    service_category = ServiceCategorySerializer(read_only=True)
    service_category_id = serializers.PrimaryKeyRelatedField(
        queryset=ServiceCategory.objects.all(), source='service_category', write_only=True
    )

    class Meta:
        model = Service
        fields = ['id', 'service_name', 'price', 'service_category', 'service_category_id']

class BookingSerializer(serializers.ModelSerializer):
    guest = GuestSerializer(read_only=True)
    guest_id = serializers.PrimaryKeyRelatedField(
        queryset=Guest.objects.all(), source='guest', write_only=True
    )
    room = RoomSerializer(read_only=True)
    room_id = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all(), source='room', write_only=True
    )

    class Meta:
        model = Booking
        fields = [
            'id', 'guest', 'guest_id', 'room', 'room_id',
            'check_in_date', 'check_out_date', 'booking_status'
        ]

class PaymentSerializer(serializers.ModelSerializer):
    booking = BookingSerializer(read_only=True)
    booking_id = serializers.PrimaryKeyRelatedField(
        queryset=Booking.objects.all(), source='booking', write_only=True
    )

    class Meta:
        model = Payment
        fields = ['id', 'booking', 'booking_id', 'payment_date', 'amount', 'payment_method', 'payment_status', 'partial_payment']


class FeedbackSerializer(serializers.ModelSerializer):
    guest = GuestSerializer(read_only=True)
    guest_id = serializers.PrimaryKeyRelatedField(
        queryset=Guest.objects.all(), source='guest', write_only=True
    )
    booking = BookingSerializer(read_only=True)
    booking_id = serializers.PrimaryKeyRelatedField(
        queryset=Booking.objects.all(), source='booking', write_only=True
    )

    class Meta:
        model = Feedback
        fields = ['id', 'guest', 'guest_id', 'booking', 'booking_id', 'rating', 'title', 'comment', 'is_public']

class RoomMaintenanceSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)
    room_id = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all(), source='room', write_only=True
    )

    class Meta:
        model = RoomMaintenance
        fields = ['id', 'room', 'room_id', 'start_date', 'end_date', 'maintenance_type']

class BookingLogSerializer(serializers.ModelSerializer):
    booking = BookingSerializer(read_only=True)
    booking_id = serializers.PrimaryKeyRelatedField(
        queryset=Booking.objects.all(), source='booking', write_only=True
    )

    class Meta:
        model = BookingLog
        fields = ['id', 'booking', 'booking_id', 'old_status', 'new_status', 'changed_at']
