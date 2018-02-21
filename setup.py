from setuptools import setup

setup(
    name='polarity',
    version='0.1dev',
    packages=[
        'polarity',
        'polarity.bruteforce',
        'polarity.enumeration',
        'polarity.host_deployment',
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
        'jsonpickle',
        'paramiko',
        'pysmb',
        'python-nmap',
        'requests',
    ],
    python_requires='~=3.6',
)
