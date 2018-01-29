import os
from ConfigParser import ConfigParser
from logger import logger

CONFIG_DIR = os.environ['MTR_CONFIG_DIR']

class Base(ConfigParser):

    def __str__(self):
        return self.__class__.__name__.lower()

    def __init__(self, *args, **kwargs):
        ConfigParser.__init__(self, *args, **kwargs)
        self.read(CONFIG_DIR + '/{}.cfg'.format(str(self)))

    def __getitem__(self, item_tuple):
        return self.get(*item_tuple)

class App(Base):
    pass

app_cfg = App()
