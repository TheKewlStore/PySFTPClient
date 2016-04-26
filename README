# PySFTPClient
Cross-platform SFTP client API aimed at making a more pythonic wrapper around the chilkat sftp library.

Requirements:
chilkat python library

Note: The PySFTPClient requires a license key to the chilkat python library, otherwise, you can use the chilkat trial for 30 days as normal.

Basic usage example::

    from sftp_client import SFTPClient

    with SFTPClient(host, username, password, license_key='license_key') as client:
        client.download('./server_path.txt', '~/local_path.txt')
        client.upload('./server_path2.txt', ~/local_path.txt)
        print client.list_directory('./')

