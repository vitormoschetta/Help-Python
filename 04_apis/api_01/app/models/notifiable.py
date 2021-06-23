class Notifiable:
    notifications = []

    def __init__(self):
        self.notifications = []

    def add_notification(self, message):
        self.notifications.append(message)

    def is_valid(self) -> bool:
        return any(self.notifications)

    def is_invalid(self) -> bool:
        return not self.is_valid
