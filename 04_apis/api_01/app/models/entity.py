import uuid
from app.models.notifiable import Notifiable


class Entity(Notifiable):

    def __init__(self, id):
        super(Entity, self).__init__()
        if not id:
            self.__id = uuid.uuid4()
        else:
            self.__id = id

    @property
    def id(self):
        return self.__id
