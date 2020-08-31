
Notes 
   Github commands 
   echo -n "$(git rev-parse --abbrev-ref HEAD)" ; echo -n "-" ; echo -n "$(git rev-list --count --first-parent HEAD)"




```pylint --rcfile=pylint.cfg $(find handlers -maxdepth 1 -name "*.py" -print)  --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" > pylint.log || exit 0```






