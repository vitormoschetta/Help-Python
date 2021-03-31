import uuid
from notifiable import Notifiable

class  Product(Notifiable):
    def __init__(self, name, price):
        self.id = uuid.uuid4()
        self.name = name
        self.price = price  
        self.Validate()
    
    def Update(self, name, price):
        self.name = name
        self.price = price  

    def Validate(self):
        if not self.name:
            self.AddNotification('Nome do Produto é obrigatório!')
        if self.price <= 0:
            self.AddNotification('Preço do Produto informado é inválido.')
    