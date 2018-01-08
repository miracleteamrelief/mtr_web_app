import hmac
from config import app_cfg
from logger import logger

def make_digest(*args):
    digest_maker = hmac.new(app_cfg[('FLASK', 'secret_key')])
    for arg in args:
        digest_maker.update(arg)
    return digest_maker.hexdigest()

def validate_digest(a, b):
    return a == b

if __name__ == '__main__':
    print make_digest('cary', 'jones')
