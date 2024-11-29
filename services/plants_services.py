from services.base_services import BaseServices
from queries.crud_manager_with_two_joins import CrudManagerWithTwoJoins
from data.plants_with_info import PlantWithInfo


class PlantServices(BaseServices):
    query_manager = CrudManagerWithTwoJoins("plants",
                                            "id",
                                            "plants_info",
                                            "id",
                                            "plants_classes",
                                            "id",
                                            "class_id",
                                            PlantWithInfo)

    def get_all(self) -> list[PlantWithInfo]:
        return self.query_manager.get_all_rows()

    # TODO: Implement later
    def get_by_id(self, id):
        return None
