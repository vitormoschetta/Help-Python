class Notifiable:
    _notifications = []

    def add_notification(self, message):
        self._notifications.append(message)

    def is_valid(self):
        if len(self._notifications) > 0:
            return False
        else:
            return True

    def is_invalid(self):
        return not self.is_valid()
