from werkzeug.datastructures import ImmutableMultiDict

from services.base_services import BaseServices
from queries.crud_query_manager import CrudQueryManager
from data.plants_info import PlantsInfo


class PlantsInfoService(BaseServices):
    query_manager = CrudQueryManager(PlantsInfo, "plants_info")

    def get_all(self) -> list[PlantsInfo]:
        return self.query_manager.get_all_rows()

    def get_by_id(self, id):
        return self.query_manager.get_row_by_id(id)

    def update_by_id(self, id: int, payload: ImmutableMultiDict) -> None:
        self.query_manager.update_row({"id": id, **payload})
