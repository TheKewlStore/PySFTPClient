from setuptools import setup

setup(
    name='sftp_client',
    version='1.0.4',
    packages=('sftp_client', 'sftp_client.drivers'),
    install_requires=['unit_conversion', ],
    url = 'https://github.com/TheKewlStore/PySFTPClient',
    license = '',
    author = 'Ian Davis',
    author_email = 'thekewlstore@gmail.com',
    description = "An API to make SFTP file transfers through chilkat simpler and more pythonic",
    )
