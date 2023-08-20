#BBDD_CONNECTION = "postgresql://admin:ueDrxqVQwtQeBGJ@192.168.88.247/rasa"  


BBDD_CONNECTION = "oracle+cx_oracle://hca:{password}@drobinsundec_medium/?encoding=UTF-8&nencoding=UTF-8"

import cx_Oracle

d="/opt/oracle/instantclient_19_20"
print(d)
cx_Oracle.init_oracle_client(lib_dir=d)

