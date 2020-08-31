
Notes 
   Github commands 
   echo -n "$(git rev-parse --abbrev-ref HEAD)" ; echo -n "-" ; echo -n "$(git rev-list --count --first-parent HEAD)"




```pylint --rcfile=pylint.cfg $(find handlers -maxdepth 1 -name "*.py" -print)  --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" > pylint.log || exit 0```





To create virtualenv for installation 

    $  sudo easy_install pip 
    $  pip list 
    $  pip install virtualenv --upgrade                
    $  /usr/local/bin/virtualenv-2.7 env
    $  source env/bin/activate


Installation : 

    $  (env):$  pip install  /tmp/foo/helloworld-0.1.tar.gz 


Check : 

    $ env/bin/python 
    
    >>> import helloworld
    >>> dir(helloworld.hello)
    >>> hey = helloworld.hello.Hello()
    >>> hey.say_hello()



