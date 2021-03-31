class Notifiable():       

    # tentar tornar privada essa propriedade, para que seja acessível apenas pelo método AddNotification
    _notifications = []   
    
    def AddNotification(self, message):
        self._notifications.append(message)
    