from core.ports.notification_service import NotificationServicePort
from core.domain.notification import Notification

class InAppNotificationService(NotificationServicePort):
    def send(self, notification: Notification):
        print(f"[Notification] User {notification.user_id}: {notification.message}")