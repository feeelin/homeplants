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
            result_translated = []
            for row in result:
                result_translated.append(self.data_class(*row))
        return result_translated

