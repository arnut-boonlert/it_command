import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Define the directory for FTP users
ftp_dir = os.path.join(os.path.dirname(__file__), '../../serv_file_dir')

# Create the directory if it doesn't exist
if not os.path.exists(ftp_dir):
    os.makedirs(ftp_dir)

# Create an authorizer object to manage permissions
authorizer = DummyAuthorizer()

# Define a user with full permissions (read, write, delete, etc.)
authorizer.add_user("user", "password", ftp_dir, perm="elradfmw")

# Optionally, add an anonymous user with read-only permissions
authorizer.add_anonymous(ftp_dir)

# Create an FTP handler class that uses the authorizer
handler = FTPHandler
handler.authorizer = authorizer

# Set a custom banner (optional)
handler.banner = "Welcome to the FTP server."

# Create an FTP server instance
server = FTPServer(("0.0.0.0", 21), handler)

# Start the server
server.serve_forever()