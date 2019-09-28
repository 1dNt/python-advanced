import json
import logging
from protocol import validate_request, make_400, make_404, make_500
from middlewares import comp_middleware, decomp_mid_key


@comp_middleware
def handle_tcp_req(bytes_req, action_mapping):
    """
    Функция обработки запроса
    :param bytes_req: bytes
    :param action_mapping: dict
    :return: bytes
    """
    req = json.loads(bytes_req)
    if validate_request(req):
        action = req.get('action')
        controller = action_mapping.get(action)
        if controller:
            try:
                resp = controller(req)
                logging.debug(f'Request: {bytes_req.decode()}')
            except Exception as err:
                resp = make_500(req)
                logging.critical(err)
        else:
            resp = make_404(req)
            logging.error(f'404: Wrong action: {req}')
    else:
        resp = make_400(req, 'Request is not valid')
        logging.error(f'400: Wrong request: {req}')
    str_resp = json.dumps(resp)
    return str_resp.encode()


@decomp_mid_key
def handle_resp_key(bytes_resp):  # TODO костыль для функции остановки сервера
    try:
        return json.loads(bytes_resp).pop('key')
    except KeyError:
        return None
