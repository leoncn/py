import socket
import logging

hostname='map.google.com'
addr = socket.gethostbyname(hostname)

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)
#d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger('tcpserver')

logger.info( "%s addr is %s" , hostname, addr)

foostr = 'abcde'
print foostr[::1]
print foostr[1::-1]