import os
import tornado.ioloop
import tornado.web
import json
from models import Sensors

root = os.path.dirname(__file__)
port = 8888

class TempLast(tornado.web.RequestHandler):
    def get(self):
        data = Sensors().getLast();
        self.write(str(data[0]))

class TempDay(tornado.web.RequestHandler):
    def get(self):
      data = Sensors().getDay()
      self.write(json.dumps(data))

application = tornado.web.Application([
    (r"/last/", TempLast),
    (r"/day/", TempDay),
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": root, "default_filename": "index.html"}),
])


if __name__ == '__main__':
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
