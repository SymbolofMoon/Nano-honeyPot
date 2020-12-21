from setuptools import setup


def readme_file_data():
    with open('README.rst') as readme_file:
        data=readme_file.read()

    return data




setup(
    name='nanoPot',
    version='1.0.0',
    description='Simple TCP Honeypot',
    long_description=readme_file_data(),
    author='Prateek',
    author_email= 'prateekchandra1027@gmail.com',
    license='MIT',
    packages=['nanopot'],
    #script=['bin/nanopot,'bin/nanopot.bat'],
    zip_safe=False,
    install_requires=[]

)    
