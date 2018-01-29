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

class NeedsController(BaseController):

    def get(self):
        return self.context

class VolunteersController(BaseController):

    def get(self):
        return self.context
