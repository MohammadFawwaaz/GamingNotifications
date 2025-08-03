from fastapi import FastAPI
from api.controllers.notification_controller import router as notification_router
from api.controllers.preference_controller import router as preference_router

app = FastAPI()
app.include_router(notification_router, prefix="/notifications")
app.include_router(preference_router, prefix="/notifications")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)