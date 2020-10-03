from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, select, join, MetaData, Table, Column, Integer
from config_vars import BBDD_CONNECTION

Base = declarative_base()


class Headquarters(Base):
    __tablename__ = "headquarters"
    print("entering headquarters config")
    engine = create_engine(BBDD_CONNECTION)
    metadata = MetaData()
    heq = Table("headquarters", metadata, autoload=True, autoload_with=engine, schema='hca')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for headquarters")

    @classmethod
    def headquarters_by_hospital_id(cls, *, hos_id):
        """
        Cuáles son las sedes del hospital hos_id
        """
        query = select([cls.heq]).where(cls.heq.c.hos_id == hos_id)
        return query

    @classmethod
    def single_headquarters(cls, *, heq_id):
        """
        Cuáles son las sedes de la sede heq_id
        """
        query = select([cls.heq]).where(cls.heq.c.heq_id == heq_id)
        return query

    @classmethod
    def all_headquarters(cls):
        """
        Cuáles son las sedes (en caso de no pasar parámetros)
        """
        query = select([cls.heq])
        return query
