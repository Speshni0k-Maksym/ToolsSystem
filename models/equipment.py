from datetime import datetime
from models.enums import TechnicalState


class Equipment:
    def __init__(self, id, name, equipment_type, inventory_number, serial_number, current_room, technical_state=None, created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.equipment_type = equipment_type
        self.inventory_number = inventory_number
        self.serial_number = serial_number
        self.current_room = current_room
        self.technical_state = technical_state or TechnicalState.WORKING
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "equipment_type": self.equipment_type,
            "inventory_number": self.inventory_number,
            "serial_number": self.serial_number,
            "current_room": self.current_room,
            "technical_state": self.technical_state.value,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    def copy(self, **updates):
        data = {
            "id": self.id,
            "name": self.name,
            "equipment_type": self.equipment_type,
            "inventory_number": self.inventory_number,
            "serial_number": self.serial_number,
            "current_room": self.current_room,
            "technical_state": self.technical_state,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
        data.update(updates)
        return Equipment(**data)


class EquipmentCreate:
    def __init__(self, name, equipment_type, inventory_number, serial_number, current_room):
        self.name = name
        self.equipment_type = equipment_type
        self.inventory_number = inventory_number
        self.serial_number = serial_number
        self.current_room = current_room


class EquipmentStateChange:
    def __init__(self, equipment_id, new_state):
        self.equipment_id = equipment_id
        self.new_state = new_state


class EquipmentMove:
    def __init__(self, equipment_id, to_room):
        self.equipment_id = equipment_id
        self.to_room = to_room
