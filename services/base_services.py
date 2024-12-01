from abc import ABC
from werkzeug.datastructures import ImmutableMultiDict

from queries.base_query_manager import BaseQueryManager


class BaseServices(ABC):
    query_manager: BaseQueryManager

    def get_all(self):
        return self.query_manager.get_all_rows()

    def get_by_id(self, id: int):
        result = self.query_manager.get_row_by_id(id)
        return result[0] if len(result) else None

    def update_by_id(self, id: int, payload: ImmutableMultiDict) -> None:
        updated_payload = {"id": id, **payload}
        self.query_manager.update_row(updated_payload)

    def create(self, payload: ImmutableMultiDict):
        self.query_manager.insert_row(dict(payload))

    def delete(self, id: int) -> None:
        self.query_manager.delete_row(id)
