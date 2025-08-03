from abc import ABC, abstractmethod
from core.domain.notification import Notification

class NotificationServicePort(ABC):
    @abstractmethod
    def send(self, notification: Notification):
        pass