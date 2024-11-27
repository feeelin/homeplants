from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:something@localhost:5432/homeplants")
