import os
import tornado.ioloop
import tornado.web
import sqlite3


root = os.path.dirname(__file__)
port = 80


conn = sqlite3.connect('/root/smarthome.db')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        c = conn.cursor()
        c.execute('SELECT * FROM sensors ORDER BY id DESC LIMIT 1')
        data=c.fetchone()
#        print data[2]
        self.write(str(data[2]))


application = tornado.web.Application([
    (r"/last/", MainHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": root, "default_filename": "index.html"}),
])



if __name__ == '__main__':
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
