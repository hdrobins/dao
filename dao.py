#from sqlalchemy import create_engine, select, join, MetaData, Table
import sys
import os
dirname = os.path.dirname(__file__)
 
sys.path.append(dirname)
sys.path.append(dirname+"/db_models/")
from sqlalchemy import create_engine, select, join, MetaData, Table


from db_models.headquarters import Headquarters
from db_models.specialities import Specialities
from db_models.healthrelations import HealthRelations
from db_models.doctors import Doctors
from db_models.hospital import ParametersHospital
from db_models.healthinsurance import HealthInsurances
from config_vars import BBDD_CONNECTION


class HospitalDAO:
    print("starting")
    engine = create_engine(BBDD_CONNECTION)
    connection = engine.connect()
    print("finished connection")
    metadata = MetaData()

    def get_parameters(self,*, hos_id=None):
        if hos_id is not None:
            query = ParametersHospital.parameters_by_id(hos_id=hos_id)
            return self.connection.execute(query).fetchone()

    def get_health_insurance(self,*, hos_id=None):
        if hos_id is not None:
            query = HealthInsurances.insurances_by_id(hos_id=hos_id)
            return self.connection.execute(query).fetchall()

    def get_headquarters(self, *, hos_id=None, heq_id=None):
        if heq_id:
            query = Headquarters.single_headquarters(heq_id=heq_id)
        elif hos_id:
            query = Headquarters.headquarters_by_hospital_id(hos_id=hos_id)
        else:
            query = Headquarters.all_headquarters()
        return self.connection.execute(query).fetchall()

    def get_medical_specialities(self, *, hos_id=None, heq_id=None, msp_id=None):
        if hos_id is None and heq_id is None and msp_id is None:
            query = Specialities.all_specialities()

        elif msp_id and heq_id:
            query = Specialities.single_speciality_of_headquarter(
                msp_id=msp_id, heq_id=heq_id
            )

        elif msp_id and hos_id:
            query = Specialities.single_speciality_of_hospital(
                msp_id=msp_id, hos_id=hos_id
            )

        elif msp_id:
            query = Specialities.single_speciality(msp_id=msp_id)

        elif heq_id:
            query = Specialities.specialities_by_headquarter(heq_id=heq_id)

        elif hos_id:
            query = Specialities.specialities_by_hospital(hos_id=hos_id)

        return self.connection.execute(query).fetchall()

    def get_doctors(self, *, hos_id=None, heq_id=None, msp_id=None, doc_id=None):

        single_mode = doc_id is not None

        if single_mode and not hos_id and not heq_id and not msp_id:
            query = Doctors.single_doctor(doc_id=doc_id)
        elif msp_id:
            if heq_id:
                query = Doctors.doctors_by_speciality_in_headquarters(
                    heq_id=heq_id, single_mode=single_mode, doc_id=doc_id, msp_id=msp_id
                )
            elif hos_id:
                query = Doctors.doctors_by_speciality_in_hospital(
                    hos_id=hos_id, single_mode=single_mode, doc_id=doc_id, msp_id=msp_id
                )
            else:
                query = Doctors.doctors_by_speciality(
                    single_mode=single_mode, msp_id=msp_id, doc_id=doc_id
                )
        elif heq_id:
            query = Doctors.doctors_by_headquarters(
                heq_id=heq_id, single_mode=single_mode, doc_id=doc_id
            )
        elif hos_id:
            query = Doctors.doctors_by_hospital(
                hos_id=hos_id, single_mode=single_mode, doc_id=doc_id
            )
        elif hos_id is None and heq_id is None and msp_id is None and doc_id is None:
            query = Doctors.all_doctors()
        return self.connection.execute(query).fetchall()

    def get_calendar_id(self, *, heq_id=None, doc_id=None):
        if doc_id and heq_id:
            query = HealthRelations.calendars_by_doctor_in_headquarters(
                doc_id=doc_id, heq_id=heq_id
            )
        elif heq_id and not doc_id:
            query = HealthRelations.calendars_by_headquarters(heq_id=heq_id)
        elif doc_id and not heq_id:
            query = HealthRelations.calendars_by_doctor(doc_id=doc_id)
        else:
            query = HealthRelations.all_calendars()
        return self.connection.execute(query).fetchall()
