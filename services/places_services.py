from services.base_services import BaseServices
from queries.crud_query_manager import CrudQueryManager
from queries.crud_manager_with_two_joins import CrudManagerWithTwoJoins
from data.place import Place
from data.place_with_plant import PlaceWithPlant


class PlacesServices(BaseServices):
    query_manager = CrudQueryManager(Place, "places")
    full_query_manager = CrudManagerWithTwoJoins(
        "places",
        "id",
        "plants",
        "id",
        "plants_info",
        "id",
        "info_id",
        PlaceWithPlant
    )

    def get_all(self):
        return self.full_query_manager.get_all_rows()

    def get_all_single(self):
        return self.query_manager.get_all_rows()

    def get_by_id(self, id):
        return id

    def get_all_for_room(self, room_id):
        all_places = self.get_all()
        if not len(all_places):
            all_places = self.get_all_single()
        return list(filter(lambda room: room.room_id == room_id, all_places))

