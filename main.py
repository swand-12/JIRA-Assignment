import os
from dotenv import load_dotenv

# ✅ Load .env before anything else
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import configs AFTER dotenv is loaded
import config.mongo_config
import config.cloudinary_config

# Import routes
from routes.home import router as home_router
from routes.register_team import router as register_team_router
from routes.get_teams import router as get_teams_router
from routes.change_player_status import router as change_player_status_router
from routes.change_team_status import router as change_team_status_router

app = FastAPI()

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(home_router)
app.include_router(register_team_router)
app.include_router(get_teams_router)
app.include_router(change_player_status_router)
app.include_router(change_team_status_router)
