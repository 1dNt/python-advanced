import yaml
import socket
import json
import zlib
import threading
from datetime import datetime
from argparse import ArgumentParser


def get_request(action, text, date=datetime.now()):
    return {
        'action': action,
        'data': text,
        'time': date.timestamp()
    }


def read(sock, buffer):
    while True:
        try:
            if shd_key:
                sock.close()
                break
            else:
                bytes_resp = zlib.decompress(sock.recv(buffer))
                resp = json.loads(bytes_resp)
                print(f'\n{resp}')
        except:
            sock.close()
            print(resp.get('data'))
            break


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
    shd_key = False

    try:
        sock = socket.socket()
        sock.connect((host, port))

        read_thread = threading.Thread(target=read, args=(sock, buffer))
        read_thread.start()

        while True:
            action = input('Enter action name: ')
            if action == 'client shd':  # У меня почему то "Ctrl+C" не останавилвает программу в терминале PyCh :D
                shd_key = True
                sock.close()
                break
            else:
                msg = input('Enter your message: ')

                req = get_request(action, msg)
                str_req = json.dumps(req)
                bytes_req = str_req.encode()

                sock.send(zlib.compress(bytes_req))
    except:
        print('Client has been shutdown')
