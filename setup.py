from setuptools import setup, find_packages

setup(
    name='netsweeper',
    version='0.1.2',
    description='Python class to allow programmers to create easily your own net sweeper scripts.',
    author='Alexsandro Camargo',
    py_modules=['netsweeper'],
    author_email='alexx.files@gmail.com',
    download_url='https://github.com/alexx-files/netsweeper/archive/0.1.1.tar.gz',
    packages=find_packages(include=['exampleproject', 'exampleproject.*']),
    install_requires=[
        'ping3'
    ],
    python_requires='>=3'
)

