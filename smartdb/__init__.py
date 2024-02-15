# __init__ | SmartDB

try:
    from smartdb.modules import *
except ImportError:
    print('Your SmartDB is broken. Please reinstall SmartDB.')