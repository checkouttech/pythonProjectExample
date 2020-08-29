 
import sys
sys.path.append("./")



import pprint
import sys
pprint.pprint(sys.path)



import pytest 
from project_A.multiplyExample import multiply 



import pytest
 
 
 
 
 
 
def test_raises_exception():
 
    """ This example tests mult() with only one input factor """
 
    with pytest.raises(TypeError):
 
        multiply(3)



