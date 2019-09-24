from datetime import datetime


def validate_request(request):
    """
    Проверка корректности запроса
    :param request: dict
    :return: bool
    """
    return 'action' in request and 'time' in request and request.get('action') and request.get('time')


def get_response(request, code, data=None, date=datetime.now(), **kw):
    """
    Формирует ответ сервера
    :param request: dict
    :param code: int
    :param data: any
    :param date: timestamp
    :return: dict
    """
    return {
        'action': request.get('action'),
        'time': date.timestamp() if isinstance(date, datetime) else date,
        'code': code,
        'data': data,
        'key': kw.get('key'),
    }


def make_200(request, data=None, date=datetime.now(), **kw):
    return get_response(request, 200, data, date, **kw)


def make_400(request, data=None, date=datetime.now()):
    return get_response(request, 400, data, date)


def make_404(request, date=datetime.now()):
    return get_response(request, 404, f'404: Action {request.get("action")} not found', date)


def make_401(request, date=datetime.now()):
    return get_response(request, 401, f'401: Unauthorized. Please enter the password', date)


def make_500(request, date=datetime.now()):
    return get_response(request, 500, '500: Internal server error', date)
