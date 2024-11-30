from services.base_services import BaseServices
from queries.crud_query_manager import CrudQueryManager
from data.room import Room


class RoomServices(BaseServices):
    query_manager = CrudQueryManager(Room, "rooms")
