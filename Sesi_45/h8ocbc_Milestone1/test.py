import unittest
import requests
import config

from director import read_all as d_read_all, read_one as d_read_one
from movie import read_all as m_read_all, read_one as m_read_one

connex_app = config.connex_app

class TestDirector(unittest.TestCase):
    '''
    testing if the read_all() method return a list or not
    '''
    def test_read_all(self):
        self.assertIs(type(d_read_all()), list)

    '''
    testing if the read_one() method of the director_id 4762 is a dict or not
    '''    
    def test_read_one(self):
        self.assertIs(type(d_read_one(4762)), dict)

    def test_director_response_read_all(self):
        r = requests.get('http://localhost:5000/api/director')
        self.assertEqual(r.status_code, 200)

    def test_movie_read_one(self):
        self.assertIs(type(m_read_one(4762, 48400)), dict)

    def test_movie_response_read_all(self):
        r = requests.get('http://localhost:5000/api/movie')
        self.assertEqual(r.status_code, 200)
    

if __name__ == '__main__':
    unittest.main()