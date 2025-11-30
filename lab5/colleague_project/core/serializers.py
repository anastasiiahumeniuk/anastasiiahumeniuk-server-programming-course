from rest_framework import serializers
from .models import Agent, Customer, Operation, Appointment, Rental, Property, Payment, Commission

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['agent_id', 'first_name', 'last_name', 'email']
        read_only_fields = ['agent_id']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_id', 'first_name', 'last_name', 'email']
        read_only_fields = ['customer_id']

class OperationSerializer(serializers.ModelSerializer):
    operation_customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    operation_agent_id = serializers.PrimaryKeyRelatedField(queryset=Agent.objects.all())
    operation_property_id = serializers.PrimaryKeyRelatedField(queryset=Property.objects.all())

    class Meta:
        model = Operation
        fields = ['operation_id', 'operation_type', 'operation_date', 'price',
                  'operation_customer_id', 'operation_agent_id', 'operation_property_id', 'operation_status']
        read_only_fields = ['operation_id']

class AppointmentSerializer(serializers.ModelSerializer):
    appointment_customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    appointment_agent_id = serializers.PrimaryKeyRelatedField(queryset=Agent.objects.all())
    appointment_property_id = serializers.PrimaryKeyRelatedField(queryset=Property.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Appointment
        fields = [
            'appointment_id', 'date_time', 'appointment_status',
            'appointment_customer_id', 'appointment_agent_id', 'appointment_property_id'
        ]
        read_only_fields = ['appointment_id']

class RentalSerializer(serializers.ModelSerializer):
    rental_customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    rental_property_id = serializers.PrimaryKeyRelatedField(queryset=Property.objects.all())

    class Meta:
        model = Rental
        fields = ['rental_id', 'start_date', 'end_date', 'monthly_price', 'rental_customer_id', 'rental_property_id']
        read_only_fields = ['rental_id']

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
        read_only_fields = ['property_id']

class PaymentSerializer(serializers.ModelSerializer):
    payment_operation_id = serializers.PrimaryKeyRelatedField(queryset=Operation.objects.all())

    class Meta:
        model = Payment
        fields = ['payment_id', 'amount', 'payment_date', 'method', 'payment_status', 'payment_operation_id']
        read_only_fields = ['payment_id']

class CommissionSerializer(serializers.ModelSerializer):
    commission_operation_id = serializers.PrimaryKeyRelatedField(queryset=Operation.objects.all())
    commission_agent_id = serializers.PrimaryKeyRelatedField(queryset=Agent.objects.all())

    class Meta:
        model = Commission
        fields = ['commission_id', 'commission_operation_id', 'commission_agent_id', 'amount']
        read_only_fields = ['commission_id']