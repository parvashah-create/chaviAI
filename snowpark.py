import json
import pandas as pd
from snowflake.snowpark.session import Session
from snowflake.snowpark.functions import col
import logging 
logger = logging.getLogger("snowflake.snowpark.session")

class con_snowpark:
    def create_session():
         
        connection_parameters = json.load(open('connection.json'))
        session = Session.builder.configs(connection_parameters).create()
        session.sql_simplifier_enabled = True