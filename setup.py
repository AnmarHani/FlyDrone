from setuptools import setup, find_packages

setup(
    name='flydrone',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/AnmarHani/PyDrone',
    license='MIT',
    author='Anmar Hani',
    install_requires=['pymavlink'],
    keywords=['python', 'drone', 'embedded', 'automation'],
    author_email='AnmarHaniV1@gmail.com',
    description='A simple basic drone python api that is built on top of pymavlink',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent'
    ]
)