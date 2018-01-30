import sys
import os

class BaseController(object):

    def __init__(self, request):
        self.request = request

    def __str__(self):
        return self.__class__.__name__.lower().replace('controller', '')

##############################################################################
# Index Controller
##############################################################################

class IndexController(BaseController):

    def get(self):
        return self.context

class SignupController(BaseController):

    def get(self):
        return self.context

class LoginController(BaseController):

    def get(self):
        return self.context

class DonateController(BaseController):

    def get(self):
        return self.context

class NeedsController(BaseController):

    def get(self):
        return self.context

class VolunteersController(BaseController):

    def get(self):
        return self.context

class ContributorsController(BaseController):

    def get(self):
        return self.context

class ResourcesController(BaseController):

    def get(self):
        return self.context

class CollaboratorsController(BaseController):

    def get(self):
        return self.context

class TeamsController(BaseController):

    def get(self):
        return self.context

class LiaisonController(BaseController):

    def get(self):
        return self.context

class EventsController(BaseController):

    def get(self):
        return self.context
