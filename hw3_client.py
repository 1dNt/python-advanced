import yaml
import socket
import json
from argparse import ArgumentParser


def get_request(text):
    return {
        'data': text
    }


if __name__ == '__main__':
    cfg = dict(host='localhost', port=8000, buffersize=1024)

    parser = ArgumentParser()
    parser.add_argument('-c', '--config', type=str, required=False,
                        help='Set config path')
    parser.add_argument('-ht', '--host', type=str, required=False,
                        help='Set server host')
    parser.add_argument('-p', '--port', type=int, required=False,
                        help='Set server port')
    parser.add_argument('-bf', '--buffer', type=int, required=False,
                        help='Set buffer size')

    args = parser.parse_args()

    if args.config:
        with open(args.config) as file:
            file_config = yaml.safe_load(file)
            cfg.update(file_config or {})

    host = args.host if args.host else cfg.get('host')
    port = args.port if args.port else cfg.get('port')
    buffer = args.buffer if args.buffer else cfg.get('buffersize')

    sock = socket.socket()
    sock.connect((host, port))

    msg = input('Enter your message: ')
    req = get_request(msg)
    str_req = json.dumps(req)

    sock.send(str_req.encode('utf-8'))
    bytes_resp = sock.recv(buffer)

    resp = json.loads(bytes_resp)

    print(f'Send message {req} to {host}:{port}')
    print(resp)
    print(f'Client configuration: {resp.get("client_host")}:{resp.get("client_port")}\n Serv resp: {resp.get("data")}')

    sock.close()
