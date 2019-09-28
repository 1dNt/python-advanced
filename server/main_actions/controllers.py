from datetime import datetime
from protocol import make_200
from decorators import log


@log('Controller: %(name)s, Request: %(req)s - Response: %(res)s')
def timestamp_controller(request):
    """
    Возвращается время на сервере в формате datastamp
    :param request: dict
    :return: dict
    """
    return make_200(request, datetime.now().timestamp())


@log('Controller: %(name)s, Request: %(req)s - Response: %(res)s')
def echo_controller(request):
    """
    Возвращает полученный запрос обратно
    :param request: dict
    :return: dict
    """
    return make_200(request, request.get('data'))