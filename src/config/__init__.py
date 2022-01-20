import os

HOME_PATH = os.path.expanduser('~')
CONFIG_FOLDER_PATH = os.path.join(HOME_PATH, '.cherrynas')
CONFIG_FILE_NAME = "cherrynas.ini"
CONFIG_FILE_PATH = os.path.join(CONFIG_FOLDER_PATH, CONFIG_FILE_NAME)
LOG_PATH = os.path.join(CONFIG_FOLDER_PATH, "cherrynas.log")
DAEMON_LOCK_PATH = os.path.join(CONFIG_FOLDER_PATH, "cherrynas.lock")
FTP_LOG_FILE_PATH = os.path.join(CONFIG_FOLDER_PATH, "ftp.log")

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.abspath(os.path.join(SCRIPT_PATH, os.path.pardir))
MODULE_PATH = os.path.join(ROOT_PATH, "cdaemon", "modules")

def create_config_folder():
  if not os.path.exists(CONFIG_FOLDER_PATH):
    os.makedirs(CONFIG_FOLDER_PATH)

def load_config():
  pass

create_config_folder()
load_config()
