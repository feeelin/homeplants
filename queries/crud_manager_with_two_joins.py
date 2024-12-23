from sqlalchemy import text

from database import engine
from queries.base_query_manager import BaseQueryManager


class CrudManagerWithTwoJoins(BaseQueryManager):
    def __init__(self,
                 first_table: str,
                 first_pk: str,
                 second_table: str,
                 second_pk: str,
                 third_table: str,
                 third_pk: str,
                 first_and_second_union: str,
                 second_and_third_union: str,
                 data_class
                 ):
        self.first_table_name = first_table
        self.second_table_name = second_table
        self.third_table_name = third_table
        self.first_pk = first_pk
        self.second_pk = second_pk
        self.first_and_second_union = first_and_second_union
        self.second_and_third_unit = second_and_third_union
        self.third_pk = third_pk
        self.data_class = data_class

    def get_all_rows(self) -> list:
        query = f"""
        SELECT * FROM {self.first_table_name} 
            JOIN {self.second_table_name} 
            ON {self.first_table_name}.{self.first_and_second_union} = {self.second_table_name}.{self.second_pk}
            JOIN {self.third_table_name} 
            ON {self.third_table_name}.{self.third_pk} = {self.second_table_name}.{self.second_and_third_unit}
        """

        with engine.connect() as connection:
            result = connection.execute(text(query))
        return self.transform_result_to_dataclass(result)

    def get_row_by_id(self, id) -> list:
        query = f"""
            SELECT * FROM {self.first_table_name} 
                JOIN {self.second_table_name} 
                ON {self.first_table_name}.{self.first_and_second_union} = {self.second_table_name}.{self.second_pk}
                JOIN {self.third_table_name} 
                ON {self.third_table_name}.{self.third_pk} = {self.second_table_name}.{self.second_and_third_unit}
                WHERE {self.first_table_name}.{self.first_pk} = :id;
            """

        with engine.connect() as connection:
            result = connection.execute(text(query), {"id": id})
        return self.transform_result_to_dataclass(result)[0]

    def update_row(self, row):
        print("Cannot update JOIN row. Use single manager's instead.")

    def insert_row(self, row):
        print("Cannot create JOIN row. Use single manager's instead.")

    def delete_row(self, row):
        print("Cannot delete JOIN row. Use single manager's instead.")
