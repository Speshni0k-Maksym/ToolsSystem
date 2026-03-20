from enum import Enum


class TechnicalState(str, Enum):
    WORKING = "working"
    NEEDS_SERVICE = "needs_service"
    BROKEN = "broken"
    DECOMMISSIONED = "decommissioned"


class IssueSeverity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
