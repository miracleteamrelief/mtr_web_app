import sys
import os
from random import choice
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado import autoreload
from urls import app
from daemonize import Daemon
from config import app_cfg
from logger import logger

class Main(Daemon):
    arg_map = {
        'dev'       : 'development',
        'start'     : 'start',
        'stop'      : 'stop',
        'pull'      : 'pull',
        'restart'   : 'restart'}

    def __call__(self, arg):
        getattr(self, self.arg_map[arg])()

    def run(self):
        http_server = HTTPServer(WSGIContainer(app))
        http_server.listen(app_cfg[('SERVER', 'port')])
        http_server.debug = app_cfg[('FLASK', 'debug_on')]
        ioloop = IOLoop.instance()
        autoreload.start(ioloop)
        ioloop.start()

Main('/tmp/mtr.pid')(sys.argv[1])
