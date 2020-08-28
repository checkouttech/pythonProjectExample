from setuptools import setup

setup(
    name='helloworld',
    version='0.1',
    license='BSD',
    author='gyeh',
    author_email='hello@world.com',
    url='http://www.hello.com',
    long_description="README.txt",
    packages=['helloworld', 'helloworld.images'],
    include_package_data=True,
    package_data={'helloworld.images' : ['hello.gif']},
    description="Hello World testing setuptools",
)





