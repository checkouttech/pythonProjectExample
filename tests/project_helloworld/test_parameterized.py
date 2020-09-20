from parameterized import parameterized
import pytest 

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output



@parameterized.expand(['autorepr', 'django-nose', 'chai-subset'])
def test_repos_existence_in_wolever_profile(self, repo):
    api_url = 'https://api.github.com/users/wolever/repos'
    response = requests.get().json(api_url)
    self.assertIn(repo, [item['name'] for item in response])


@pytest.mark.parametrize(
    "test_input,expected",
    [("3+5", 8), ("2+4", 6), pytest.param("6*9", 42, marks=pytest.mark.xfail)],
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected






@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    pass





testdata = [(1,0),(2,2),(6,3),(24,4)]

@pytest.mark.parametrize("factorial,number",testdata )
def test_factorial(factorial,number ) :
    

    fact = 1 

    if number < 0:
        fact = 0 
    elif (number == 1) or (number == 0) :
        fact = 1 
    else :
        for i in range ( 1, number+1 ): 
            fact = fact * i 

    assert factorial == fact  



