from services.base_services import BaseServices
from queries.crud_manager_with_two_joins import CrudManagerWithTwoJoins
from queries.crud_query_manager import CrudQueryManager
from data.plants_with_info import PlantWithInfo
from data.plant import Plant


class PlantServices(BaseServices):
    full_query_manager = CrudManagerWithTwoJoins("plants",
                                                 "id",
                                                 "plants_info",
                                                 "id",
                                                 "plants_classes",
                                                 "id",
                                                 "class_id",
                                                 PlantWithInfo)
    query_manager = CrudQueryManager(Plant, "plants")

    def get_all(self) -> list[PlantWithInfo]:
        return self.full_query_manager.get_all_rows()

    def get_by_id(self, id):
        return self.full_query_manager.get_row_by_id(id)
