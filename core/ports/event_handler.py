from abc import ABC, abstractmethod
from core.domain.events import Event

class EventHandlerPort(ABC):
    @abstractmethod
    def handle(self, event: Event):
        pass