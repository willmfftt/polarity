from setuptools import setup

setup(
    name='polarity',
    version='0.1dev',
    packages=[
        'polarity',
        'polarity.bruteforce',
        'polarity.enumeration',
        'polarity.network_scanner',
        'polarity.objects',
        'polarity.utils',
    ],
    license='',
    author='William Moffitt',
    author_email='wmoffitt@cybrtalk.com',
    description='',
    entry_points={
        'console_scripts': [
            'polarity = polarity.__main__:main',
        ],
    },
    install_requires=[
        'argparse',
        'paramiko',
        'pysmb',
        'python-nmap',
    ],
    python_requires='~=3.6',
)
