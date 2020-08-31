    # python3 
  
    sudo yum install -y python3

    sudo python3 -m pip install configparser


    pyline 
    pytest-cov


    run after installation pip 





tests/context.py 

```
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sample
```










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
-- sudo yum install -y python3
sudo yum install -y python3
sudo yum install -y python3.7
sudo yum install -y python37
-- yum install -y python3
-- yum install -y python3





[flake8]
exclude =
    .git,
    __pycache__,
    .pytest_cache,
    venv

ignore =
    # Put Error/Style codes here e.g. H301

max-line-length = 120
max-complexity = 10

[bandit]
targets: blueprint

[coverage:run]
branch = True
omit =
    */__main__.py
    */tests/*
    */venv/*

[coverage:report]
exclude_lines =
    pragma: no cover
    if __name__ == .__main__.:

[coverage:html]
directory = reports

[pylint]
...  # 100 lines of config...





pytest-picked

pytest-instafail
pytest-tldr










