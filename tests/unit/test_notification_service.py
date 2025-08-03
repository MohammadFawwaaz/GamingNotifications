import pytest
from infrastructure.adapters.in_app_notification_service import InAppNotificationService
from core.domain.notification import Notification

def test_in_app_service_send(capsys):
    service = InAppNotificationService()
    notification = Notification(
        user_id=1,
        message="Test notification",
        category="GAME"
    )
    service.send(notification)
    
    captured = capsys.readouterr()
    assert "Test notification" in captured.out
    assert "User 1" in captured.out

def test_multiple_notifications(capsys):
    service = InAppNotificationService()
    
    # First notification
    notif1 = Notification(1, "First message", "GAME")
    service.send(notif1)
    
    # Second notification
    notif2 = Notification(2, "Second message", "SOCIAL")
    service.send(notif2)
    
    captured = capsys.readouterr()
    assert "First message" in captured.out
    assert "Second message" in captured.out
    assert "User 1" in captured.out
    assert "User 2" in captured.out