class Event:
    def __init__(self, event_type: str, user_id: int):
        self.event_type = event_type
        self.user_id = user_id

class LevelUpEvent(Event):
    def __init__(self, user_id: int, level: int):
        super().__init__("LEVEL_UP", user_id)
        self.level = level

class ItemAcquiredEvent(Event):
    def __init__(self, user_id: int, item_name: str):
        super().__init__("ITEM_ACQUIRED", user_id)
        self.item_name = item_name

class ChallengeCompletedEvent(Event):
    def __init__(self, user_id: int, challenge_name: str):
        super().__init__("CHALLENGE_COMPLETED", user_id)
        self.challenge_name = challenge_name

class PvPEvent(Event):
    def __init__(self, user_id: int, outcome: str, opponent_name: str):
        super().__init__("PVP_EVENT", user_id)
        self.outcome = outcome
        self.opponent_name = opponent_name

class FriendRequestEvent(Event):
    def __init__(self, recipient_id: int, sender_name: str):
        super().__init__("FRIEND_REQUEST", recipient_id)
        self.sender_name = sender_name

class FriendAcceptedEvent(Event):
    def __init__(self, requester_id: int, accepter_name: str):
        super().__init__("FRIEND_ACCEPTED", requester_id)
        self.accepter_name = accepter_name

class NewFollowerEvent(Event):
    def __init__(self, user_id: int, follower_name: str):
        super().__init__("NEW_FOLLOWER", user_id)
        self.follower_name = follower_name