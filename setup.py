from setuptools import setup, find_packages

setup(
    name='netsweeper',
    version='0.1.23',
    description='Python class to allow programmers to create easily your own net sweeper scripts.',
    long_description='Python class to allow programmers to create easily your own net sweeper scripts. '
                     'The examples added to the package already are net sweepers that can be used and improved',
    author='Alexsandro Camargo',
    py_modules=['netsweeper'],
    author_email='alexx.files@gmail.com',
    download_url='https://github.com/alexx-files/netsweeper/archive/0.1.23.tar.gz',
    packages=find_packages(include=['exampleproject', 'exampleproject.*']),
    install_requires=[
        'ping3'
    ],
    keywords='net sweeper netsweeper network scan ping icmp python3',
    python_requires='>=3'
)

