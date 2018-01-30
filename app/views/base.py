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

class SignupView(BaseView):

    def get(self):
        return render_template('signup.html')

class LoginView(BaseView):

    def get(self):
        return render_template('login.html')

class DonateView(BaseView):

    def get(self):
        return render_template('donate.html')

class NeedsView(BaseView):

    def get(self):
        return render_template('needs.html')

class VolunteersView(BaseView):

    def get(self):
        return render_template('volunteers.html')

class ContributorsView(BaseView):

    def get(self):
        return render_template('contributors.html')

class ResourcesView(BaseView):

    def get(self):
        return render_template('resources.html')

class CollaboratorsView(BaseView):

    def get(self):
        return render_template('collaborators.html')

class TeamsView(BaseView):

    def get(self):
        return render_template('teams.html')

class LiaisonView(BaseView):

    def get(self):
        return render_template('liaison.html')

class EventsView(BaseView):

    def get(self):
        return render_template('events.html')
