import pytest
from core.domain.events import LevelUpEvent, FriendRequestEvent
from infrastructure.adapters.in_app_notification_service import InAppNotificationService
from infrastructure.persistence.in_memory_preferences_repo import InMemoryPreferencesRepository
from application.use_cases.notification_manager import NotificationManager

@pytest.fixture
def full_system():
    service = InAppNotificationService()
    repo = InMemoryPreferencesRepository()
    manager = NotificationManager(service, repo)
    return service, repo, manager

def test_full_notification_flow(full_system, capsys):
    service, repo, manager = full_system
    
    # Create event
    event = LevelUpEvent(user_id=1, level=15)
    
    # Process event
    manager.handle(event)
    
    # Verify output
    captured = capsys.readouterr()
    assert "Congratulations! You've reached level 15!" in captured.out
    assert "User 1" in captured.out

def test_preference_filtering_flow(full_system, capsys):
    service, repo, manager = full_system
    
    # Disable social notifications for user 2
    prefs = repo.get(2)
    prefs.preferences["SOCIAL"] = False
    repo.save(prefs)
    
    # Create social event
    event = FriendRequestEvent(recipient_id=2, sender_name="PlayerX")
    
    # Process event
    manager.handle(event)
    
    # Verify no output
    captured = capsys.readouterr()
    assert "friend request" not in captured.out

def test_multiple_users_flow(full_system, capsys):
    service, repo, manager = full_system
    
    # User 1: Enable all notifications (default)
    # User 2: Disable game notifications
    prefs2 = repo.get(2)
    prefs2.preferences["GAME"] = False
    repo.save(prefs2)
    
    # Create events
    event1 = LevelUpEvent(user_id=1, level=10)
    event2 = LevelUpEvent(user_id=2, level=10)
    
    # Process events
    manager.handle(event1)
    manager.handle(event2)
    
    # Verify output
    captured = capsys.readouterr()
    assert "User 1" in captured.out
    assert "User 2" not in captured.out

def test_preference_update_flow(full_system, capsys):
    service, repo, manager = full_system
    
    # User 3: Disable notifications
    prefs = repo.get(3)
    prefs.preferences["GAME"] = False
    repo.save(prefs)
    
    # First event - should be blocked
    event1 = LevelUpEvent(user_id=3, level=5)
    manager.handle(event1)
    
    # Update preferences
    prefs.preferences["GAME"] = True
    repo.save(prefs)
    
    # Second event - should go through
    event2 = LevelUpEvent(user_id=3, level=6)
    manager.handle(event2)
    
    # Verify
    captured = capsys.readouterr()
    assert "level 5" not in captured.out
    assert "level 6" in captured.out

def test_complete_event_types_flow(full_system, capsys):
    service, repo, manager = full_system
    
    # Create various events
    events = [
        LevelUpEvent(user_id=1, level=10),
        FriendRequestEvent(recipient_id=1, sender_name="PlayerA"),
        LevelUpEvent(user_id=2, level=20),
        FriendRequestEvent(recipient_id=3, sender_name="PlayerB")
    ]
    
    # Process all events
    for event in events:
        manager.handle(event)
    
    # Verify output
    captured = capsys.readouterr().out
    assert "level 10" in captured
    assert "level 20" in captured
    assert "PlayerA" in captured
    assert "PlayerB" in captured
    assert "User 1" in captured
    assert "User 2" in captured
    assert "User 3" in captured