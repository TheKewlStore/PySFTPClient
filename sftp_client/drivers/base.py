# coding=utf-8
""" Module Docstring.

Author: Ian Davis
Last Updated: 12/9/2015
"""

from shared.util import unit_conversion


class SFTPClient(object):
    def __init__(self, host, username, password, timeout=None):
        self.host = host
        self.username = username
        self.password = password
        self.timeout = timeout

        if not self.timeout:
            self.timeout = 15000

        self.timeout = unit_conversion.milliseconds(self.timeout, base=unit_conversion.SECOND)

    def connect(self):
        raise NotImplementedError('Abstract base method.')

    def download(self, server_filepath, local_filepath):
        raise NotImplementedError('Abstract base method.')

    def upload(self, server_filepath, local_filepath):
        raise NotImplementedError('Abstract base method.')

    def list_directory(self, directory_path):
        raise NotImplementedError('Abstract base method.')

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return
