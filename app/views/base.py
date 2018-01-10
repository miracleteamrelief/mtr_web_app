from flask import (
    render_template,
    request,
    session,
    make_response,
    redirect,
    url_for,
    abort)
from flask.views import MethodView

class BaseView(MethodView):
    context    = {}

    def __init__(self, *args, **kwargs):
    	MethodView.__init__(self, *args, **kwargs)

class IndexView(BaseView):

	def get(self):
		return render_template('index.html')

class NeedsView(BaseView):

    def get(self):
        return render_template('needs.html')

class VolunteersView(BaseView):

    def get(self):
        return render_template('volunteers.html')        