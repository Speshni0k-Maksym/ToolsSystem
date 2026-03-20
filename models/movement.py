from datetime import datetime
from pydantic import BaseModel, Field


class MovementRecord(BaseModel):
    id: int
    equipment_id: int
    from_room: str
    to_room: str
    moved_at: datetime = Field(default_factory=datetime.utcnow)
