from datetime import datetime
from models.enums import IssueSeverity


class TechnicalIssueRecord:
    def __init__(self, id, equipment_id, title, description, severity=None, is_resolved=False, created_at=None, resolved_at=None):
        self.id = id
        self.equipment_id = equipment_id
        self.title = title
        self.description = description
        self.severity = severity or IssueSeverity.MEDIUM
        self.is_resolved = is_resolved
        self.created_at = created_at or datetime.utcnow()
        self.resolved_at = resolved_at

    def to_dict(self):
        return {
            "id": self.id,
            "equipment_id": self.equipment_id,
            "title": self.title,
            "description": self.description,
            "severity": self.severity.value,
            "is_resolved": self.is_resolved,
            "created_at": self.created_at,
            "resolved_at": self.resolved_at if self.resolved_at else None,
        }


class TechnicalIssueCreate:
    def __init__(self, title, description, severity=None):
        self.title = title
        self.description = description
        self.severity = severity or IssueSeverity.MEDIUM
