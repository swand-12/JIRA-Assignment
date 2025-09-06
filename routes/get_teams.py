from fastapi import APIRouter
from config.mongo_config import teams_collection
from utils.helpers import fix_objectid

router = APIRouter()

@router.get("/teams/")
async def get_teams():
    cursor = teams_collection.find({})
    teams = []
    async for doc in cursor:
        teams.append(fix_objectid(doc))
    return teams
