from functools import reduce

from settings import INSTALLED_APPS


def get_server_action():
    application = reduce(
        lambda value, itm: value + [__import__(f'{itm}.routes')],
        INSTALLED_APPS, []
    )
    routes = reduce(
        lambda value, itm: value + [getattr(itm, 'routes', None)],
        application, []
    )
    mapping = reduce(
        lambda value, itm: value + getattr(itm, 'actionmapping', []),
        routes, []
    )
    return {itm.get('action'):itm.get('controller') for itm in mapping if itm}


def resolve(action, routes):
    return routes.get(action)