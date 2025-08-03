class Notification:
    def __init__(self, user_id: int, message: str, category: str):
        self.user_id = user_id
        self.message = message
        self.category = category