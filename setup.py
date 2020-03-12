from setuptools import setup
from glob import glob

package_name = 'odroid_ups'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    keywords=['Mighty Thymio'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='A minimal ROS driver for the Odroid UPS',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ups = odroid_ups.ups_node:main',
        ],
    },
)
