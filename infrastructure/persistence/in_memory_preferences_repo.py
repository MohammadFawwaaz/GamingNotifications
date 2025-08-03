from core.ports.preferences_repository import PreferencesRepositoryPort
from core.domain.preferences import UserPreferences

class InMemoryPreferencesRepository(PreferencesRepositoryPort):
    def __init__(self):
        self.preferences = {}
    
    def get(self, user_id: int) -> UserPreferences:
        return self.preferences.get(user_id, UserPreferences(user_id))
    
    def save(self, preferences: UserPreferences):
        self.preferences[preferences.user_id] = preferences