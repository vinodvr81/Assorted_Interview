
import sqlalchemy

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

from sqlalchemy import create_engine

# This engine just used to query for list of databases
mysql_engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}'.format("vinod", "Oncemore!1", "localhost", 3306))
mysql_engine.execute("USE Employee")
meta=MetaData()
cursor = mysql_engine.execute("select * from personnal_info")
result = cursor.fetchone()
print(result)
mysql_engine.execute("USE Employee")
cursor = mysql_engine.execute("insert into personnal_info values (2, 'Vukkalam','Nevaan','Palava','Navi Mumbai')")
result = cursor.fetchall()
print(result)
# students = Table('students', meta, Column('id', Integer, primary_key=True), Column('name', String), Column('lastname', String), )
# meta.create_all(mysql_engine)
#
#
#
# ins=students.insert().values(name='Ravi', lastname='Kapoor')
# conn = mysql_engine.connect()
# result = conn.execute(ins)