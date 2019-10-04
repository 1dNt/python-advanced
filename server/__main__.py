# python server
# python client
import yaml
import socket
import select
import logging
import threading
from argparse import ArgumentParser
from resolvers import get_server_action
from handlers import handle_resp_key, handle_tcp_req

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

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers={
        logging.FileHandler('server\logs\server.log'),
        logging.StreamHandler()
    }
)

requests = []
connections = []


def read(sock, requests, buffer):
    try:
        req = sock.recv(buffer)
        if req:
            requests.append(req)
    except:  # Избавляемся от зависания сервера
        """
        Удаляем из всех листов клиента, который сам отключился 
        Иначе сервер уходит в бесконечный краш при попытках взаимодействия с отключенным клиентом: 
        ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host
        """
        connections.remove(sock)
        rlist.remove(sock)
        wlist.remove(sock)


def write(sock, resp):
    sock.send(resp)


try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.setblocking(False)
    # sock.settimeout(0)
    sock.listen(3)

    logging.info(f'Server started with {host}:{port}')

    action_mapping = get_server_action()

    while True:
        s_key = None
        try:
            client, (client_host, client_port) = sock.accept()
            logging.info(f'Client {client_host}:{client_port} was connected')
            connections.append(client)
        except:
            pass
        if connections:  # !!!
            """
            Без этого решения сервер валится при запуске на Windows через sock.settimeout(n) секунд
            Тк connections = [] пустой. С обшибкой:
                File "server\__main__.py", line 76, in <module>
                    rlist, wlist, xlist = select.select(connections, connections, connections, 0)
                OSError: [WinError 10022] An invalid argument was supplied
                
            Походу функция select на Win не хочет отрабатывать с пустым списком?
            """
            rlist, wlist, xlist = select.select(connections, connections, connections, 0)

            for read_client in rlist:
                read_thread = threading.Thread(target=read, args=(read_client, requests, buffer))
                read_thread.start()

            if requests:
                bytes_req = requests.pop()
                bytes_resp = handle_tcp_req(bytes_req, action_mapping)
                s_key = handle_resp_key(bytes_resp)  # TODO костыль для функции удаленной остановки сервера

                for write_client in wlist:
                    write_thread = threading.Thread(target=write, args=(write_client, bytes_resp))
                    write_thread.start()

            if s_key == 'shd':
                sock.close()
                logging.info('Server has been shutdown by client command')
                break

except KeyboardInterrupt:
    logging.info('Server shutdown')

# Traceback (most recent call last):
#   File "C:\Program Files\Python37\lib\threading.py", line 917, in _bootstrap_inner
#     self.run()
#   File "C:\Program Files\Python37\lib\threading.py", line 865, in run
#     self._target(*self._args, **self._kwargs)
#   File "server\__main__.py", line 49, in read
#     req = sock.recv(buffer)
# ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host

