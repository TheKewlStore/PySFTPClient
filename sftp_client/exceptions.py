# coding=utf-8
""" Module Docstring.

Author: Ian Davis
Last Updated: 12/9/2015
"""


class SFTPError(Exception):
    pass


class SFTPTimeoutError(SFTPError):
    pass


class SFTPAuthenticationError(SFTPError):
    pass


class SFTPDownloadError(SFTPError):
    pass


class SFTPUploadError(SFTPError):
    pass
