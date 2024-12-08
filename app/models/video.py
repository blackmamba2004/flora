from datetime import date, time
import uuid

from sqlalchemy.orm import Mapped, mapped_column

from app.base.fields import str_unique
from app.database import Base


class Video(Base):
    id: Mapped[str_unique] = mapped_column(primary_key=True, default=str(uuid.uuid4()))
    address: Mapped[str | None] = mapped_column()
    lat: Mapped[float | None] = mapped_column()
    lon: Mapped[float | None] = mapped_column()
    incident_type: Mapped[str | None] = mapped_column()
    description: Mapped[str | None] = mapped_column()
    incident_date: Mapped[date | None] = mapped_column()
    incident_time: Mapped[time | None] = mapped_column()
    video_url: Mapped[str | None] = mapped_column()
