

Execute  
 
    # from directory 
    python project_A/driver_A.py   --config conf/project_A.conf  --dataset_one b1_table --dataset_two b2_table --tag_name foobar


    # after installation 
    export PYTHONPATH=/usr/lib/python2.7/site-packages/project_A

    TODO 




Run Tests 
    # run all 
    python -m pytest

    # run tagged test 
    pytest –m client_a

    #To run parameterized test, need to install module 
    pip install parameterized

    # Generating HTML tests result
    pip install pytest-html
    pytest --html report.html

    # Nice output 
    pip install pytest-sugar
     


    # stand alone 
    pytest -v  --cov=fakebidder  --cov-report html  --cov-report xml --junitxml results.xml  --html=report.htm 

    # as part of setup.py 
    python setup.py test -a "-v  --cov=fakebidder   --cov-report html --cov-report xml --junitxml results.xml  --html=report.html"


    # coverage report 
    python -m pytest  --cov=project_A






   

Setup  :

   Draw tree command 
   ```find . -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g' ```

            test-setuptools
            |
            |____helloworld
            | |______init__.py
            | |____hello.py
            | |____images
            | | |______init__.py
            | | |____hello.gif
            |____MANIFEST.in
            |____README.txt
            |____setup.py


Build / Packaging 


    # Clean 
    python setup.py clean

    


    # Build RPM ( only on Linux box )
    ```
    python setup.py bdist_rpm
 
        python setup.py bdist_rpm --spec-only  
        python setup.py bdist_rpm --requires=python-bottle,supervisor,python-requests  --release=2
        python setup.py bdist_rpm --requires=python-bottle,supervisor,python-requests  --release=`git rev-list --count --first-parent HEAD`

        # Important : --python ensure the package portability to a regular python env
        python setup.py bdist_rpm  --python=&quot;/usr/bin/python&quot
    ```

    # Dry run of files 
    rpm -qpl  dist/project_A-0.15-1.noarch.rpm

    # Install RPM
    sudo yum install project_A-0.15-1.noarch.rpm

    # Check location of files installed 
    rpm -ql  project_A

    # install rpm locally 
    TODO - rpm  --install dist/project_A-0.15-1.noarch.rpm  -r /home/vagrant/foo2/build/pythonProjectExample/install_dir2/


    # Build Egg 
    python setup.py sdist

    # Install egg 
     pip install dist/project_A-0.15.tar.gz

    # Install egg in local directory 
    pip install dist/project_A-0.15.tar.gz   -t install_dir/




    # tool needed to build rpm 
    sudo yum install rpm-build


    location -  /usr/lib/python2.7/site-packages/pythonBoilerplate/







TODO 
    # python3 
  
    sudo yum install -y python3

    sudo python3 -m pip install configparser


    pyline 
    pytest-cov


    run after installation pip 






Notes 
   Github commands 
   echo -n "$(git rev-parse --abbrev-ref HEAD)" ; echo -n "-" ; echo -n "$(git rev-list --count --first-parent HEAD)"







pytest-picked

pytest-instafail
pytest-tldr

```pylint --rcfile=pylint.cfg $(find handlers -maxdepth 1 -name "*.py" -print)  --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" > pylint.log || exit 0```







pip install allure-pytest
pip install configparse
pip install pip install allure-pytest
pip install pytest-allure-adaptor
pip install pytest-html pytest-sugar
pip install pytest-tldr
pip install python3
pip install python3.8
pip install setuptools
pip install --upgrade pip
pip install --upgrade  setuptools
pip install -U pytest
pip uninstall pytest-allure-adaptor
sudo pip install allure-pytest
sudo pip install configparse
sudo pip install pytest-tldr
sudo pip install setuptools
sudo pip install --upgrade pip
sudo pip install wheel
sudo python3 -m pip install configparser
sudo yum install epel-release
sudo yum install python-pip
# sudo yum install -y python3
sudo yum install -y python3
sudo yum install -y python3.7
sudo yum install -y python37
yum install -y python3
yum install -y python3


