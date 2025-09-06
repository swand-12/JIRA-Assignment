from fastapi import APIRouter, Form, File, UploadFile, HTTPException
from typing import List
import cloudinary.uploader
from config.mongo_config import teams_collection

router = APIRouter()

@router.post("/register_team/")
async def register_team(
    college_name: str = Form(...),
    team_leader: str = Form(...),
    sport: str = Form(...),
    gender: str = Form(...),
    coach_name: str = Form(...),
    coach_contact: str = Form(...),
    player_names: List[str] = Form(...),
    college_ids: List[str] = Form(...),
    phones: List[str] = Form(...),
    emails: List[str] = Form(...),
    id_photos: List[UploadFile] = File(...)
):
    required_count = None
    if sport == "Lawn Tennis" and gender == "M": required_count = 5
    elif sport == "Lawn Tennis" and gender == "F": required_count = 4
    elif sport == "Hand ball": required_count = 12
    elif sport == "Yoga": required_count = 6

    if required_count is None:
        raise HTTPException(status_code=400, detail="❌ Invalid sport or gender selection")

    if len(player_names) != required_count:
        raise HTTPException(
            status_code=400,
            detail=f"❌ {sport} ({gender}) requires {required_count} players, got {len(player_names)}"
        )

    uploaded_urls = []
    for photo in id_photos:
        upload_result = cloudinary.uploader.upload(photo.file, folder="sports_teams")
        uploaded_urls.append(upload_result["secure_url"])

    team_doc = {
        "college_name": college_name,
        "team_leader_id": team_leader,
        "sport": sport,
        "gender": gender,
        "coach_name": coach_name,
        "coach_contact": coach_contact,
        "team_status":"Registered",
        "players": [
            {
                "name": n,
                "college_id": c,
                "phone": p,
                "email": e,
                "id_photo_url": url,
                "status":"Registered"
            }
            for n, c, p, e, url in zip(player_names, college_ids, phones, emails, uploaded_urls)
        ],
    }

    result = await teams_collection.insert_one(team_doc)

    return {"message": "✅ Team registered successfully", "id": str(result.inserted_id)}
