from setuptools import setup, find_packages

setup(
    name='netsweeper',
    version='0.1',
    description='Python class to allow programmers to create easily your own net sweeper scripts.',
    author='Alexsandro Camargo',
    author_email='alexx.files@gmail.com',
    packages=find_packages(include=['exampleproject', 'exampleproject.*']),
    install_requires=[
        'ping3'
    ],
    python_requires='>=3'
)
