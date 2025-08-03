from infrastructure.adapters.in_app_notification_service import InAppNotificationService
from infrastructure.persistence.in_memory_preferences_repo import InMemoryPreferencesRepository
from application.use_cases.notification_manager import NotificationManager

preferences_repo = InMemoryPreferencesRepository()
notification_service = InAppNotificationService()

def get_notification_manager() -> NotificationManager:
    return NotificationManager(notification_service, preferences_repo)