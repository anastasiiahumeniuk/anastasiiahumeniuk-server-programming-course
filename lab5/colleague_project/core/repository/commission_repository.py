from core.repository.base_repository import BaseRepository
from core.models import Commission

class CommissionRepository(BaseRepository):
    model = Commission