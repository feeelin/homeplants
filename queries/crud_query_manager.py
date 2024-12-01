from sqlalchemy import text
from werkzeug.datastructures import ImmutableDict

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
        query = f"UPDATE {self.table_name} SET {self.build_values_string(row)} WHERE id = :id;"

        with engine.connect() as connection:
            connection.execute(text(query), {"id": row["id"]})
            connection.commit()

    def get_row_by_id(self, id: int) -> list:
        query = f"SELECT * FROM {self.table_name} WHERE id = :id;"

        with engine.connect() as connection:
            result = connection.execute(text(query), {"id": id})
        return self.transform_result_to_dataclass(result)

    def insert_row(self, row: dict) -> None:
        query = (f"INSERT INTO {self.table_name} ({self.get_values_names_string(row)}) "
                 f"VALUES ({self.build_values_string_without_keys(row)});")
        with engine.connect() as connection:
            connection.execute(text(query), {"id": id})
            connection.commit()

    def delete_row(self, id: int) -> None:
        query = f"DELETE FROM {self.table_name} WHERE id = :id"
        with engine.connect() as connection:
            connection.execute(text(query), {"id": id})
            connection.commit()
