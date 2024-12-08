from app.models.video import Video
from app.schemas.video import VideoDTO
from app.serializers.universal import transform


async def serialize_video(video: Video) -> VideoDTO:
    return transform(
        video,
        VideoDTO
    )