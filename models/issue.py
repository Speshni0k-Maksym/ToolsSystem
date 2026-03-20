from datetime import datetime
from pydantic import BaseModel, Field
from models.enums import IssueSeverity


class TechnicalIssueRecord(BaseModel):
    id: int
    equipment_id: int
    title: str
    description: str
    severity: IssueSeverity = IssueSeverity.MEDIUM
    is_resolved: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    resolved_at: datetime | None


class TechnicalIssueCreate(BaseModel):
    title: str
    description: str
    severity: IssueSeverity = IssueSeverity.MEDIUM
