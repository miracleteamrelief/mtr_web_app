import time
from datetime import datetime as dt
from datetime import timedelta as td
from base import *
from utils.crypt import validate_digest

class Users(Multi):
    _dataconnector = DataConnector('users')
    form = Form('user')

    def __init__(self):
        self.items = [User(**item) for item in list(self._dataconnector)]

    def __len__(self):
        return sum(1 for x in self)

class User(Singleton):
    pass
