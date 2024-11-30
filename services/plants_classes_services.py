from services.base_services import BaseServices
from queries.crud_query_manager import CrudQueryManager
from data.plants_class import PlantsClass
from services.plants_services import PlantServices


class PlantsClassesServices(BaseServices):
    query_manager = CrudQueryManager(PlantsClass, "plants_classes")

    @staticmethod
    def is_class_deletable(class_id: int) -> bool:
        plants = PlantServices().get_all()
        this_class_plants = [plant for plant in plants if plant.class_id == class_id]
        return len(this_class_plants) == 0

