import tornado.ioloop
import tornado.web

from database import Graph
from session import Session


class MainHandler(tornado.web.RequestHandler):
    def initialize(self, session):
        self.session = session

    def get(self, action):
        if action == 'init':
            self.session.restart()
            self.write(self.session.ask())
        elif action == 'submit':
            data = self.get_argument("data")
            self.session.answer(data)
            self.write(self.session.ask())
        else:
            self.clear()
            self.set_status(403, "bad request333")
            self.finish()


session = Session(Graph.get_graph())

app = tornado.web.Application([
    (r"/api/([^/]*)/?", MainHandler, dict(session=session)),
])

if __name__ == "__main__":
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
