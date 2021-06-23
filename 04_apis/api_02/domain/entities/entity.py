import uuid
from domain.entities.notifiable import Notifiable


class Entity(Notifiable):
    def __init__(self):
        self.id = uuid.uuid4()
