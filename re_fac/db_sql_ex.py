
import sqlalchemy

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

from sqlalchemy import create_engine

mysql_engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}'.format("root", "root", "localhost", 3306))
mysql_engine.execute("USE bookinfo")
meta=MetaData()
cursor = mysql_engine.execute("select * from author")
result = cursor.fetchone()
print(result)
mysql_engine.execute("USE bookinfo")
cursor = mysql_engine.execute("insert into author values (DEFAULT, 'Vukkalam Nevaan','India','Navi Mumbai')")
result = cursor.fetchall()
print(result)