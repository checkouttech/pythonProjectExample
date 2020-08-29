
import sys
sys.path.append("./")



import pprint
import sys
pprint.pprint(sys.path)



import pytest 
from project_A.multiplyExample import multiply 



#from  multiplyExample import multiply 



def test_numbers_3_4():
    assert multiply(3,4) == 12

def test_numbers_0_4():
    assert multiply(0,4) == 4


def test_strings_a_3():
    assert multiply('a',3) == 'aaa'



