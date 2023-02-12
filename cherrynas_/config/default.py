# Copyright 2019 fnwinter@gmail.com

DEFAULT_CONFIG = {
    # ADMIN
    'ADMIN_ID': 'admin@cherrynas.com',
    'ADMIN_PASSWORD': 'c775e7b757ede630cd0aa1113bd102661ab38829ca52a6422ab782862f268646',

    # ACCOUNT
    'ACCOUNT_EMAIL': 'admin@cherrynas',
    'ACCOUNT_PASSWORD': '1234567890',

    # FTP
    'FTP_ROOT_ENABLE': True,
    'FTP_ROOT_PATH': '/ftp/path/here',
    'FTP_ANONYMOUS_ENABLE': True,
    'FTP_ANONYMOUS_PATH': '/ftp/path/here',
    'FTP_PASSIVE_PORT': "60000, 65535",
    'FTP_ADDRESS': '127.0.0.1',
    'FTP_PORT': '21',
    'FTP_MAX_CONNECTION': '10',
    'FTP_MAX_CON_PER_IP': '2',
    'FTP_WELCOME_BANNER': '\nWelcome! cherrynas FTP server.\n',
}

def load_default(section):
    """
    >>> load_default('ACCOUNT').get('ACCOUNT_EMAIL')
    'admin@cherrynas'
    >>> load_default('FTP').get('FTP_ROOT_ENABLE')
    True
    """
    config = {}
    for d in DEFAULT_CONFIG:
        if section in d:
            config.update({d:DEFAULT_CONFIG.get(d)})
    return config
