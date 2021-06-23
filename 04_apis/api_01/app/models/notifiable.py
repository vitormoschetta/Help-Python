class Notifiable:
    def __init__(self):
        self.notifications = []

    def add_notification(self, message):
        self.notifications.append(message)

    @property
    def is_invalid(self) -> bool:
        return any(self.notifications)

    @property
    def is_valid(self):
        return not self.is_invalid


