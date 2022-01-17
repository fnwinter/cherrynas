import os

HOME_PATH = os.path.expanduser('~')
CONFIG_FOLDER_PATH = os.path.join(HOME_PATH, '.cherrynas')
CONFIG_FILE_PATH = os.path.join(CONFIG_FOLDER_PATH, 'cherrynas.ini')
LOG_PATH = os.path.join(CONFIG_FOLDER_PATH, "cherrynas.log")
DAEMON_LOCK_PATH = os.path.join(CONFIG_FOLDER_PATH, "cherrynas.lock")

def create_config_folder():
  if not os.path.exists(CONFIG_FOLDER_PATH):
    os.makedirs(CONFIG_FOLDER_PATH)

def load_config():
  pass

create_config_folder()
load_config()
