from main_actions.controllers import timestamp_controller, echo_controller
from server_manage.controllers import sh_server_controller
from .fixtures import *


def test_data_timestamp_controller(init_req):
    resp = timestamp_controller(init_req)
    data = resp.get('data')
    assert data is not None and type(data) == float


def test_data_echo_controller(init_req, exp_data):
    resp = echo_controller(init_req)
    data = resp.get('data')
    assert data == exp_data


def test_key_sh_server_controller(init_shd_req, exp_key):
    resp = sh_server_controller(init_shd_req)
    data = resp.get('key')
    assert data == exp_key


def test_succ_sh_server_controller(init_shd_req, exp_codes):
    resp = sh_server_controller(init_shd_req)
    data = resp.get('code')
    assert data == exp_codes.get('make200')


def test_fail_sh_server_controller(init_req, exp_codes):
    resp = sh_server_controller(init_req)
    data = resp.get('code')
    assert data == exp_codes.get('make401')
