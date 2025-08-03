# Gaming Notifications Service

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

## Interactive API Testing

Test endpoints directly through GitHub Actions:

| Endpoint | Test Button |
|----------|-------------|
| Level Up | [![Test Level Up](https://img.shields.io/badge/Test_Endpoint-Run_Level_Up-blue?logo=github)](https://github.com/MohammadFawwaaz/GamingNotifications/actions/workflows/api-test.yml?query=workflow%3A%22API+Test+Runner%22+level-up) |
| Item Acquired | [![Test Item Acquired](https://img.shields.io/badge/Test_Endpoint-Run_Item_Acquired-blue?logo=github)](https://github.com/MohammadFawwaaz/GamingNotifications/actions/workflows/api-test.yml?query=workflow%3A%22API+Test+Runner%22+item-acquired) |
| Friend Request | [![Test Friend Request](https://img.shields.io/badge/Test_Endpoint-Run_Friend_Request-blue?logo=github)](https://github.com/MohammadFawwaaz/GamingNotifications/actions/workflows/api-test.yml?query=workflow%3A%22API+Test+Runner%22+friend-request) |
| Update Preferences | [![Test Preferences](https://img.shields.io/badge/Test_Endpoint-Run_Update_Preferences-blue?logo=github)](https://github.com/MohammadFawwaaz/GamingNotifications/actions/workflows/api-test.yml?query=workflow%3A%22API+Test+Runner%22+update-preferences) |

### How to Use:
1. Click any "Test Endpoint" button above
2. Click "Run workflow" on the GitHub Actions page
3. Fill in the parameters (or use defaults)
4. Click "Run workflow"
5. View results in the workflow logs

> **Note**: The first run might take longer as it builds the Docker image

## API Testing

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/dd81764f-b24a-44fe-ae87-a4a9719de6d2?action=collection%2Fimport&source=https://raw.githubusercontent.com/MohammadFawwaaz/GamingNotifications/main/postman/Gaming%20Notifications%20API.postman_collection.json)

[Download Postman Collection](https://github.com/MohammadFawwaaz/GamingNotifications/raw/main/postman/Gaming%20Notifications%20API.postman_collection.json)

### Environment Variables
| Variable  | Initial Value       | Current Value       |
|-----------|---------------------|---------------------|
| base_url  | http://localhost:8000 | http://localhost:8000 |

### Testing Instructions
1. Click the "Run in Postman" button above
2. Add a variable `base_url` with value `http://localhost:8000`
3. Start your local service with `docker run -p 8000:8000 gaming-notifications`
4. Execute the requests in Postman
5. Check Docker logs for notification outputs
