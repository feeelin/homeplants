from werkzeug.datastructures import ImmutableDict

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
        "plant_id",
        "info_id",
        PlaceWithPlant
    )

    def get_all(self):
        return self.full_query_manager.get_all_rows()

    def get_all_single(self):
        return self.query_manager.get_all_rows()

    def get_all_for_room(self, room_id):
        all_places = self.get_all()
        all_single_places = self.get_all_single()
        if len(all_places) != len(all_single_places):
            for place in all_single_places:
                is_contains = False
                for full_place in all_places:
                    if full_place.id == place.id:
                        is_contains = True
                if not is_contains:
                    all_places.append(place)
        return list(filter(lambda room: room.room_id == room_id, all_places))

    def update_some_rows(self, rows: dict):
        for row in rows:
            row_unchanged = self.get_by_id(row)
            row_unchanged.plant_id = rows[row] if rows[row] != "NULL" else None
            print({"room_id": row_unchanged.room_id, "plant_id": row_unchanged.plant_id})
            self.update_by_id(row, {"room_id": row_unchanged.room_id, "plant_id": row_unchanged.plant_id})

