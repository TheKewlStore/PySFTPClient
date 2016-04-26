# coding=utf-8
""" Module Docstring.

Author: Ian Davis
Last Updated: 12/9/2015
"""

import pexpect

from base import SFTPClient
from network.sftp.exceptions import SFTPError
from network.sftp.exceptions import SFTPTimeoutError


DOWNLOAD_COMMAND_TEMPLATE = 'scp -o ConnectTimeout=30 -o StrictHostKeyChecking=no -v {user}@{host}:{remote} {local}'
UPLOAD_COMMAND_TEMPLATE = 'scp -o ConnectTimeout=30 -o StrictHostKeyChecking=no -v {local} {user}@{host}:{remote}'


def command_succeeded(command_data):
    success_message = 'Exit status 0'
    lines = command_data.split('\n')[:-1]

    return any(success_message in line.strip() for line in lines)


class PexpectClient(SFTPClient):
    def _execute_scp_process(self, scp_command):
        scp_process = pexpect.spawn(scp_command, timeout=self.timeout)

        try:
            index_found = scp_process.expect(('assword:', 'yes/no'))
        except pexpect.EOF as err:
            raise SFTPTimeoutError(str(err))

        if index_found == 0:
            scp_process.sendline(self.password)
        elif index_found == 1:
            scp_process.sendline('yes')
            scp_process.expect('assword:')
            scp_process.sendline(self.password)

        scp_process.timeout = self.timeout
        command_data = scp_process.read()
        scp_process.close()

        if command_succeeded(command_data):
            return command_data
        else:
            raise SFTPError(command_data)

    def connect(self):
        pass

    def download(self, server_filepath, local_filepath):
        return self._execute_scp_process(DOWNLOAD_COMMAND_TEMPLATE.format(user=self.username,
                                                                          host=self.host,
                                                                          remote=server_filepath,
                                                                          local=local_filepath))

    def upload(self, server_filepath, local_filepath):
        return self._execute_scp_process(UPLOAD_COMMAND_TEMPLATE.format(user=self.username,
                                                                        host=self.host,
                                                                        remote=server_filepath,
                                                                        local=local_filepath))

    def list_directory(self, directory_path):
        pass
