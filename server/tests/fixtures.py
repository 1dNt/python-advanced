import pytest
from datetime import datetime


@pytest.fixture
def exp_code():
    return 1488


@pytest.fixture
def exp_codes():
    return {
        'make200': 200,
        'make400': 400,
        'make401': 401,
        'make404': 404,
        'make500': 500,
    }


@pytest.fixture
def exp_action():
    return 'test'


@pytest.fixture
def exp_date():
    return datetime.now().timestamp()


@pytest.fixture
def exp_data():
    return 'test_data'


@pytest.fixture
def exp_pss():
    return '12345'


@pytest.fixture
def exp_key():
    return 'shd'


@pytest.fixture
def init_req(exp_action, exp_date, exp_data):
    return {  # изменен порядок ключей
        'time': exp_date,
        'action': exp_action,
        'data': exp_data,
    }


@pytest.fixture
def init_resp(exp_action, exp_code, exp_date, exp_data, exp_key):
    return {  # изменен порядок ключей
        'key': exp_key,
        'time': exp_date,
        'action': exp_action,
        'data': exp_data,
        'code': exp_code,
    }


@pytest.fixture
def init_shd_req(exp_action, exp_date, exp_pss):
    return {  # изменен порядок ключей
        'time': exp_date,
        'action': exp_action,
        'data': exp_pss,
    }
