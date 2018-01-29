from flask import (
    render_template,
    request,
    session,
    make_response,
    redirect,
    url_for,
    abort)
from flask.views import MethodView
from controllers import base
from logger import logger

class BaseView(MethodView):

    def __init__(self, *args, **kwargs):
        MethodView.__init__(self, *args, **kwargs)
        self.request = request
        try:
            self.controller = getattr(base, '{}{}'.format(str(self).replace('View', ''), 'Controller'))(request)
        except Exception as e:
            logger.error('{}{} does not exist'.format(str(self).replace('View', ''), 'Controller'))

    def __str__(self):
        return self.__class__.__name__

class IndexView(BaseView):

    def get(self):
        return render_template('index.html')

class NeedsView(BaseView):

    def get(self):
        return render_template('needs.html')

class VolunteersView(BaseView):

    def get(self):
        return render_template('volunteers.html')
