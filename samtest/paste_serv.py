
from paste.deploy import loadapp
from wsgiref.simple_server import make_server
import signal
import os

def sigint_handler(signal, frame):
    """Exits at SIGINT signal."""
    logging.debug('SIGINT received, stopping servers.')
    sys.exit(0) 

def main():
    signal.signal(signal.SIGINT, sigint_handler)
    configfile="etc/samtest-paste.ini"
    appname="main"
    wsgi_app = loadapp("config:%s" % os.path.abspath(configfile), appname)
    server = make_server('localhost',8088,wsgi_app)
    server.serve_forever()   


if __name__ == "__main__":
    main()
