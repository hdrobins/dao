from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, select, join, MetaData, Table
from config_vars import BBDD_CONNECTION

Base = declarative_base()


class HealthRelations(Base):
    __tablename__ = "health relations"

    print("entering healthrelations config")
    engine = create_engine(BBDD_CONNECTION)
    metadata = MetaData()
    hre = Table("health_relations", metadata, autoload=True, autoload_with=engine, schema='hca')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for healthrealations")

    @classmethod
    def all_calendars(cls):
        """
            Cuáles son los calendarios
        """
        query = select([cls.hre])
        return query

    @classmethod
    def calendars_by_headquarters(cls, *, heq_id):
        """
        Cuáles son los calendarios de la sede heq_id
        """
        query = select([cls.hre]).where(cls.hre.c.heq_id == heq_id)
        return query

    @classmethod
    def calendars_by_doctor(cls, *, doc_id):
        """
            Cuáles son los calendarios del doctor doc_id
        """
        query = select([cls.hre]).where(cls.hre.c.doc_id == doc_id)
        return query

    @classmethod
    def calendars_by_doctor_in_headquarters(cls, *, doc_id, heq_id):
        """
            Cuáles son los calendarios de la sede heq_id y del doctor doc_id
        """
        query = (
            select([cls.hre])
            .where(cls.hre.c.heq_id == heq_id)
            .where(cls.hre.c.doc_id == doc_id)
        )
        return query
