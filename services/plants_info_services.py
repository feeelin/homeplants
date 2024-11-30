from services.base_services import BaseServices
from queries.crud_query_manager import CrudQueryManager
from data.plants_info import PlantsInfo


class PlantsInfoService(BaseServices):
    query_manager = CrudQueryManager(PlantsInfo, "plants_info")
