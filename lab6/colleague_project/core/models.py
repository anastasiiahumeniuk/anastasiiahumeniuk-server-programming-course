from django.db import models

class Agent(models.Model):
    agent_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=45, unique=True)
    email = models.EmailField(max_length=75, unique=True)

    class Meta:
        db_table = 'Agent'

    def __str__(self):
        return f"{self.agent_id} {self.first_name} {self.last_name}"


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'Customer'
        managed = False

    def __str__(self):
        return f"{self.customer_id} {self.first_name} {self.last_name}"


class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    property_type = models.CharField(max_length=45)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    property_status = models.CharField(
        max_length=10,
        choices=[('available', 'Available'), ('sold', 'Sold')],
        default='available'
    )

    class Meta:
        db_table = 'Property'
        managed = False

    def __str__(self):
        return f"{self.property_id} {self.address}, {self.city}"


class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    monthly_price = models.DecimalField(decimal_places=2, max_digits=10)
    rental_property = models.ForeignKey(Property, on_delete=models.PROTECT, related_name='rentals')
    rental_customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='rentals')

    class Meta:
        db_table = 'Rental'
        managed = False

    def __str__(self):
        return f'Rental "{self.rental_property}" for customer "{self.rental_customer}"'


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField()
    appointment_status = models.CharField(max_length=100)
    appointment_customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='appointments')
    appointment_agent = models.ForeignKey(Agent, on_delete=models.PROTECT, related_name='appointments')
    appointment_property = models.ForeignKey(Property, on_delete=models.PROTECT, related_name='appointments')

    class Meta:
        db_table = 'Appointment'
        managed = False

    def __str__(self):
        return f"Appointment for customer {self.appointment_customer} with status {self.appointment_status}"


class Operation(models.Model):
    operation_id = models.AutoField(primary_key=True)
    operation_type = models.CharField(max_length=100)
    operation_date = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    operation_status = models.CharField(
        max_length=10,
        choices=[('pending', 'Pending'), ('agreed', 'Agreed'), ('complete', 'Complete')],
        default='pending',
    )
    operation_customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="operations")
    operation_agent = models.ForeignKey(Agent, on_delete=models.PROTECT, related_name="operations")
    operation_property = models.ForeignKey(Property, on_delete=models.PROTECT, related_name="operations")

    class Meta:
        db_table = 'Operation'
        managed = False

    def __str__(self):
        return f"Operation customer {self.operation_customer} with status {self.operation_status}"


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    payment_date = models.DateField()
    method = models.CharField(max_length=45)
    payment_status = models.CharField(max_length=45)
    payment_operation = models.ForeignKey(Operation, on_delete=models.PROTECT, related_name='payments')

    class Meta:
        db_table = 'Payment'
        managed = False

    def __str__(self):
        return f"Payment {self.amount} $ for operation '{self.payment_operation}'"


class Commission(models.Model):
    commission_id = models.AutoField(primary_key=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    commission_operation = models.ForeignKey(Operation, on_delete=models.PROTECT, related_name='commissions')
    commission_agent = models.ForeignKey(Agent, on_delete=models.PROTECT, related_name='commissions')

    class Meta:
        db_table = 'Commission'
        managed = False

    def __str__(self):
        return f"Commission {self.amount} $ for {self.commission_agent} for operation '{self.commission_operation}'"
