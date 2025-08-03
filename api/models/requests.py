from pydantic import BaseModel

class LevelUpRequest(BaseModel):
    user_id: int
    level: int

class ItemAcquiredRequest(BaseModel):
    user_id: int
    item_name: str

class ChallengeCompletedRequest(BaseModel):
    user_id: int
    challenge_name: str

class PvPRequest(BaseModel):
    user_id: int
    outcome: str
    opponent_name: str

class FriendRequest(BaseModel):
    sender_name: str
    recipient_id: int

class FriendAcceptedRequest(BaseModel):
    requester_id: int
    accepter_name: str

class NewFollowerRequest(BaseModel):
    user_id: int
    follower_name: str

class PreferenceUpdate(BaseModel):
    user_id: int
    category: str
    enabled: bool