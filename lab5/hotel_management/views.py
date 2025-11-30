from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


from .repositories import GuestRepository, RoomRepository, BookingRepository, PaymentRepository, \
    ServiceRepository, FeedbackRepository, ServiceCategoryRepository, RoomTypeRepository, RoomMaintenanceRepository

from .serializers import GuestSerializer, RoomSerializer, BookingSerializer, PaymentSerializer, \
    FeedbackSerializer, ServiceSerializer, ServiceCategorySerializer, RoomTypeSerializer, RoomMaintenanceSerializer


def index(request):
    return HttpResponse("Hotel management API is running.")


class BaseApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    repository_class = None
    serializer_class = None

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            repo = self.repository_class()
            obj = repo.create(**serializer.validated_data)
            return Response(self.serializer_class(obj).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        repo = self.repository_class()

        if pk:
            obj = repo.get_by_id(pk)
            if not obj:
                return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(obj)
        else:
            objs = repo.get_all()
            serializer = self.serializer_class(objs, many=True)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        repo = self.repository_class()
        obj = repo.get_by_id(pk)

        if not obj:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(obj, data=request.data)
        if serializer.is_valid():
            updated = repo.update(pk, **serializer.validated_data)
            return Response(self.serializer_class(updated).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        repo = self.repository_class()

        if repo.delete(pk):
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)


class GuestApiView(BaseApiView):
    repository_class = GuestRepository
    serializer_class = GuestSerializer


class RoomApiView(BaseApiView):
    repository_class = RoomRepository
    serializer_class = RoomSerializer


class BookingApiView(BaseApiView):
    repository_class = BookingRepository
    serializer_class = BookingSerializer


class PaymentApiView(BaseApiView):
    repository_class = PaymentRepository
    serializer_class = PaymentSerializer


class FeedbackApiView(BaseApiView):
    repository_class = FeedbackRepository
    serializer_class = FeedbackSerializer


class ServiceApiView(BaseApiView):
    repository_class = ServiceRepository
    serializer_class = ServiceSerializer


class ServiceCategoryApiView(BaseApiView):
    repository_class = ServiceCategoryRepository
    serializer_class = ServiceCategorySerializer


class RoomTypeApiView(BaseApiView):
    repository_class = RoomTypeRepository
    serializer_class = RoomTypeSerializer


class RoomMaintenanceApiView(BaseApiView):
    repository_class = RoomMaintenanceRepository
    serializer_class = RoomMaintenanceSerializer


class BookingReportApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        repo = BookingRepository()
        report_data = repo.get_aggregated_report()
        return Response(report_data)