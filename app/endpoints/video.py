import os
import uuid
import datetime

from datetime import date, datetime
from pathlib import Path

from fastapi import APIRouter, UploadFile, File, Form, Query, Request

from app.dao.video import VideoDAO
from app.schemas.video import CreateVideo, VideoDTO

router = APIRouter()

BASE_VIDEO_PATH=Path("app/videos")

def get_file_path(incident_date, incident_type) -> Path:
    file_path: Path = BASE_VIDEO_PATH/incident_date/incident_type
    file_path.mkdir(parents=True, exist_ok=True)
    return file_path


@router.post(
    path="/upload-video", 
    response_model=VideoDTO, 
    name="Загрузить видео на сайт",
    tags=["Панель управления / Загрузка"]
)
async def upload_video(
    address: str = Form(...),
    lat: float = Form(...),
    lon: float = Form(...),
    incident_type: str = Form(...),
    description: str = Form(...),
    incident_date: date = Form(...),
    incident_time: str = Form(...),
    file: UploadFile = File(...),
):
    incident_date = incident_date.strftime("%Y-%m-%d")
    incident_time = datetime.strptime(incident_time, "%H:%M").time()

    video_id = uuid.uuid4()

    file_path = get_file_path(incident_date, incident_type)
    file_name = f"{video_id}{os.path.splitext(file.filename)[1]}"
    full_path = file_path / file_name
    
    with open(full_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    obj_in = CreateVideo(
        id=str(video_id),
        address=address,
        lat=lat,
        lon=lon,
        incident_type=incident_type,
        description=description,
        incident_date=incident_date,
        incident_time=incident_time,
        video_url=str(full_path),
    )
    return await VideoDAO.create(obj_in)


@router.get(
    path="/videos",
    response_model=list[VideoDTO],
    name="Получить список видео",
    tags=["Клиентское приложение / Видео"]
)
async def get_videos(
    request: Request,
    video_date: date = Query(...),
    video_type: str = Query(None),
):
    videos = await VideoDAO.find_all_by_filter(
        incident_date=video_date
    ) 
    if video_type is not None:
        videos = await VideoDAO.find_all_by_filter(
            incident_date=video_date, 
            incident_type=video_type
        )

    base_url = str(request.base_url).rstrip("/")
    data = []
    for video in videos:
        video_url_name = Path(video.video_url).name
        video_params = f"{video.incident_date}/{video.incident_type}"
        video.video_url = f"{base_url}/videos/{video_params}/{video_url_name}"
        data.append(video)
    return data