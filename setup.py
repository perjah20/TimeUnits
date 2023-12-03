from setuptools import setup, find_packages

setup(
    name='timeunits',
    version='0.1.0',
    author='Per Jahnstedt',
    author_email='per.olof.jahnstedt@gmail.com',
    description='A Python library for working with and converting between various time units.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/perjah20/TimeUnits',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: Attribution License',  # Replace with your license
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.7',
    install_requires=[
        # Currently, no dependencies
    ],
    extras_require={
        # Currently, no dependencies
    },
)
