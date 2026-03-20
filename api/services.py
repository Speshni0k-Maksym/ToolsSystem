from datetime import datetime
from fastapi import HTTPException
from models.equipment import Equipment
from models.enums import TechnicalState
from models.issue import TechnicalIssueRecord
from models.movement import MovementRecord


class EquipmentService:
    def __init__(self):
        self.equipment_items = {}
        self.movement_history = []
        self.issue_records = []
        self.next_equipment_id = 1
        self.next_movement_id = 1
        self.next_issue_id = 1

    def list_equipment(self, filters=None):
        items = list(self.equipment_items.values())

        if filters is None:
            return items

        filtered_items = items

        if filters.name_query:
            query = filters.name_query.strip().lower()
            filtered_items = [item for item in filtered_items if query in item.name.lower()]

        if filters.room:
            filtered_items = [item for item in filtered_items if item.current_room == filters.room]

        if filters.technical_state:
            filtered_items = [item for item in filtered_items if item.technical_state == filters.technical_state]

        if filters.only_faulty:
            filtered_items = [
                item
                for item in filtered_items
                if item.technical_state in {TechnicalState.NEEDS_SERVICE, TechnicalState.BROKEN}
            ]

        return filtered_items

    def get_equipment(self, equipment_id):
        equipment = self.equipment_items.get(equipment_id)
        if equipment is None:
            raise HTTPException(status_code=404, detail="Equipment not found")
        return equipment

    def create_equipment(self, data):
        equipment = Equipment(
            id=self.next_equipment_id,
            name=data.name,
            equipment_type=data.equipment_type,
            inventory_number=data.inventory_number,
            serial_number=data.serial_number,
            current_room=data.current_room,
        )
        self.equipment_items[equipment.id] = equipment
        self.next_equipment_id += 1
        return equipment

    def update_equipment_state(self, state_change):
        equipment = self.get_equipment(state_change.equipment_id)
        updated_equipment = equipment.copy(
            technical_state=state_change.new_state,
            updated_at=datetime.utcnow(),
        )
        self.equipment_items[equipment.id] = updated_equipment
        return updated_equipment

    def move_equipment(self, move):
        equipment = self.get_equipment(move.equipment_id)
        movement_record = MovementRecord(
            id=self.next_movement_id,
            equipment_id=equipment.id,
            from_room=equipment.current_room,
            to_room=move.to_room,
        )
        updated_equipment = equipment.copy(
            current_room=move.to_room,
            updated_at=datetime.utcnow(),
        )
        self.equipment_items[equipment.id] = updated_equipment
        self.movement_history.append(movement_record)
        self.next_movement_id += 1
        return updated_equipment

    def list_movements(self, equipment_id):
        self.get_equipment(equipment_id)
        return [record for record in self.movement_history if record.equipment_id == equipment_id]

    def add_issue(self, equipment_id, issue):
        self.get_equipment(equipment_id)
        issue_record = TechnicalIssueRecord(
            id=self.next_issue_id,
            equipment_id=equipment_id,
            title=issue.title,
            description=issue.description,
            severity=issue.severity,
        )
        self.issue_records.append(issue_record)
        self.next_issue_id += 1
        return issue_record

    def list_issues(self, equipment_id):
        self.get_equipment(equipment_id)
        return [record for record in self.issue_records if record.equipment_id == equipment_id]


equipment_service = EquipmentService()
