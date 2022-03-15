# Copyright 2019 fnwinter@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import copy
import os
import re

from config.default import DEFAULT_CONFIG
from config import CONFIG_FOLDER_PATH, INI_FILE_PATH
from utils.path import make_sure_path
from utils.log import get_logger

class Config():
    """
    Read and write config data to file.
    """
    def __init__(self, file_path=INI_FILE_PATH, open_mode='r'):
        """
        open config file
        >>> from config import TEST_CONFIG_READ_PATH
        >>> with Config(TEST_CONFIG_READ_PATH) as c:
        ...     TEST_CONFIG_READ_PATH == c.config_file.name
        True
        >>> try:
        ...     with Config("not_exist_file") as c:
        ...         print("")
        ... except Exception as e:
        ...         print(e)
        config file path is wrong
        """
        make_sure_path(CONFIG_FOLDER_PATH)

        if not os.path.exists(file_path):
            assert False, "config file path is wrong"

        self.config_file = open(file_path, open_mode)

        self.log = get_logger('config')
        self.re_section = re.compile(r'\[(.*)\]')
        self.re_key_section = re.compile(r'([a-zA-Z\d]*)_([a-zA-Z\d_]*)')
        self.re_key_value = re.compile(r'(.*)=(.*)')
        self.config_data = copy.copy(DEFAULT_CONFIG)
        if open_mode == 'r':
            self._read_config()

    def __del__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, _type, _value, _traceback):
        self.close()

    def close(self):
        """ close config file """
        if self.config_file:
            self.config_file.close()

    def _read_config(self):
        """
        read config file and set data to self.config_data
        """
        lines = self.config_file.readlines()
        section_name = None
        for line in lines:
            _section = self._get_section(line)
            if _section:
                section_name = _section
                continue

            key_value = self.re_key_value.match(line)
            if section_name and key_value:
                _key, _value = self._get_key_value(line)
                if _key and _value:
                    section_key = '%s_%s' % (section_name, _key)
                    value = Config.typed_value(section_key, _value)
                    self.config_data[section_key] = value
                    self.log.info("read config [%s %s], %s",
                                  section_key, value, type(value).__name__)

    @staticmethod
    def typed_value(key, value):
        _t = type(DEFAULT_CONFIG.get(key, ""))
        # bool value
        if _t.__name__ == 'bool':
            if value.lower() == 'true':
                return True
            if value.lower() == 'false':
                return False
            return False
        # string
        return value

    def get_config_data(self):
        """ return get_config_data """
        return self.config_data

    def _get_section(self, line):
        """
        return section name
        >>> from config import TEST_CONFIG_READ_PATH
        >>> with Config(TEST_CONFIG_READ_PATH, 'r') as c:
        ...     print(c._get_section('[SECTION ]'))
        ...     print(c._get_section('SECTION'))
        SECTION
        None
        >>>
        """
        section = self.re_section.match(line)
        if section:
            return section.group(1).strip()
        return None

    def _get_key_value(self, key_value):
        """
        return key and value from config string
        >>> from config import TEST_CONFIG_READ_PATH
        >>> with Config(TEST_CONFIG_READ_PATH, 'r') as c:
        ...     print(c._get_key_value('KEY=VALUE'))
        ...     print(c._get_key_value('KEY1= VALUE1'))
        ...     print(c._get_key_value('KEY1VALUE1'))
        ('KEY', 'VALUE')
        ('KEY1', 'VALUE1')
        (None, None)
        """
        match = self.re_key_value.match(key_value)
        if match:
            _key = match.group(1).strip()
            _val = match.group(2).strip()
            return _key, _val
        return None, None

    def _get_section_key(self, key):
        """
        return section and key from key name
        >>> from config import TEST_CONFIG_READ_PATH
        >>> with Config(TEST_CONFIG_READ_PATH, 'r') as c:
        ...     print(c._get_section_key('KEY_ VALUE'))
        ...     print(c._get_section_key('KEY1_VALUE1 '))
        ...     print(c._get_section_key('KEY1VALUE1'))
        ...     print(c._get_section_key('KEY1_VALUE1_TEST2'))
        ('KEY', '')
        ('KEY1', 'VALUE1')
        (None, None)
        ('KEY1', 'VALUE1_TEST2')
        """
        try:
            _match = self.re_key_section.match(key)
            if _match:
                _section = _match.group(1).strip()
                _key = _match.group(2).strip()
                return _section, _key
        except Exception as e:
            self.log.error('_get_section_key %s', e)
        return None, None

    def write_config(self, config_data):
        """
        write config file in self.config_data
        >>> from config import TEST_CONFIG_WRITE_PATH
        >>> with Config(TEST_CONFIG_WRITE_PATH, 'w') as c:
        ...     config_data = {
        ...         'FTP_ADDRESS' : '127.0.0.1',
        ...         'FTP_ACCOUNT': 'ADMIN',
        ...         'ACCOUNT_ID': 'TEST@CHERRYNAS.COM'
        ...     }
        ...     c.write_config(config_data)
        >>> with Config(TEST_CONFIG_WRITE_PATH, 'r') as c:
        ...     print(c.get_value('FTP', 'ADDRESS'))
        ...     print(c.get_value('FTP', 'ACCOUNT'))
        ...     print(c.get_value('ACCOUNT', 'ID'))
        127.0.0.1
        ADMIN
        TEST@CHERRYNAS.COM
        """
        self.config_data = config_data
        self.config_file.write("# DO NOT MODIFY THIS FILE MANUALLY #\n")
        keys = sorted(self.config_data)
        previous_section = None
        for k in keys:
            value = self.config_data.get(k)
            _section, _key = self._get_section_key(k)
            if _section and previous_section != _section:
                new_section = '\n[%s]\n' % _section
                self.config_file.write(new_section)
                previous_section = _section
            data = '%s=%s\n' % (_key, value)
            self.config_file.write(data)

    def get_value(self, section, key, default=''):
        """
        get value by section/key
        >>> from config import TEST_CONFIG_READ_PATH
        >>> with Config(TEST_CONFIG_READ_PATH, 'r') as c:
        ...     print(c.get_value('TEST', 'GET_VALUE1'))
        ...     print(c.get_value('TEST', 'GET_VALUE2'))
        ...     print(c.get_value('TEST', 'GET_VALUE3'))
        ...     print(c.get_value('TEST', 'GET_VALUE4', 'default'))
        0
        test
        None
        default
        """
        _key = "%s_%s" % (section, key)
        return self.config_data.get(_key, default)

    def get_int_value(self, section, key):
        """
        get int value by section/key
        >>> from config import TEST_CONFIG_READ_PATH
        >>> with Config(TEST_CONFIG_READ_PATH, 'r') as c:
        ...     print(c.get_int_value('TEST', 'INT_VALUE'))
        10
        """
        try:
            return int(self.get_value(section, key))
        except ValueError as ve:
            self.log.error('get_int_value %s %s', key, ve)
        except TypeError as te:
            self.log.error('get_int_value %s %s', key, te)
        return 0

    def get_tuple_value(self, section, key):
        """
        get tuple value
        >>> from config import TEST_CONFIG_READ_PATH
        >>> with Config(TEST_CONFIG_READ_PATH, 'r') as c:
        ...     print(c.get_tuple_value('TEST', 'TUPLE_VALUE'))
        (1, 2)
        """
        try:
            tuple_str = self.get_value(section, key, '')
            if len(tuple_str) != 0:
                return tuple(map(int, tuple_str.split(',')))
        except Exception as e:
            self.log.error('get_tuple_value : %s', e)
        return ()
