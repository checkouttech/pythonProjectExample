from parameterized import parameterized
import pytest 

@parameterized.expand(['autorepr', 'django-nose', 'chai-subset'])
def test_repos_existence_in_wolever_profile(self, repo):
    api_url = 'https://api.github.com/users/wolever/repos'
    response = requests.get().json(api_url)
    self.assertIn(repo, [item['name'] for item in response])




