from core.repository.base_repository import BaseRepository
from core.models import Property

class PropertyRepository(BaseRepository):
    model = Property

    def get_by_id(self, property_id: int):
        try:
            return self.model.objects.get(property_id=property_id)
        except self.model.DoesNotExist:
            return None