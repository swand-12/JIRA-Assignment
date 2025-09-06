from fastapi import APIRouter, Form, HTTPException
from bson import ObjectId
from config.mongo_config import teams_collection
from utils.helpers import fix_objectid

router = APIRouter()

@router.patch("/teams/change_player_status")
async def change_player_status(
    team_id: str = Form(...),
    new_status: str = Form(...),
    player_id: str = Form(...)
):
    doc = await teams_collection.find_one({"_id": ObjectId(team_id)})
    if not doc:
        raise HTTPException(status_code=404, detail=" Team not found")

    player_found = False
    for player in doc["players"]:
        if player["college_id"] == player_id:
            player["status"] = new_status
            player_found = True
            break

    if not player_found:
        raise HTTPException(status_code=404, detail=" Player not found in team")

    if all(player["status"] == new_status for player in doc["players"]):
        doc["team_status"] = new_status

    await teams_collection.update_one(
        {"_id": ObjectId(team_id)},
        {"$set": {"players": doc["players"], "team_status": doc["team_status"]}}
    )

    return fix_objectid(doc)
