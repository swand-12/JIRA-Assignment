from fastapi import APIRouter, Form, HTTPException
from bson import ObjectId
from config.mongo_config import teams_collection
from utils.helpers import fix_objectid

router = APIRouter()

@router.patch("/teams/change_team_status")
async def change_team_status(team_id: str = Form(...), new_status: str = Form(...)):
    doc = await teams_collection.find_one({"_id": ObjectId(team_id)})
    if not doc:
        raise HTTPException(status_code=404, detail=" Team not found")

    for player in doc["players"]:
        player["status"] = new_status

    doc["team_status"] = new_status

    await teams_collection.update_one(
        {"_id": ObjectId(team_id)},
        {"$set": {"players": doc["players"], "team_status": doc["team_status"]}}
    )

    return fix_objectid(doc)
