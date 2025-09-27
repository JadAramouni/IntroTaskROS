from setuptools import setup

package_name = 'py_talk'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jad',
    maintainer_email='j4.aramouni@gmail.com',
    description='Python pub/sub example',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'py_pub = py_talk.py_pub:main',
            'py_sub = py_talk.py_sub:main',
        ],
    },
)
