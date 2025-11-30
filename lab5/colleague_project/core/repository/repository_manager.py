from .agent_repository import AgentRepository
from .customer_repository import CustomerRepository
from .operation_repository import OperationRepository
from .commission_repository import CommissionRepository
from .payment_repository import PaymentRepository
from .property_repository import PropertyRepository
from .rental_repository import RentalRepository
from .appointment_repository import AppointmentRepository

class RepositoryManager:
    def __init__(self):
        self.agents = AgentRepository()
        self.customers = CustomerRepository()
        self.operations = OperationRepository()
        self.rentals = RentalRepository()
        self.properties = PropertyRepository()
        self.payments = PaymentRepository()
        self.commissions = CommissionRepository()
        self.appointment = AppointmentRepository()
