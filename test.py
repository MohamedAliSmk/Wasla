import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData,inspect
from sqlalchemy.orm import sessionmaker

# Define database connection parameters
db_url = 'sqlite:///db.sqlite3'

# Create SQLAlchemy engine and session objects
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()

# Define metadata and table object
metadata = MetaData()

#print table names
#inspector = inspect(engine)
#print(inspector.get_table_names())


metadata.reflect(bind=engine, schema='db.sqlite3', views=False, only=None, extend_existing=True)# Define column name mapping dictionary
column_mapping = {
    'merchant_id': 'Merchant ID',
    'merchant_name': 'Merchant Name',
    'NameOfAccount_Manager':'Account Manager Name',
    'VPC_value': 'VPC Value',
    'UIGmigs': 'UIGmigs',
    'Billing': 'Billing',
    'CF_value': 'CF Value',
    'Salfny': 'Salfny',
    'Lending': 'Lending',
    'TrxLastMonth': 'Last Month Transactions',
    'TrxCurrentMonth': 'Current Month Transactions',
    'VolumeLastMonth': 'Last Month Volume',
    'VolumeCurrentMonth': 'Current Month Volume',
    'ChurnType': 'Churn Type',
    'ChurnVolume': 'Churn Volume',
    'ActiveTarget': 'Active Target',
    'Current_MonthTarget': 'Current Month Target',
    'Pre_MonthTarget': 'Previous Month Target'
}
# Define the table object based on the reflected schema
mytable = metadata.tables['merchants']
# Define dictionary to map mytable column names to dataframe column names
column_name_mapping = {col.name: column_mapping[col.name] for col in mytable.columns}

# Read data from Excel file
df = pd.read_excel('apps\\home\\data\\Suez8-5.xlsx', sheet_name='BASE')
# Replace spaces in column names with underscores
df = df.rename(columns=lambda x: x.replace(' ', '_'))
# Rename columns in dataframe using column_name_mapping dictionary
df = df.rename(columns=column_name_mapping)

"""
# Execute SELECT statement and return rows as list of tuples
rows = session.query(mytable).all()
list_of_tuples = [(row.id, row.name, row.age) for row in rows]

# Close session
session.close()
# Read data from Excel file
df = pd.read_excel('apps\\home\\data\\Suez8-5.xlsx', sheet_name='BASE')

# Replace spaces in column names with underscores
df = df.rename(columns=lambda x: x.replace(' ', '_'))

# Connect to SQLite database
conn = sqlite3.connect('db.sqlite3')

# Generate SQL create statement
create_table_sql = pd.io.sql.get_schema(df, 'merchants', con=conn).replace('"', '')

# Execute the create statement
conn.execute(create_table_sql)"""
rows = session.query(mytable).all()
list_of_tuples = [(row.id, row.name, row.age) for row in rows]

inspector = inspect(engine)
columns = inspector.get_columns('merchants')
for column in columns:
    print(column['name'], column['type'])