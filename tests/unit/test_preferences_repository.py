import pytest
from infrastructure.persistence.in_memory_preferences_repo import InMemoryPreferencesRepository
from core.domain.preferences import UserPreferences

@pytest.fixture
def repo():
    return InMemoryPreferencesRepository()

def test_get_new_user(repo):
    prefs = repo.get(1)
    assert prefs.user_id == 1
    assert prefs.preferences["GAME"] is True
    assert prefs.preferences["SOCIAL"] is True

def test_save_and_retrieve(repo):
    prefs = UserPreferences(1)
    prefs.preferences["SOCIAL"] = False
    repo.save(prefs)
    
    saved_prefs = repo.get(1)
    assert saved_prefs.preferences["SOCIAL"] is False

def test_update_preferences(repo):
    # Initial save
    prefs = UserPreferences(1)
    repo.save(prefs)
    
    # Update
    prefs.preferences["GAME"] = False
    repo.save(prefs)
    
    # Verify
    saved_prefs = repo.get(1)
    assert saved_prefs.preferences["GAME"] is False

def test_multiple_users(repo):
    # User 1
    prefs1 = UserPreferences(1)
    prefs1.preferences["SOCIAL"] = False
    repo.save(prefs1)
    
    # User 2
    prefs2 = UserPreferences(2)
    prefs2.preferences["GAME"] = False
    repo.save(prefs2)
    
    # Verify
    assert repo.get(1).preferences["SOCIAL"] is False
    assert repo.get(2).preferences["GAME"] is False
    assert repo.get(1).preferences["GAME"] is True  # Default