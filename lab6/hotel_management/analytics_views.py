from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
import pandas as pd

from .analytics_repository import AnalyticsRepository

class RevenuePerRoomAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        repo = AnalyticsRepository()
        data = repo.revenue_per_room()
        df = pd.DataFrame(data)
        if not df.empty:
            df['total_revenue'] = df['total_revenue'].astype(float)
        return Response(df.to_dict(orient='records'), status=status.HTTP_200_OK)


class BookingsPerGuestAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        min_b = int(request.query_params.get('min', 2))
        repo = AnalyticsRepository()
        data = repo.bookings_count_per_guest(min_bookings=min_b)
        df = pd.DataFrame(data)
        return Response(df.to_dict(orient='records'))


class PopularServicesAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        top_n = int(request.query_params.get('top', 10))
        repo = AnalyticsRepository()
        data = repo.popular_services(top_n=top_n)
        df = pd.DataFrame(data)
        return Response(df.to_dict(orient='records'))


class AvgStayByRoomTypeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        repo = AnalyticsRepository()
        data = repo.avg_stay_by_room_type()
        df = pd.DataFrame(data)
        return Response(df.to_dict(orient='records'))


class PeakLoadPerDayAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        start = request.query_params.get('start')  # ISO date 'YYYY-MM-DD' optional
        end = request.query_params.get('end')
        repo = AnalyticsRepository()
        data = repo.peak_load_per_day(start_date=start, end_date=end)
        df = pd.DataFrame(data)
        return Response(df.to_dict(orient='records'))


class BookingStatusChangesPerRoomAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        min_changes = int(request.query_params.get('min', 1))
        repo = AnalyticsRepository()
        data = repo.booking_status_changes_per_room(min_changes=min_changes)
        df = pd.DataFrame(data)
        return Response(df.to_dict(orient='records'))