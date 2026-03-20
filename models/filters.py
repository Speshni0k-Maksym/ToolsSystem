from models.enums import TechnicalState


class EquipmentFilter:
    def __init__(self, name_query=None, room=None, technical_state=None, only_faulty=False):
        self.name_query = name_query
        self.room = room
        self.technical_state = technical_state
        self.only_faulty = only_faulty
