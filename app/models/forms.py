import re
from datetime import datetime
from bson import ObjectId
from logger import logger
from config import app_cfg

class Form(object):

    def __init__(self, field_type):
        self.fields = dict(
            f.split(':') for f in app_cfg[('FORMS', field_type)].split(','))

    def _convert_floatstr_to_int(self, field, v):
        if not isinstance(v, int) and self.fields[field] == 'int' and '.' in v:
            return v[:v.index('.')]
        return v

    def process(self, form_data):
        self.__dict__ = {'fields': self.__dict__['fields']}
        for k, v in form_data.items():
            for field in self.fields:
                sub = re.sub('{}'.format(''.join(k.split(field))), '', k)
                if field == k:
                    if self.fields[field] == 'int':
                        v = self._convert_floatstr_to_int(field, v)
                    if v in ('', u'') and self.fields[field] == 'float':
                        continue
                    try:
                        exec('self.__dict__[k] = {}(v)'.format(self.fields[field]))
                    except:
                        raise ValueError(
                            'Attribute for {}: {}, must be `{}` datatype'.format(
                                field, v.encode('utf-8'), self.fields[field]))
        return {k: v for k, v in self.__dict__.items() if k != 'fields'}

    def to_obj(self, form_data, klass):
        data = self.process(form_data)
        return type(str(klass), (klass.__class__.__mro__[1],), data)
