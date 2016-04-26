# coding=utf-8
""" Module Docstring.

Author: Ian Davis
Last Updated: 12/9/2015
"""

import chilkat

from base import SFTPClient

from network.sftp.exceptions import *


class ChilkatClient(SFTPClient, chilkat.CkSFtp):
    def __init__(self, host, username, password, timeout=None, license_key=None):
        SFTPClient.__init__(self, host, username, password, timeout=timeout)
        chilkat.CkSFtp.__init__(self)

        self.UnlockComponent(license_key)
        self.put_ConnectTimeoutMs(int(self.timeout))
        self.put_IdleTimeoutMs(int(self.timeout))

        self._connected = False

    def connect(self):
        success = self.Connect(self.host, 22)
        if not success:
            raise SFTPError(self.lastErrorText())

        success = self.AuthenticatePw(self.username, self.password)
        if not success:
            raise SFTPAuthenticationError(self.lastErrorText())

        success = self.InitializeSftp()
        if not success:
            raise SFTPError(self.lastErrorText())

        self._connected = True

    def download(self, server_filepath, local_filepath):
        if not self._connected:
            self.connect()

        handle = self.openFile(server_filepath, "readOnly", "openExisting")
        if not handle:
            raise SFTPError(self.lastErrorText())

        success = self.DownloadFile(handle, local_filepath)
        if not success:
            raise SFTPDownloadError(self.lastErrorText())

        success = self.CloseHandle(handle)
        if not success:
            raise SFTPError(self.lastErrorText())

    def upload(self, server_filepath, local_filepath):
        if not self._connected:
            self.connect()

        handle = self.openFile(server_filepath, "writeOnly", "createTruncate")
        if not handle:
            raise SFTPError(self.lastErrorText())

        success = self.UploadFile(handle, local_filepath)
        if not success:
            raise SFTPUploadError(self.lastErrorText())

        success = self.CloseHandle(handle)
        if not success:
            raise SFTPError(self.lastErrorText())

    def list_directory(self, directory_path):
        if not self._connected:
            self.connect()

        handle = self.openDir(directory_path)
        if not handle:
            raise SFTPError(self.lastErrorText())

        listing = self.ReadDir(handle)
        if not listing:
            raise SFTPError(self.lastErrorText())

        number_directories = listing.get_NumFilesAndDirs()
        if not number_directories:
            raise SFTPError(self.lastErrorText())

        filenames = []

        for current_index in xrange(0, number_directories):
            file_object = listing.GetFileObject(current_index)
            filenames.append(file_object.filename())

        success = self.CloseHandle(handle)
        if not success:
            raise SFTPError(self.lastErrorText())

        return filenames
