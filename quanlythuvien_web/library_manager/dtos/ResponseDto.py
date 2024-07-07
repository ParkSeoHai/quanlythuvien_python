class ResponseDto:
    def __init__(self, status, message, data = None):
        self.status = status
        self.message = message
        self.data = data