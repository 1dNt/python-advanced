# python server
# python client.py
import yaml
import json
import socket
from argparse import ArgumentParser

from resolvers import get_server_action
from protocol import validate_request, make_400, make_404, make_500

cfg = dict(host='localhost', port=8000, buffersize=1024)

parser = ArgumentParser()
parser.add_argument('-c', '--config', type=str, required=False,
                    help='Set config path')
parser.add_argument('-ht', '--host', type=str, required=False,
                    help='Set server host')
parser.add_argument('-p', '--port', type=str, required=False,
                    help='Set server port')
parser.add_argument('-bf', '--buffer', type=int, required=False,
                    help='Set buffer size')

args = parser.parse_args()

if args.config:
    with open(args.config) as file:
        file_config = yaml.safe_load(file)
        cfg.update(file_config or {})

host = args.host if args.host else cfg.get('host')
port = int(args.port) if args.port else int(cfg.get('port'))
buffer = args.buffer if args.buffer else cfg.get('buffersize')

try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(3)

    print(f'Server started with {host}:{port}')

    action_mapping = get_server_action()

    while True:
        client, (client_host, client_port) = sock.accept()
        print(f'Client {client_host}:{client_port} was connected')

        bytes_req = client.recv(buffer)

        req = json.loads(bytes_req)

        if validate_request(req):
            action = req.get('action')
            controller = action_mapping.get(action)
            if controller:
                try:
                    resp = controller(req)
                    print(f'Request: {bytes_req.decode()}')
                except Exception as err:
                    resp = make_500(req)
                    print(err)
            else:
                resp = make_404(req)
                print(f'404: Wrong action: {req}')
        else:
            resp = make_400(req, 'Request is not valid')
            print(f'400: Wrong request: {req}')

        try:
            s_key = resp.pop('key')
        except KeyError:
            pass

        str_resp = json.dumps(resp)
        client.send(str_resp.encode())
        client.close()

        if s_key == 'shd':
            print('Server has been shutdown by client command')
            break

except KeyboardInterrupt:
    print('Server shutdown')
