from distutils.core import setup

setup(
    name='SFTPClient',
    version='1.0.0',
    packages=('sftp_client', ),
    install_requires=('unit_conversion', ),
    url = '',
    license = '',
    author = 'Ian Davis',
    author_email = 'thekewlstore@gmail.com',
    description = "An API to make SFTP file transfers through chilkat simpler and more pythonic",
    )
