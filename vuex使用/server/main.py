import os
import sys
import json
import logging
from logging.handlers import TimedRotatingFileHandler
from tornado import web
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import define, options

try:
    import coloredlogs
    LOG_UES_COLOR = True
except ImportError:
    LOG_UES_COLOR = False

WEB_SETTINGS = {
    'autoreload': False,
    'xsrf_cookies': False,
    'error': False,
    'login_url': '/api/login',
    'cookie_secret': '123456'
}


def create_logger(logname='logs.log', logconsole=True, level=logging.INFO):
    FORMAT = "%(asctime)s [%(levelname)s] [%(filename)s] [%(lineno)d]: %(message)s"
    logdir = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), "logs")
    if not os.path.exists(logdir):
        os.mkdir(logdir)

    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    formatter = logging.Formatter(fmt=FORMAT, datefmt="%m/%d/%Y %H:%M:%S")

    fh = TimedRotatingFileHandler(filename=os.path.join(logdir, logname),
                                  when='midnight',
                                  interval=1,
                                  encoding='utf-8')
    fh.setLevel(level)
    fh.suffix = "%Y-%m-%d.log"
    fh.setFormatter(formatter)
    root_logger.addHandler(fh)

    if logconsole:
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(formatter)
        root_logger.addHandler(ch)

    if LOG_UES_COLOR:
        FIELD_STYLES = {'asctime': {'color': 'green'},
                        'hostname': {'color': 'magenta'},
                        'levelname': {'color': 'magenta'},
                        'programname': {'color': 'cyan'},
                        'lineno': {'color': 'magenta'},
                        'name': {'color': 'blue'}}
        coloredlogs.install(fmt=FORMAT,
                            logger=root_logger,
                            field_styles=FIELD_STYLES)


class TodosHandler(web.RequestHandler):

    def get(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', 'x-requested-with')
        self.set_header('Access-Control-Allow-Methods',
                        'POST, GET, PUT, DELETE')
        data = {"data": [{"id": 1, "title": "Learn Vue.js", "completed": False},
                         {"id": 2, "title": "Learn React.js", "completed": False}]}
        self.write(data)
        self.finish()


class TodoHandler(web.RequestHandler):

    def get(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', 'x-requested-with')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE')
        index = self.request.uri.split('/')[-1]
        data = [{"id": 1, "title": "Learn Vue.js", "completed": False},
                {"id": 2, "title": "Learn React.js", "completed": False}]
        index = int(index)-1
        self.write(data[index])
        self.finish()


class TodoAddHandler(web.RequestHandler):

    def initialize(self):
        pass

    def post(self):
        data = [{"id": 1, "title": "Learn Vue.js", "completed": False},
                {"id": 2, "title": "Learn React.js", "completed": False}]
        item = json.loads(self.request.body.decode())
        self.write({"id": len(data)+1, "title": item['title'], "completed": False})
        self.finish()


class TodoDeleteHandler(web.RequestHandler):

    def initialize(self):
        pass

    def delete(self):
        data = [{"id": 1, "title": "Learn Vue.js", "completed": False},
                {"id": 2, "title": "Learn React.js", "completed": False}]
        self.write({"result": "success"})
        self.finish()

urlhandlers = [
    (r'/api/todos', TodosHandler),
    (r'/api/todo/.?\d*', TodoHandler),
    (r'/api/todo/create', TodoAddHandler),
    (r'/api/todo/.?\d*/delete', TodoDeleteHandler)
]


def run():
    create_logger(logname='main.log')
    app = web.Application(handlers=urlhandlers, **WEB_SETTINGS)
    define('port', default=8012, help='run on given port', type=int)
    logging.info(
        "Starting tornado web server on http://127.0.0.1:{}".format(options.port))
    logging.info("Quit the server with Ctrl-C")
    if sys.platform == 'win32':
        app.listen(options.port)
    else:
        server = HTTPServer(app)
        server.bind(options.port)
        server.start(0)  # fork one process per cpu
    IOLoop.current().start()


if __name__ == "__main__":
    run()
