from abc import ABC, abstractmethod
from core.domain.preferences import UserPreferences

class PreferencesRepositoryPort(ABC):
    @abstractmethod
    def get(self, user_id: int) -> UserPreferences:
        pass
    
    @abstractmethod
    def save(self, preferences: UserPreferences):
        pass