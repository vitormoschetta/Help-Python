class GenericResponse:
    def __init__(self, success, message):
        self.success: bool = success
        self.message: str = message
