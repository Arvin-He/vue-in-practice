import sys
import logging
from tornado import web
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import define, options

WEB_SETTINGS = {
    'autoreload': False,
    'xsrf_cookies': False,
    'error': False,
    'login_url': '/api/login',
    'cookie_secret': '123456'
}


class TodosHandler(web.RequestHandler):

    def get(self):
        self.set_header('Access-Control-Allow-Origin', '*') 
        self.set_header('Access-Control-Allow-Headers', 'x-requested-with')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE')
        data = {"data": [{"id": 1, "title": "Learn Vue.js", "completed": False},
                {"id": 2, "title": "Learn React.js", "completed": False}]}
        self.write(data)
        self.finish()


urlhandlers = [
    (r'/api/todos', TodosHandler)
]


def run():
    app = web.Application(handlers=urlhandlers, **WEB_SETTINGS)
    define('port', default=8012, help='run on given port', type=int)
    print("Starting tornado web server on http://127.0.0.1:{}".format(options.port))
    print("Quit the server with Ctrl-C")
    if sys.platform == 'win32':
        app.listen(options.port)
    else:
        server = HTTPServer(app)
        server.bind(options.port)
        server.start(0)  # fork one process per cpu
    IOLoop.current().start()

if __name__ == "__main__":
    run()