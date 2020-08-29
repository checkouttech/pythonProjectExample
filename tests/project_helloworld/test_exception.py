 
import pytest
 
 
 
from sample_script import mult
 
 
 
def test_raises_exception():
 
    """ This example tests mult() with only one input factor """
 
    with pytest.raises(TypeError):
 
        mult(3)
In this example, we mus



