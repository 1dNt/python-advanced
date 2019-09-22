from .controllers import *


actionmapping = [
    {'action': 'server shutdown', 'controller': sh_server_controller},
    {'action': 'error', 'controller': errors_controller},
]