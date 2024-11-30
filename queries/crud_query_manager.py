from sqlalchemy import text
from database import engine

from queries.base_query_manager import BaseQueryManager


class CrudQueryManager(BaseQueryManager):
    def __init__(self, data_class, table_name):
        self.data_class = data_class
        self.table_name = table_name

    def get_all_rows(self) -> list:
        query = f"SELECT * FROM {self.table_name};"

        with engine.connect() as connection:
            result = connection.execute(text(query))
        return self.transform_result_to_dataclass(result)

    def update_row(self, row: dict):
        to_build = []
        for key, value in row.items():
            if key != "id":
                to_build.append(f"{key} = '{value}'")
        values = ", ".join(to_build)

        query = f"UPDATE {self.table_name} SET {values} WHERE id = (id);"

        with engine.connect() as connection:
            connection.execute(text(query), {"id": row["id"]})
            connection.commit()

    def get_row_by_id(self, id: int) -> list:
        query = f"SELECT * FROM {self.table_name} WHERE id = :id;"

        with engine.connect() as connection:
            result = connection.execute(text(query), {"id": id})
        return self.transform_result_to_dataclass(result)
