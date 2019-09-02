
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("the doctor", "1234", "/mnt/d/", perm="elradfmw")
authorizer.add_anonymous("/mnt/c/Users/akis/Desktop/Python/FTP Client-Server", perm="r")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("192.168.1.9", 2000), handler)
server.serve_forever()
