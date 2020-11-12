from setuptools import setup

setup(
    name='battery_checker',
    version='1.0',
    packages=['battery_checker'],
    package_dir={'': '.'},
    url='',
    license='',
    author='code_byter',
    author_email='',
    description='Send low battery notifications in i3',
    entry_points={
        'console_scripts': ["battery_checker = battery_checker.__main__:main"]}
)
