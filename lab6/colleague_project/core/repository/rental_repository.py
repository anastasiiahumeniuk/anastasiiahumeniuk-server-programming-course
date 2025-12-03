from core.repository.base_repository import BaseRepository
from core.models import Rental

class RentalRepository(BaseRepository):
    model = Rental