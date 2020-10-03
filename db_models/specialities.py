from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, select, join, MetaData, Table

from .headquarters import Headquarters
from . import doctors
from .healthrelations import HealthRelations
from config_vars import BBDD_CONNECTION

Base = declarative_base()


class Specialities(Base):
    __tablename__ = "specialities"

    print("entering specialities config")
    engine = create_engine(BBDD_CONNECTION)
    metadata = MetaData()
    msp = Table("medical_specialties", metadata, autoload=True, autoload_with=engine, schema='hca')
    id_not_in_db = Column(Integer, primary_key=True)
    print("finished config for specialities")

    @classmethod
    def specialities_by_hospital(cls, *, hos_id):
        """
             Especialidades médicas del hospital hos_id
        """
        query = select([cls.msp]).where(cls.msp.c.hos_id == hos_id)
        return query

    @classmethod
    def specialities_by_headquarter(cls, *, heq_id):
        """
             Especialidades médicas de la sede heq_id
        """
        j = join(
            cls.msp,
            doctors.Doctors.doc,
            cls.msp.c.msp_id == doctors.Doctors.doc.c.msp_id,
        ).join(
            HealthRelations.hre,
            HealthRelations.hre.c.doc_id == doctors.Doctors.doc.c.doc_id,
        )
        query = (
            select([cls.msp])
            .distinct()
            .select_from(j)
            .where(HealthRelations.hre.c.heq_id == heq_id)
        )
        return query

    @classmethod
    def all_specialities(cls):
        """
            Especialidades médicas
        """
        query = select([cls.msp])
        return query

    @classmethod
    def single_speciality(cls, *, msp_id):
        """
            Especialidades médicas de la especialidad msp_id
        """
        query = select([cls.msp]).where(cls.msp.c.msp_id == msp_id)
        return query

    @classmethod
    def single_speciality_of_headquarter(cls, *, heq_id, msp_id):
        """
            Especialidades médicas de la sede heq_id y de la especialidad msp_id
        """
        j = join(
            cls.msp,
            doctors.Doctors.doc,
            cls.msp.c.msp_id == doctors.Doctors.doc.c.msp_id,
        ).join(
            HealthRelations.hre,
            HealthRelations.hre.c.doc_id == doctors.Doctors.doc.c.doc_id,
        )
        query = (
            select([cls.msp])
            .distinct()
            .select_from(j)
            .where(HealthRelations.hre.c.heq_id == heq_id)
            .where(cls.msp.c.msp_id == msp_id)
        )
        return query

    @classmethod
    def single_speciality_of_hospital(cls, *, hos_id, msp_id):
        """
            Especialidades médicas de la sede heq_id y del hospital hos_id
        """
        query = (
            select([cls.msp])
            .where(cls.msp.c.msp_id == msp_id)
            .where(cls.msp.c.hos_id == hos_id)
        )
        return query
