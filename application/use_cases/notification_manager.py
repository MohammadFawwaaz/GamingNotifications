from core.ports.event_handler import EventHandlerPort
from core.domain.events import Event
from core.domain.notification import Notification

class NotificationManager(EventHandlerPort):
    EVENT_CATEGORY_MAP = {
        "LEVEL_UP": "GAME",
        "ITEM_ACQUIRED": "GAME",
        "CHALLENGE_COMPLETED": "GAME",
        "PVP_EVENT": "GAME",
        "FRIEND_REQUEST": "SOCIAL",
        "FRIEND_ACCEPTED": "SOCIAL",
        "NEW_FOLLOWER": "SOCIAL"
    }
    
    MESSAGE_FORMATTERS = {
        "LEVEL_UP": lambda e: f"Congratulations! You've reached level {e.level}!",
        "ITEM_ACQUIRED": lambda e: f"You've acquired the legendary {e.item_name}!",
        "CHALLENGE_COMPLETED": lambda e: f"Challenge completed: {e.challenge_name}!",
        "PVP_EVENT": lambda e: f"You were {e.outcome} by {e.opponent_name}!",
        "FRIEND_REQUEST": lambda e: f"Player '{e.sender_name}' has sent you a friend request.",
        "FRIEND_ACCEPTED": lambda e: f"Player '{e.accepter_name}' accepted your friend request.",
        "NEW_FOLLOWER": lambda e: f"New follower: {e.follower_name} is now following you."
    }
    
    def __init__(self, notification_service, preferences_repo):
        self.notification_service = notification_service
        self.preferences_repo = preferences_repo
    
    def handle(self, event: Event):
        category = self.EVENT_CATEGORY_MAP.get(event.event_type)
        if not category:
            return
        
        prefs = self.preferences_repo.get(event.user_id)
        
        # Check if category exists in preferences, default to True if not found
        if not prefs.preferences.get(category, True):
            return
        
        formatter = self.MESSAGE_FORMATTERS.get(event.event_type)
        if not formatter:
            return
        
        message = formatter(event)
        notification = Notification(
            user_id=event.user_id,
            message=message,
            category=category
        )
        self.notification_service.send(notification)