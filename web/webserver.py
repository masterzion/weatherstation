import os
import tornado.ioloop
import tornado.web
import sqlite3
import json

root = os.path.dirname(__file__)
port = 8888

conn = sqlite3.connect('/root/weatherstation/smarthome.db')

class TempLast(tornado.web.RequestHandler):
    def get(self):
        c = conn.cursor()
        c.execute('SELECT * FROM sensors ORDER BY id DESC LIMIT 1')
        data=c.fetchone()
        self.write(str("%.2f" % round(data[2],2) ))

class TempDay(tornado.web.RequestHandler):
    def get(self):
      c = conn.cursor()
      sql =  "select "
      sql += "substr(datetime,12,4) || '0' as date, "
      sql += "round(avg(value), 2) as temp1 "
      sql += "from sensors "
      sql += "where id in ( select id from sensors order by id desc limit 1440 ) "
      sql += "group by substr(datetime,1,15) || '0' "
      c.execute(sql)
      data=c.fetchall()
      self.write(json.dumps(data))

application = tornado.web.Application([
    (r"/last/", TempLast),
    (r"/day/", TempDay),
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": root, "default_filename": "index.html"}),
])


if __name__ == '__main__':
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
