from datetime import datetime


class MovementRecord:
    def __init__(self, id, equipment_id, from_room, to_room, moved_at=None):
        self.id = id
        self.equipment_id = equipment_id
        self.from_room = from_room
        self.to_room = to_room
        self.moved_at = moved_at or datetime.utcnow()

    def to_dict(self):
        return {
            "id": self.id,
            "equipment_id": self.equipment_id,
            "from_room": self.from_room,
            "to_room": self.to_room,
            "moved_at": self.moved_at,
        }
