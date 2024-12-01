from sqlalchemy import text

from queries.base_query_manager import BaseQueryManager
from database import engine


class CrudQueryManagerWithJoin(BaseQueryManager):
    def __init__(self,
                 first_table: str,
                 first_pk: str,
                 second_table: str,
                 second_pk: str,
                 data_class
                 ):
        self.first_table_name = first_table
        self.second_table_name = second_table
        self.first_pk = first_pk
        self.second_pk = second_pk
        self.data_class = data_class

    def get_all_rows(self) -> list:
        query = f"""
        SELECT * FROM {self.first_table_name} 
            JOIN {self.second_table_name} 
            ON {self.first_table_name}.{self.first_pk} = {self.second_table_name}.{self.second_pk};
        """

        with engine.connect() as connection:
            result = connection.execute(text(query))
        return self.transform_result_to_dataclass(result)

    # TODO: Implement if need it
    def get_row_by_id(self, id: int):
        return None

    def update_row(self, row):
        print("Cannot update JOIN row. Use single managers instead.")

    def insert_row(self, row):
        print("Cannot create JOIN row. Use single manager's instead.")

    def delete_row(self, row):
        print("Cannot delete JOIN row. Use single manager's instead.")
