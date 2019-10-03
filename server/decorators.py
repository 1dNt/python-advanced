import logging
from functools import wraps

logger = logging.getLogger('controllers')

fh = logging.FileHandler('server\logs\controllers.log')
fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(fh)


def log(log_format):
    def decor(func):
        @wraps(func)
        def wrap(req, *args, **kwargs):
            res = func(req, *args, **kwargs)
            logger.debug(
                log_format % {'name': func.__name__, 'req': req, 'args': args, 'kwargs': kwargs, 'res': res}
            )
            return res
        return wrap
    return decor
