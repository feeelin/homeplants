from werkzeug.datastructures import ImmutableMultiDict

from services.base_services import BaseServices
from queries.crud_query_manager import CrudQueryManager
from data.plants_class import PlantsClass


class PlantsClassesServices(BaseServices):
    query_manager = CrudQueryManager(PlantsClass, "plants_classes")

    def get_all(self):
        return self.query_manager.get_all_rows()

    def get_by_id(self, id: int):
        return self.query_manager.get_row_by_id(id)

    def update_by_id(self, id: int, payload: ImmutableMultiDict) -> None:
        updated_payload = {"id": id, **payload}
        self.query_manager.update_row(updated_payload)
