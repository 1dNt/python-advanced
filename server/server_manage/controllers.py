from protocol import make_200, make_401


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

