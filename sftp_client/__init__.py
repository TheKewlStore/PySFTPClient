# coding=utf-8
""" Script docstring.

Author: Ian Davis
Last Updated: 12/9/2015
"""

import os

from exceptions import *

from drivers.chilkat_client import ChilkatClient as SFTPClient


#if os.name == 'nt':
#    from drivers.chilkat_client import ChilkatClient as SFTPClient
#else:
#     from drivers.pexpect_client import PexpectClient as SFTPClient
