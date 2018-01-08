import sys
import os

class BaseController(object):
	pass

##############################################################################
# Index Controller
##############################################################################

class IndexController(BaseController):

    def get(self):
        return self.context
