# Gaming Notifications Service

![CI/CD Status](https://github.com/MohammadFawwaaz/gaming-notifications/actions/workflows/ci-cd.yml/badge.svg)

A real-time notification system for online gaming platforms that handles in-game and social events with user preference management.

## Features

- **Real-time notifications** for in-game events:
  - Level ups
  - Item acquisitions
  - Challenge completions
  - PvP events
- **Social notifications**:
  - Friend requests
  - Friend acceptances
  - New followers
- **User preferences** - Enable/disable notification categories
- **Clean architecture** - Separation of concerns with SOLID principles
- **Docker support** - Containerized deployment
- **REST API** - Easy integration with game systems

## API Endpoints

| Endpoint | Method | Description | Request Body Example |
|----------|--------|-------------|----------------------|
| `/notifications/events/level-up` | POST | Trigger level up event | `{"user_id": 123, "level": 15}` |
| `/notifications/events/item-acquired` | POST | Trigger item acquired event | `{"user_id": 456, "item_name": "Sword of Azeroth"}` |
| `/notifications/events/challenge-completed` | POST | Trigger challenge completion | `{"user_id": 789, "challenge_name": "Dragon Slayer"}` |
| `/notifications/events/pvp` | POST | Trigger PvP event | `{"user_id": 101, "outcome": "defeated", "opponent_name": "DarkKnight"}` |
| `/notifications/events/friend-request` | POST | Trigger friend request | `{"sender_name": "PlayerX", "recipient_id": 123}` |
| `/notifications/events/friend-accepted` | POST | Trigger friend acceptance | `{"requester_id": 456, "accepter_name": "PlayerY"}` |
| `/notifications/events/new-follower` | POST | Trigger new follower event | `{"user_id": 789, "follower_name": "PlayerZ"}` |
| `/notifications/preferences` | PUT | Update user preferences | `{"user_id": 123, "category": "SOCIAL", "enabled": false}` |

## Getting Started

### Prerequisites

- Docker
- Python 3.9+

### Installation

1. Clone the repository:
```bash
git clone https://github.com/MohammadFawwaaz/gaming-notifications.git
cd gaming-notifications
```

2. Build the Docker image:
```
docker build -t gaming-notifications .
```

### Running the Service
```
docker run -p 8000:8000 gaming-notifications
```

The service will be available at `http://localhost:8000`

### Running Tests
```
# Build test image
docker build --build-arg INSTALL_TESTS=true -t gaming-notifications-test .

# Run tests
docker run --rm gaming-notifications-test pytest tests/
```

## Usage Examples

### Trigger Level Up Event
```
curl -X POST http://localhost:8000/notifications/events/level-up \
  -H "Content-Type: application/json" \
  -d '{"user_id": 123, "level": 15}'
```

### Update User Preferences
```
curl -X PUT http://localhost:8000/notifications/preferences \
  -H "Content-Type: application/json" \
  -d '{"user_id": 123, "category": "SOCIAL", "enabled": false}'
```
