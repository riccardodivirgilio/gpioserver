
from setuptools import setup, find_packages

# to publish:

# python3 setup.py sdist bdist_wheel && twine upload dist/*

setup(
    name = 'gpioserver',
    version = '1.0.4',
    description = 'A Python library to start a gpio server for your raspberry pi.',
    keywords=['Raspberry PI', 'GPIO', 'aiohttp', 'api'],
    author = 'Riccardo Di Virgilio',
    python_requires='>=3.5.3',
    packages=find_packages(),
    include_package_data=True,
    install_requires = [
        'aiohttp>=3.5.4',
    ],
    entry_points={
        'console_scripts': [
            'gpioserver = gpioserver.__main__:main',
        ]
    }
)
