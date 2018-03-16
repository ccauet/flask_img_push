import os
from setuptools import setup

setup(
    name='push-it-to-the-limit',
    url='https://github.com/ccauet/push-it-to-the-limit',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3 :: Only',
    ],
    packages=['pittl'],
    entry_points={
        'console_scripts': [
            'pittl = pittl.cli:main',
        ]
    },
    package_data={
        'pittl': ['templates/html/*']
    },
    install_requires=[
        'tqdm',
        'click',
        'pendulum',
        'jinja2',
        'falcon'
    ],
)
