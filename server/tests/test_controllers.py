from main_actions.controllers import timestamp_controller, echo_controller
from server_manage.controllers import sh_server_controller
from datetime import datetime

DATE = datetime.now().timestamp()

DATA = 'test_data'

KEY = 'shd'

REQUEST = { # изменен порядок ключей
    'time': DATE,
    'action': 'test',
    'data': DATA,
}

SHD_REQUEST = { # специальный запрос на выключение сервера
    'time': DATE,
    'action': 'test',
    'data': '12345',
}


def test_data_timestamp_controller():
    resp = timestamp_controller(REQUEST)
    data = resp.get('data')
    assert data is not None and type(data) == float


def test_data_echo_controller():
    resp = echo_controller(REQUEST)
    data = resp.get('data')
    assert data == DATA


def test_key_sh_server_controller():
    resp = sh_server_controller(SHD_REQUEST)
    data = resp.get('key')
    assert data == KEY


def test_succ_sh_server_controller():
    resp = sh_server_controller(SHD_REQUEST)
    data = resp.get('code')
    assert data == 200


def test_fail_sh_server_controller():
    resp = sh_server_controller(REQUEST)
    data = resp.get('code')
    assert data == 401


