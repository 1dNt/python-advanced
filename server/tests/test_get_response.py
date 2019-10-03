from protocol import get_response
from .fixtures import *


def test_get_response(init_req, init_resp, exp_code, exp_data, exp_date,
                      exp_key):  # выводит True даже при разбросанных ключах в словаре
    resp = get_response(init_req, exp_code, exp_data, exp_date, key=exp_key)
    assert resp == init_resp


def test_act_get_response(init_req, exp_action, exp_code, exp_data, exp_date, exp_key):
    resp = get_response(init_req, exp_code, exp_data, exp_date, key=exp_key)
    act = resp.get('action')
    assert act == exp_action


def test_code_get_response(init_req, exp_code, exp_data, exp_date, exp_key):
    resp = get_response(init_req, exp_code, exp_data, exp_date, key=exp_key)
    code = resp.get('code')
    assert code == exp_code


def test_time_get_response(init_req, exp_code, exp_data, exp_date, exp_key):
    resp = get_response(init_req, exp_code, exp_data, exp_date, key=exp_key)
    time = resp.get('time')
    assert time == exp_date


def test_dt_get_response(init_req, exp_code, exp_data, exp_date, exp_key):
    resp = get_response(init_req, exp_code, exp_data, exp_date, key=exp_key)
    dt = resp.get('data')
    assert dt == exp_data


def test_key_get_response(init_req, exp_code, exp_data, exp_date, exp_key):
    resp = get_response(init_req, exp_code, exp_data, exp_date, key=exp_key)
    key = resp.get('key')
    assert key == exp_key


def test_invalid_get_resp(exp_code):
    with pytest.raises(AttributeError):
        get_response(None, exp_code)
