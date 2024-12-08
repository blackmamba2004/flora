from datetime import date, time

from app.base.schemas import BaseSchema


class CreateVideo(BaseSchema):
    id: str
    address: str
    lat: float
    lon: float
    incident_type: str
    description: str
    incident_date: date | None = None
    incident_time: time | None = None
    video_url: str | None = None


class VideoDTO(BaseSchema):
    id: str
    address: str
    lat: float
    lon: float
    incident_type: str
    description: str
    incident_date: date
    incident_time: time
    video_url: str | None = None
    