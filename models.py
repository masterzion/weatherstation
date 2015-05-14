import sqlite3

conn = sqlite3.connect('/root/weatherstation/smarthome.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS sensors (id INTEGER PRIMARY KEY AUTOINCREMENT, sensor1 real, datetime string )')


class Sensors():
    def getLast(self):
        c.execute('SELECT round(sensor1, 2) FROM sensors ORDER BY id DESC LIMIT 1')
        return c.fetchone()

    def getDay(self):
      sql =  "select "
      sql += "substr(datetime,12,4) || '0' as date, "
      sql += "round(avg(sensor1), 2) as temp1 "
      sql += "from sensors "
      sql += "where id in ( select id from sensors order by id desc limit 1440 ) "
      sql += "group by substr(datetime,1,15) || '0' "
      c.execute(sql)
      return c.fetchall()

    def InsertData(self, sensor1, datetime):
        c.execute("INSERT INTO sensors (sensor1, datetime)  VALUES ("+str(sensor1)+",'"+datetime+"')")
        conn.commit()


'''
class Sensors(Model):
    id = UUIDField(primary_key=True)
    sensor1 = FloatField()
    datetime = DateTimeField()

    class Meta:
        database = db

    def getLast():
        return Sensors.select(Sensors.sensor1).order_by(Sensors.id.desc()).limit(1).get()

 
if __name__ == "__main__":
    try:
        Sensors.create_table()
    except peewee.OperationalError:
        print "Artist table already exists!"


if __name__ == "__main__":
    try:
        c.execute('CREATE TABLE IF NOT EXISTS sensors (id INTEGER PRIMARY KEY AUTOINCREMENT, sensor1 real, datetime string )')
    except peewee.OperationalError:
        print "sensors table already exists!"

'''