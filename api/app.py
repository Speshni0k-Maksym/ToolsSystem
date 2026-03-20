from fastapi import FastAPI
from api.services import equipment_service
from models.equipment import EquipmentCreate, EquipmentMove, EquipmentStateChange
from models.filters import EquipmentFilter
from models.issue import TechnicalIssueCreate

general_api = FastAPI()


@general_api.get("/")
def root():
    return {"message": "Equipment Management API is running"}


@general_api.get("/equipment")
def list_equipment(
    name_query=None,
    room=None,
    technical_state=None,
    only_faulty=False,
):
    filters = EquipmentFilter(name_query=name_query, room=room, technical_state=technical_state, only_faulty=only_faulty)
    return [item.to_dict() for item in equipment_service.list_equipment(filters)]


@general_api.get("/equipment/{equipment_id}")
def get_equipment(equipment_id):
    return equipment_service.get_equipment(equipment_id).to_dict()


@general_api.post("/equipment", status_code=201)
def create_equipment(equipment: EquipmentCreate):
    return equipment_service.create_equipment(equipment).to_dict()


@general_api.patch("/equipment/state")
def update_equipment_state(state_change: EquipmentStateChange):
    return equipment_service.update_equipment_state(state_change).to_dict()


@general_api.post("/equipment/move")
def move_equipment(move: EquipmentMove):
    return equipment_service.move_equipment(move).to_dict()


@general_api.get("/equipment/{equipment_id}/movements")
def list_equipment_movements(equipment_id):
    return [m.to_dict() for m in equipment_service.list_movements(equipment_id)]


@general_api.get("/equipment/{equipment_id}/issues")
def list_equipment_issues(equipment_id):
    return [i.to_dict() for i in equipment_service.list_issues(equipment_id)]


@general_api.post("/equipment/{equipment_id}/issues", status_code=201)
def add_equipment_issue(equipment_id, issue: TechnicalIssueCreate):
    return equipment_service.add_issue(equipment_id, issue).to_dict()
