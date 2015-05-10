import os
import tornado.ioloop
import tornado.web
import sqlite3
import json


root = os.path.dirname(__file__)
port = 8888


conn = sqlite3.connect('/root/smarthome.db')


class TempLast(tornado.web.RequestHandler):
    def get(self):
        c = conn.cursor()
        c.execute('SELECT * FROM sensors ORDER BY id DESC LIMIT 1')
        data=c.fetchone()
        self.write(str("%.2f" % round(data[2],2) ))

class TempDay(tornado.web.RequestHandler):
    def get(self):
      c = conn.cursor()
      c.execute("select  substr(datetime,12,4) || '0' as date,  round(avg(value), 2) as temp1 from sensors group by substr(datetime,1,15) || '0' limit 144  ")
      data=c.fetchall()
      self.write(json.dumps(data))
'''
      prefix = ''
      out= "[\n"
      for row in data:
        out += prefix +" {\n";
        out += '  "date": "'  + row[0] + '",' + "\n"
        out += '  "temp1": ' + str(row[1]) + ',' + "\n"
        out += '  "temp2": ' + str(row[2]) + '' + "\n"
        out += " }"
        prefix = ",\n"
      out += "\n]"
      self.write(out)
'''



application = tornado.web.Application([
    (r"/last/", TempLast),
    (r"/day/", TempDay),
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": root, "default_filename": "index.html"}),
])



if __name__ == '__main__':
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
