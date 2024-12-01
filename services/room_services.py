from werkzeug.datastructures import ImmutableMultiDict

from services.base_services import BaseServices
from services.places_services import PlacesServices
from queries.crud_query_manager import CrudQueryManager
from data.room import Room


class RoomServices(BaseServices):
    query_manager = CrudQueryManager(Room, "rooms")

    def create(self, payload: ImmutableMultiDict):
        super().create(payload)
        created = self.get_all()[-1]
        places_services = PlacesServices()
        for i in range(int(dict(payload)["places_count"])):
            places_services.create(
                {"room_id": created.id, "plant_id": None}
            )
