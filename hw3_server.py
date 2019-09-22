import yaml
import socket
import json
from argparse import ArgumentParser


if __name__ == '__main__':
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

    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(3)

    while True:
        client, (client_host, client_port) = sock.accept()
        print(f'Client {client_host}:{client_port} was connected')

        bytes_req = client.recv(buffer)
        resp = json.loads(bytes_req)
        resp['client_host'] = client_host
        resp['client_port'] = client_port
        bytes_resp = json.dumps(resp).encode('utf-8')
        print(f"Json request: {bytes_req.decode('utf-8')}")
        print(f'Source request: {json.loads(bytes_req)}')
        client.send(bytes_resp)

        client.close()
