from protocol import *
from datetime import datetime

CODES = {
    'make200': 200,
    'make400': 400,
    'make401': 401,
    'make404': 404,
    'make500': 500,
}

ACTION = 'test'

DATE = datetime.now().timestamp()

KEY = '-s'

REQUEST = {
    'time': DATE,
    'action': ACTION,
    'data': 'tes_data',
}


def test_make200():
    resp = make_200(REQUEST, date=DATE, key=KEY)
    code = resp.get('code')
    assert code == CODES.get('make200')


def test_make400():
    resp = make_400(REQUEST, date=DATE)
    code = resp.get('code')
    assert code == CODES.get('make400')


def test_make401():
    resp = make_401(REQUEST, date=DATE)
    code = resp.get('code')
    assert code == CODES.get('make401')


def test_make404():
    resp = make_404(REQUEST, date=DATE)
    code = resp.get('code')
    assert code == CODES.get('make404')


def test_make500():
    resp = make_500(REQUEST, date=DATE)
    code = resp.get('code')
    assert code == CODES.get('make500')