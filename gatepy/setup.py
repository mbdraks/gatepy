from setuptools import setup, find_packages

setup(
    name='gatepy',
    version='1.2.0',
    description='FortiGate Automation using REST API',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='fortinet fortigate fortios',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
)