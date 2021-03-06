from setuptools import setup, find_packages

setup(
    name='netsweeper',
    version='0.5.2',
    description='Python class to allow programmers to create easily your own net sweeper scripts.',
    long_description='Python class to allow programmers to create easily your own net sweeper scripts. '
                     'The examples added to the package already are net sweepers that can be used and improved.',
    author='Alexsandro Camargo',
    py_modules=['netsweeper'],
    author_email='alexx.files@gmail.com',
    download_url='https://github.com/alexx-files/netsweeper/archive/0.5.2.tar.gz',
    license='MIT',
    packages=find_packages(include=['exampleproject', 'exampleproject.*']),
    install_requires=[
        'ping3'
    ],
    keywords='net network sweeper netsweeper network scan ping icmp python3 pentest pentester tool',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Security',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3'
)

