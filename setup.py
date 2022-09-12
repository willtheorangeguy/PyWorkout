from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
	name='pyworkout',
	version='1.2.0',
    description='A minimal CLI to keep you inspired during your workout! ',
    long_description=readme(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Other/Nonlisted Topic',
    ],
    keywords='workout plan tracking tracker video cli',
    url='https://github.com/Dog-Face-Development/PyWorkout',
    author='willtheorangeguy',
    py_modules = ['main'],
    entry_points={
        'console_scripts': [
            'pyworkout=main:workout'
        ]
    },
)
