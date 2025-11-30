from core.repository.base_repository import BaseRepository
from core.models import Operation

class OperationRepository(BaseRepository):
    model = Operation