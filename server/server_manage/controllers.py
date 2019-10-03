from protocol import make_200, make_401
from decorators import log


@log('Controller: %(name)s, Request: %(req)s - Response: %(res)s')
def sh_server_controller(request):
    """
    Отсанавливает сервер, требудется ввод пароля
    :param request: dict
    :return: dict
    """
    if request.get('data') == '12345':
        return make_200(request, 'Server has been shutdown', key='shd')
    else:
        return make_401(request)


def errors_controller(request):
    raise Exception('Server error')
