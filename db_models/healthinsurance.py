from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, MetaData, Table, select
from config_vars import BBDD_CONNECTION

Base = declarative_base()


class HealthInsurances(Base):
    __tablename__ = "health_insurances"
    print("entering parameters config")
    engine = create_engine(BBDD_CONNECTION)
    metadata = MetaData()
    ins = Table("health_insurance", metadata, autoload=True, autoload_with=engine, schema='hca')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for parameters")
    
    @classmethod
    def insurances_by_id(cls, *, hos_id):
        """
        Cuáles son las obras sociales
        """
        query = select([cls.ins]).where(cls.ins.c.hos_id == hos_id)
        return query
        
