from protocol import *
from .fixtures import *


def test_make200(init_req, exp_codes, exp_date, exp_key):
    resp = make_200(init_req, date=exp_date, key=exp_key)
    code = resp.get('code')
    assert code == exp_codes.get('make200')


def test_make400(init_req, exp_codes, exp_date):
    resp = make_400(init_req, date=exp_date)
    code = resp.get('code')
    assert code == exp_codes.get('make400')


def test_make401(init_req, exp_codes, exp_date):
    resp = make_401(init_req, date=exp_date)
    code = resp.get('code')
    assert code == exp_codes.get('make401')


def test_make404(init_req, exp_codes, exp_date):
    resp = make_404(init_req, date=exp_date)
    code = resp.get('code')
    assert code == exp_codes.get('make404')


def test_make500(init_req, exp_codes, exp_date):
    resp = make_500(init_req, date=exp_date)
    code = resp.get('code')
    assert code == exp_codes.get('make500')
