#This code is just for creating the green_growth table (Name: Enviro_devel), NOT inputting data into it.

#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import DateTime, Boolean
from sqlalchemy import exists
from sqlalchemy import sql, select, join, desc
from sqlalchemy import inspect

# Create a sqlite database 
engine = create_engine('sqlite:///./green_growth.sqlite')

metadata=MetaData(engine)

# Try to load Environmental development info from database, if not there, create it.
try:
	Enviro_Devel=Table('Enviro_devel', metadata, autoload=True)
except:
	Enviro_Devel=Table('Enviro_devel', metadata
		Column('Country_by_Year', String, primary_key=True),
		Column('Country', String),
		Column('GDP', Float(Numeric)),
		Column('GDP_CO2emmissions', Float(Numeric)),
		Column('Enviro_taxes', Float(Numeric)),
		Column('Enviro_R&D', Float(Numeric)),
		Column('Renew_energy', Float(Numeric)),
		Column('Devel_enviro_tech', Float(Numeric)),
		Column('Tot_Enviro_ODA', Float(Numeric)),
		Column('Climate_mit_ODA', Float(Numeric)),
		Column('Biodiv_ODA', Float(Numeric)),
		)

metadata.create_all(engine)

inspector =inspect(engine)
print(inspector.get_table_names())
