from app.base.dao import BaseDAO
from app.models.video import Video


class VideoDAO(BaseDAO):
    model = Video
