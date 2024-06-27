from setuptools import find_packages, setup

package_name = 'movingbox_gps'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='movingbox',
    maintainer_email='movingbox@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "gps_sender = movingbox_gps.gps_sender:main",
            "test_sub = movingbox_gps.test_sub:main"
        ],
    },
)
