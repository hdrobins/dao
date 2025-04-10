#BBDD_CONNECTION = "postgresql://{user}:{password}@{host}/{db_name}"  

import cx_Oracle
BBDD_CONNECTION = "oracle+cx_oracle://hca:hca@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=XE)))"