from django.db.models import Sum, Count, Avg, F, ExpressionWrapper, DurationField
from django.utils import timezone
from datetime import timedelta

from .models import Room, Booking, Payment, Guest, Service, RoomType, BookingLog

class AnalyticsRepository:

    def revenue_per_room(self):
        """
        Revenue per room (sum of payment.amount grouped by room)
        SQL equivalent: SELECT room.room_number, SUM(payment.amount) as total
                        FROM payment JOIN booking ON payment.booking_id = booking.id
                                     JOIN room ON booking.room_id = room.id
                        GROUP BY room.room_number
                        ORDER BY total DESC;
        """
        qs = Payment.objects.values(
            'booking__room__id', 'booking__room__room_number'
        ).annotate(
            total_revenue=Sum('amount')
        ).order_by('-total_revenue')

        # normalize keys for output
        return [
            {
                'room_id': row['booking__room__id'],
                'room_number': row['booking__room__room_number'],
                'total_revenue': float(row['total_revenue'] or 0)
            } for row in qs
        ]

    def bookings_count_per_guest(self, min_bookings=2):
        """
        Number of bookings per guest, HAVING count >= min_bookings.
        SQL: SELECT guest.id, guest.first_name, guest.last_name, COUNT(booking.id) as cnt
             FROM booking JOIN guest ON booking.guest_id = guest.id
             GROUP BY guest.id HAVING cnt >= min_bookings
             ORDER BY cnt DESC;
        """
        qs = Booking.objects.values(
            'guest__id', 'guest__first_name', 'guest__last_name'
        ).annotate(
            bookings_count=Count('id')
        ).filter(
            bookings_count__gte=min_bookings
        ).order_by('-bookings_count')

        return [
            {
                'guest_id': r['guest__id'],
                'first_name': r['guest__first_name'],
                'last_name': r['guest__last_name'],
                'bookings_count': r['bookings_count']
            } for r in qs
        ]

    def popular_services(self, top_n=10):
        """
        Count how many times each service was used.
        SQL: SELECT service.id, service.service_name, COUNT(booking_service.booking_id) as uses
             FROM service LEFT JOIN booking_service ON service.id = booking_service.service_id
             GROUP BY service.id ORDER BY uses DESC LIMIT top_n;
        """
        qs = Service.objects.values(
            'id', 'service_name'
        ).annotate(
            uses=Count('booking')  # reverse relation from Service to Booking through M2M
        ).order_by('-uses')[:top_n]

        return [
            {
                'service_id': r['id'],
                'service_name': r['service_name'],
                'uses': r['uses']
            } for r in qs
        ]

    def avg_stay_by_room_type(self):
        result = []
        room_types = RoomType.objects.all()

        for rt in room_types:
            bookings = Booking.objects.filter(room__room_type=rt)
            if bookings.exists():
                # середня різниця днів
                avg_stay = bookings.annotate(
                    stay=ExpressionWrapper(
                        F('check_out_date') - F('check_in_date'),
                        output_field=DurationField()
                    )
                ).aggregate(avg=Avg('stay'))['avg']
                avg_days = avg_stay.days if avg_stay else 0
            else:
                avg_days = 0

            result.append({
                'room_type_id': rt.id,
                'room_type_name': rt.name,
                'average_stay_days': avg_days
            })
        return result

    def peak_load_per_day(self, start_date=None, end_date=None):
        """
        Peak load (number of simultaneous bookings) per day.
        This is hard to do purely in ORM; we fetch bookings and expand date ranges in Python,
        then count per date. The result is a list of {'date': date, 'occupied_count': n}
        """
        qs = Booking.objects.all().select_related('room')

        if start_date:
            qs = qs.filter(check_out_date__gte=start_date)
        if end_date:
            qs = qs.filter(check_in_date__lte=end_date)

        # build date counts
        counts = {}
        for b in qs:
            current = b.check_in_date
            while current <= b.check_out_date:
                counts[current] = counts.get(current, 0) + 1
                current += timedelta(days=1)

        # convert to sorted list
        items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))  # by count desc then date
        return [{'date': d.isoformat(), 'occupied_count': c} for d, c in items]

    def booking_status_changes_per_room(self, min_changes=1):
        """
        Count BookingLog entries (status changes) per room.
        SQL: SELECT room.room_number, COUNT(bookinglog.id) FROM bookinglog
             JOIN booking ON bookinglog.booking_id = booking.id
             JOIN room ON booking.room_id = room.id
             GROUP BY room.room_number HAVING COUNT(...) >= min_changes
        """
        qs = BookingLog.objects.values(
            'booking__room__id', 'booking__room__room_number'
        ).annotate(
            changes=Count('id')
        ).filter(
            changes__gte=min_changes
        ).order_by('-changes')

        return [
            {
                'room_id': r['booking__room__id'],
                'room_number': r['booking__room__room_number'],
                'changes': r['changes']
            } for r in qs
        ]
