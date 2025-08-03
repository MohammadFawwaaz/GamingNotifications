from fastapi import APIRouter, Depends
from core.domain.events import (
    LevelUpEvent, ItemAcquiredEvent, ChallengeCompletedEvent, PvPEvent,
    FriendRequestEvent, FriendAcceptedEvent, NewFollowerEvent
)
from application.use_cases.notification_manager import NotificationManager
from api.models.requests import (
    LevelUpRequest, ItemAcquiredRequest, ChallengeCompletedRequest, PvPRequest,
    FriendRequest, FriendAcceptedRequest, NewFollowerRequest
)
from dependencies import get_notification_manager

router = APIRouter()

@router.post("/events/level-up")
async def level_up_event(
    request: LevelUpRequest, 
    manager: NotificationManager = Depends(get_notification_manager)
):
    event = LevelUpEvent(
        user_id=request.user_id,
        level=request.level
    )
    manager.handle(event)
    return {"status": "processed"}

@router.post("/events/item-acquired")
async def item_acquired_event(
    request: ItemAcquiredRequest, 
    manager: NotificationManager = Depends(get_notification_manager)
):
    event = ItemAcquiredEvent(
        user_id=request.user_id,
        item_name=request.item_name
    )
    manager.handle(event)
    return {"status": "processed"}

@router.post("/events/challenge-completed")
async def challenge_completed_event(
    request: ChallengeCompletedRequest, 
    manager: NotificationManager = Depends(get_notification_manager)
):
    event = ChallengeCompletedEvent(
        user_id=request.user_id,
        challenge_name=request.challenge_name
    )
    manager.handle(event)
    return {"status": "processed"}

@router.post("/events/pvp")
async def pvp_event(
    request: PvPRequest, 
    manager: NotificationManager = Depends(get_notification_manager)
):
    event = PvPEvent(
        user_id=request.user_id,
        outcome=request.outcome,
        opponent_name=request.opponent_name
    )
    manager.handle(event)
    return {"status": "processed"}

@router.post("/events/friend-request")
async def friend_request_event(
    request: FriendRequest, 
    manager: NotificationManager = Depends(get_notification_manager)
):
    event = FriendRequestEvent(
        recipient_id=request.recipient_id,
        sender_name=request.sender_name
    )
    manager.handle(event)
    return {"status": "processed"}

@router.post("/events/friend-accepted")
async def friend_accepted_event(
    request: FriendAcceptedRequest, 
    manager: NotificationManager = Depends(get_notification_manager)
):
    event = FriendAcceptedEvent(
        requester_id=request.requester_id,
        accepter_name=request.accepter_name
    )
    manager.handle(event)
    return {"status": "processed"}

@router.post("/events/new-follower")
async def new_follower_event(
    request: NewFollowerRequest, 
    manager: NotificationManager = Depends(get_notification_manager)
):
    event = NewFollowerEvent(
        user_id=request.user_id,
        follower_name=request.follower_name
    )
    manager.handle(event)
    return {"status": "processed"}