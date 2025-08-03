from fastapi import APIRouter
from dependencies import preferences_repo
from api.models.requests import PreferenceUpdate

router = APIRouter()

@router.put("/preferences")
async def update_preferences(request: PreferenceUpdate):
    prefs = preferences_repo.get(request.user_id)
    prefs.preferences[request.category] = request.enabled
    preferences_repo.save(prefs)
    return {"status": "preferences updated"}