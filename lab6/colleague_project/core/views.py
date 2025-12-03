from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Count
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Value
from django.db.models.functions import Concat
from rest_framework.views import APIView
from .models import Agent, Customer, Operation, Appointment, Rental, Property, Payment, Commission
from .serializers import (
    AgentSerializer, CustomerSerializer, OperationSerializer, AppointmentSerializer,
    RentalSerializer, PropertySerializer, PaymentSerializer, CommissionSerializer
)
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Customer


class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='report')
    def report(self, request):
        data = (
            Commission.objects
            .values('commission_agent_id__first_name', 'commission_agent_id__last_name')
            .annotate(
                total_commission = Sum('amount'),
                operation_count = Count('commission_operation_id')
            )
        )
        return Response(list(data))

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='report')
    def report(self, request):
        data = (
            Operation.objects
            .annotate(
                customer_name = Concat(
                    'operation_customer_id__first_name',
                    Value(' '),
                    'operation_customer_id__last_name'
                    )
                )
            .values('customer_name')
            .annotate(
                total_operations=Count('operation_id'),
                total_spent=Sum('price')
            )
        )
        return Response(list(data))

class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.select_related(
        'operation_customer_id', 'operation_agent_id', 'operation_property_id'
    )
    serializer_class = OperationSerializer
    permission_classes = [IsAuthenticated]

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.select_related(
        'appointment_customer_id', 'appointment_agent_id', 'appointment_property_id'
    )
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.select_related(
        'rental_customer_id', 'rental_property_id'
    )
    serializer_class = RentalSerializer
    permission_classes = [IsAuthenticated]

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.select_related('payment_operation_id')
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

class CommissionViewSet(viewsets.ModelViewSet):
    queryset = Commission.objects.select_related('commission_agent_id', 'commission_operation_id')
    serializer_class = CommissionSerializer
    permission_classes = [IsAuthenticated]


class ReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_agents = Agent.objects.count()
        total_customers = Customer.objects.count()
        total_operations = Operation.objects.count()
        total_property = Property.objects.count()
        total_payment = Payment.objects.count()
        total_commission = Commission.objects.count()
        total_rental = Rental.objects.count()
        total_appointment = Appointment.objects.count()

        total_operations_price = Operation.objects.aggregate(total=Sum('price'))['total'] or 0
        total_rental_monthly_price = Rental.objects.aggregate(total=Sum('monthly_price'))['total'] or 0
        total_payment_value = Payment.objects.aggregate(total=Sum('amount'))['total'] or 0

        city_rate = Property.objects.values('city').annotate(
            total_properties = Count('property_id'),
            total_value = Sum('price')
        ).order_by('-total_properties')

        report = {
            'general' :{
                'total_agents': total_agents,
                'total_customers': total_customers,
                'total_operations': total_operations,
                'total_property': total_property,
                'total_payment': total_payment,
                'total_commission': total_commission,
                'total_rental': total_rental,
                'total_appointment': total_appointment,
            },
            'sums' : {
                'total_operations_price' : total_operations_price,
                'total_rental_monthly_price': total_rental_monthly_price,
                'total_payment_price': total_payment_value
            },
            "city_with_most_properties" : list(city_rate)
        }

        return Response(report)