import pytest
from protocol import get_response
from datetime import datetime

CODE = 1488

ACTION = 'test'

DATE = datetime.now().timestamp()

DATA = 'test_data'

KEY = '-s'

REQUEST = { # изменен порядок ключей
    'time': DATE,
    'action': ACTION,
    'data': DATA,
}

RESP = { # изменен порядок ключей
    'key': KEY,
    'time': DATE,
    'action': ACTION,
    'data': DATA,
    'code': CODE,
}


def test_get_response(): # выводит True даже при разбросанных ключах в словаре
    resp = get_response(REQUEST, CODE, DATA, DATE, key=KEY)
    assert resp == RESP


def test_act_get_response():
    resp = get_response(REQUEST, CODE, DATA, DATE, key=KEY)
    act = resp.get('action')
    assert act == ACTION


def test_code_get_response():
    resp = get_response(REQUEST, CODE, DATA, DATE, key=KEY)
    code = resp.get('code')
    assert code == CODE


def test_time_get_response():
    resp = get_response(REQUEST, CODE, DATA, DATE, key=KEY)
    time = resp.get('time')
    assert time == DATE


def test_dt_get_response():
    resp = get_response(REQUEST, CODE, DATA, DATE, key=KEY)
    dt = resp.get('data')
    assert dt == DATA


def test_key_get_response():
    resp = get_response(REQUEST, CODE, DATA, DATE, key=KEY)
    key = resp.get('key')
    assert key == KEY


def test_invalid_get_resp():
    with pytest.raises(AttributeError):
        resp = get_response(None, CODE)