from setuptools import setup
from setuptools.command.test import test as TestCommand
from setuptools import setup, Command
import os
import subprocess
from subprocess import STDOUT, check_output


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        pytest.main(self.pytest_args)


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')


# module details
__name__ = 'project-A',


# add release here 
    # if creating outside git 

try:
    __release__   = subprocess.check_output(["git", "rev-list", "--count", "--first-parent", "HEAD"]).rstrip(),
except:
    __release__   = '0.0.4'

#release=subprocess.check_output(["git", "rev-list", "--count", "--first-parent", "HEAD"]).rstrip(),

requires = [
    'setuptools>=39.1'
]


setup(
    name             = 'project-A',
    #version         = __version__,
    version          = 0.15,
    #rel # ease          = '0.0.1',
    release          = __release__,
    license          = 'BSD',
    
    author           = 'foo bar',
    author_email     = 'hello@world.com',
    url              = 'http://www.hello.com',
    description      = 'A python boiler plate module',
    long_description = "README.txt",

    #zip_safe         = False,
 


    #install_requires=['bottle','requests','supervisor'],  # currently not working 

    install_requires = requires,

    packages         = ['project-A', 'project-A.lib'] , 

    package_dir      = { 'project-A' : 'project_A' ,  'project-A.lib' : 'lib'}  , 



    # release is not supported in bdist rpm
    #dependency_links = ['https://pypi.python.org/packages/source/b/bottle/bottle-0.12.8.tar.gz'],



    include_package_data=True,

    package_data={'images' : ['hello.gif']},

    data_files=[
                #('/etc/init.d/', ['project_Actl']),  # some startup script 
                ('/var/log/project_A',[]),
                ('/etc/project_A/conf/',['conf/project_A.conf'])
                ],

    tests_require=['pytest'],

    cmdclass = {
                'test': PyTest,
                'clean': CleanCommand
                }

)

