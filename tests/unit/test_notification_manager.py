import pytest
from application.use_cases.notification_manager import NotificationManager
from core.domain.events import LevelUpEvent, FriendRequestEvent
from core.domain.notification import Notification

class MockNotificationService:
    def __init__(self):
        self.sent_notifications = []
    
    def send(self, notification):
        self.sent_notifications.append(notification)

class MockPreferencesRepository:
    def __init__(self):
        self.preferences = {}
    
    def get(self, user_id):
        return self.preferences.get(user_id, UserPreferences(user_id))

class UserPreferences:
    def __init__(self, user_id):
        self.user_id = user_id
        self.preferences = {"GAME": True, "SOCIAL": True}

@pytest.fixture
def manager():
    service = MockNotificationService()
    repo = MockPreferencesRepository()
    return NotificationManager(service, repo)

def test_handle_level_up_event(manager):
    event = LevelUpEvent(user_id=1, level=15)
    manager.handle(event)
    
    assert len(manager.notification_service.sent_notifications) == 1
    notification = manager.notification_service.sent_notifications[0]
    assert notification.user_id == 1
    assert notification.message == "Congratulations! You've reached level 15!"
    assert notification.category == "GAME"

def test_handle_friend_request_event(manager):
    event = FriendRequestEvent(recipient_id=2, sender_name="PlayerX")
    manager.handle(event)
    
    assert len(manager.notification_service.sent_notifications) == 1
    notification = manager.notification_service.sent_notifications[0]
    assert notification.user_id == 2
    assert notification.message == "Player 'PlayerX' has sent you a friend request."
    assert notification.category == "SOCIAL"

def test_filter_disabled_game_notifications(manager):
    # Setup disabled preferences
    repo = manager.preferences_repo
    prefs = repo.get(1)
    prefs.preferences["GAME"] = False
    repo.preferences[1] = prefs
    
    event = LevelUpEvent(user_id=1, level=15)
    manager.handle(event)
    
    assert len(manager.notification_service.sent_notifications) == 0

def test_filter_disabled_social_notifications(manager):
    # Setup disabled preferences
    repo = manager.preferences_repo
    prefs = repo.get(2)
    prefs.preferences["SOCIAL"] = False
    repo.preferences[2] = prefs
    
    event = FriendRequestEvent(recipient_id=2, sender_name="PlayerX")
    manager.handle(event)
    
    assert len(manager.notification_service.sent_notifications) == 0

def test_handle_unknown_event_type(manager):
    class UnknownEvent:
        event_type = "UNKNOWN_EVENT"
        user_id = 1
    
    manager.handle(UnknownEvent())
    assert len(manager.notification_service.sent_notifications) == 0

def test_missing_formatter(manager):
    # Create custom event type
    class CustomEvent:
        event_type = "CUSTOM_EVENT"
        user_id = 1
    
    # Add to category map but not to formatters
    manager.EVENT_CATEGORY_MAP["CUSTOM_EVENT"] = "GAME"
    
    manager.handle(CustomEvent())
    assert len(manager.notification_service.sent_notifications) == 0

def test_default_preferences(manager):
    # User 99 has no explicit preferences
    event = LevelUpEvent(user_id=99, level=10)
    manager.handle(event)
    
    assert len(manager.notification_service.sent_notifications) == 1
    notification = manager.notification_service.sent_notifications[0]
    assert notification.user_id == 99