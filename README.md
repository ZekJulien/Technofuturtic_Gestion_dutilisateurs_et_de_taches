# [Technofuturtic] Gestion d'utilisateurs et de tâches
    Tutorial project with Technofuturtic for learning SQLALCHEMY with a postgreSQL DB.
# How to use this project ?
## Use a virtual environemment
### Create environemment :
    py -3 -m venv .venv
### Use this environemment (Windows) :
    .\.venv\Scripts\activate
### Install requirements.txt : 
    pip install -r requirements.txt
## Create config.py in app/database/ with this information :
    scheme = "postgresql+psycopg2"
    username = "yours"
    password = "yours"
    hostname = "yours"
    port = "yours"
    database_name = "yours"

    URL_DB = f"{scheme}://{username}:{password}@{hostname}:{port}/{database_name}"

