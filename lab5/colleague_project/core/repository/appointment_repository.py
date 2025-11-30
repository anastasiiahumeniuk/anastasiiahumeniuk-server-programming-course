from core.repository.base_repository import BaseRepository
from core.models import Appointment

class AppointmentRepository(BaseRepository):
    model = Appointment