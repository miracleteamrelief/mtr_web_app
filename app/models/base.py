import sys
import re
from pprint import pprint, pformat
from operator import attrgetter, itemgetter
from data.data import DataConnector
from forms import Form
from logger import logger

class Base(object):

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return pformat(
            [vars(item) for item in self.items])\
            if hasattr(self, 'items') else pformat(vars(self))

class Multi(Base):

    def __init__(self, user_id=None):
        self.user_id = user_id

    def __iter__(self):
        return (item for item in self.items)

    def __len__(self):
        return sum(1 for x in self)

    def __contains__(self, _id):
        return any(_id == str(item._id) for item in self)

    def __getitem__(self, _id):
        for item in self:
            if hasattr(item, '_id') and str(item._id) == _id:
                return item

    def __add__(self, data):
        data = vars(data) if not isinstance(data, dict) else data
        obj = self.form.to_obj(data, self)
        if any([key for key in obj.__dict__ if key in data.keys()]):
            _id = self._dataconnector + {k: v for k, v in vars(obj).items()
                                         if k not in ('_id', '__doc__', '__module__')}
            self.items.append(obj)
            return str(_id)
        else:
            raise ValueError(
                'Create data cannot be empty (check that data attributes match form validation)')

    def __iadd__(self, update_info):
        _id, data = update_info
        self[_id].__dict__.update(data)
        if _id in self:
            obj = self.form.to_obj(self[_id].__dict__, self)
            self._dataconnector += (_id,
                                    {k: v for k, v in vars(obj).items() if k not
                                     in ('_id', 'items', '__doc__', '__module__')})
        else:
            raise LookupError('PUT: _id {} not found in the database'.format(_id))
        return self

    def __sub__(self, _id):
        if _id in self:
            data = self._dataconnector[_id]
            obj = self.form.to_obj(data, self)
            self._dataconnector - _id
        else:
            raise LookupError('DELETE: _id {} not found in the database'.format(_id))
        return self

    def get_by_attr(self, attr):
        return [item[attr] for item in self]

    def filter_by_attr(self, attr, condition):
        return [item for item in self if hasattr(item, attr) and eval(condition.format(item=getattr(item, attr)))]

    def filter_by_attrs(self, condition_map, operator='&'):
        prev = None
        for attr in condition_map:
            curr = [item for item in self if hasattr(item, attr) and eval(condition_map[attr].format(item=getattr(item, attr)))]
            if operator == '^':
                prev = list(set(curr).symmetric_difference(set(prev if prev else curr)))
            elif operator == '|':
                prev = list(set(curr).union(set(prev if prev else curr)))
            elif operator == '&':
                prev = list(set(curr).intersection(set(prev if prev else curr)))
            elif operator == '-':
                prev = list(set(curr).difference(set(prev if prev else curr)))
        return prev

    def clear(self):
        answer = raw_input('Are you sure you want to clear all the {} data for'
            ' user (user_id: {})?'.format(str(self), self._user_id))
        if answer in ('Y', 'y', 'Yes', 'yes'):
            self._dataconnector.clear()
        else:
            sys.exit('Someone tried to clear the {} data for user (user_id: {})'\
                .format(str(self), self._user_id))

    def run_migrations(self, versions=[]):
        if versions:
            for version in versions:
                getattr(self, 'migration_{}'.format(version.zfill(5)))()
        else:
            for attr in sorted(dir(self)):
                if 'migration_' in attr:
                    getattr(self, attr)()

    def find(self, search_string):
        results = []
        for item in self:
            for k, v in item.__dict__.items():
                match = re.search(search_string, unicode(v), re.I) if k not in ('_id', 'user_digest') else None
                if search_string in unicode(v) or match:
                    v = unicode(v).replace(
                        search_string,
                        '<span style="background-color:yellow">{}</span>'.format(search_string))
                    results += [(item._id, v, unicode(v)[:128] + '...' if len(unicode(v)) > 128 else v)]
        return (results, str(self), len(results))

class Singleton(Base):

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getitem__(self, item):
        return self.__dict__.get(item)

    def __iadd__(self, data):
        self.__dict__.update(data)
        self._dataconnector += data
