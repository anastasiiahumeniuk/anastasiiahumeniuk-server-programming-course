from core.repository.base_repository import BaseRepository
from core.models import Payment

class PaymentRepository(BaseRepository):
    model = Payment
