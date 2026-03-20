from pydantic import BaseModel
from models.enums import TechnicalState


class EquipmentFilter(BaseModel):
    name_query: str | None
    room: str | None
    technical_state: TechnicalState | None
    only_faulty: bool = False
