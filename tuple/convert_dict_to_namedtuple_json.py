from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here
BlogInfo = namedtuple('BlogInfo', ['name', 'founders', 'started', 'tags', 'location', 'site'])

def dict2nt(dict_):
    return BlogInfo(dict_['name'], dict_['founders'], dict_['started'], dict_['tags'], dict_['location'], dict_['site'])


def nt2json(nt):
    return json.dumps(dict(nt._asdict()), indent=4, sort_keys=True, default=str)


print(nt2json(dict2nt(blog)))