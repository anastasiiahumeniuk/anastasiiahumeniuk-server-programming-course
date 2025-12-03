from core.repository.base_repository import BaseRepository
from core.models import Agent

class AgentRepository(BaseRepository):
    model = Agent

    def get_by_name(self, first_name, last_name=None):
        request = self.model.objects.filter(first_name=first_name)
        if last_name:
            request = request.filter(last_name=last_name)
        return request