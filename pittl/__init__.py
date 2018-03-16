import os
import json
import jinja2
import falcon
import gunicorn.app.base
import multiprocessing

from wsgiref import simple_server
from gunicorn.six import iteritems


LOCAL_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(LOCAL_DIR, 'templates/html/')


def render_template(fname, context={}):
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(
            searchpath=TEMPLATE_DIR)).get_template(fname).render(context)


class Gallery():
    def __init__(self):
        pass

    def on_get(self, req, resp):
        # check if url is provided
        try:
            url = req.params['url']
        except Exception as e:
            print(e)
        print(TEMPLATE_DIR)
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.body = render_template('gallery.html')


class Server(gunicorn.app.base.BaseApplication):
    def __init__(self, host, port):
        self._host = host
        self._port = port

        self._gunicorn_options = {
            'bind': f'{host}:{port}',
            'workers': (multiprocessing.cpu_count() * 2) + 1
        }

        self._api = falcon.API()
        self._api.add_route('/gallery', Gallery())
        super().__init__()

    def load(self):
        return self._api

    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self._gunicorn_options)
                       if key in self.cfg.settings and value is not None])

        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def start(self, debug=False):
        if not debug:
            print('Server running...')
            self.run()
        else:
            print('Starting development HTTP server')
            httpd = simple_server.make_server(self._host, self._port, self._api)
            httpd.serve_forever()
