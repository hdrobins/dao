# Universidad Nacional de Chilecito

## Equipo de Trabajo
Jonatan Alvarez jonatan.alvarez@kunan.com.ar

Daniel Robins daniel.robins@kunan.com.ar

# dao
Data Access Objects for health care

#### Before you begin, you’ll need:
* IDE or Text editor 
* Python 3.6 or 3.7
* pip install --upgrade pip

#### Create database schema
* [dbscripts](dbscripts.sql)

#### Create the virtual environment
* python3 -m venv ./venv

#### Activate the virtual environment
* source ./venv/bin/activate

#### Install jupyter
* pip install notebook 

#### Install Libs
* pip install sqlalchemy==1.4

#### For Oracle Databases
* pip install cx_Oracle==8.3

#### For Oracle Databases Autonomous (instant client)
https://docs.oracle.com/en-us/iaas/autonomous-database-serverless/doc/connecting-python-tls.html
https://csiandal.medium.com/install-oracle-instant-client-on-ubuntu-4ffc8fdfda08

* pip install oracledb

#### For PostgreSQL
* [Install PostgreSQL Libs](https://springmerchant.com/bigcommerce/psycopg2-virtualenv-install-pg_config-executable-not-found/)
* sudo apt-get install libpq-dev python-dev
* sudo apt-get update
* pip install psycopg2


