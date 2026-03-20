from datetime import datetime
from pydantic import BaseModel, Field
from models.enums import TechnicalState


class Equipment(BaseModel):
    id: int
    name: str
    equipment_type: str
    inventory_number: str
    serial_number: str | None
    current_room: str
    technical_state: TechnicalState = TechnicalState.WORKING
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class EquipmentCreate(BaseModel):
    name: str
    equipment_type: str
    inventory_number: str
    serial_number: str | None
    current_room: str


class EquipmentStateChange(BaseModel):
    equipment_id: int
    new_state: TechnicalState


class EquipmentMove(BaseModel):
    equipment_id: int
    to_room: str
