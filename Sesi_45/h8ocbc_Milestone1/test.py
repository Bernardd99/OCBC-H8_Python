import unittest
import requests
import config
from app import connex_app

from director import read_all as d_read_all, read_one as d_read_one
from movie import read_all as m_read_all, read_one as m_read_one

connex_app = config.connex_app

class TestDirector(unittest.TestCase):

    '''
    set up the test client to be reusable
    '''
    def setUp(self):
        connex_app.app.testing = True
        self.app = connex_app.app.test_client()

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


    '''
    testing if the url of /api/director return the correct response code when executed
    '''    
    def test_read_all_director(self):
        r = self.app.get('/api/director')
        self.assertEqual(r.status_code, 200)

    '''
    testing if the url of /api/movie return the correct response code when executed
    '''        
    def test_read_all_movie(self):
        r = self.app.get('/api/movie')
        self.assertEqual(r.status_code, 200)

    '''
    testing if the director exist in the director list
    '''
    def test_read_one_director(self):
        r = self.app.get('/api/director/4762')        
        self.assertEqual(r.status_code, 200, "Not Found")

    '''
    testing if the director is not found in the director list
    '''
    def test_director_not_found(self):
        r = self.app.get('/api/director/3215421')   
        self.assertEqual(r.status_code, 404) 

    '''
    testing if the movie exist in the movie list
    '''
    def test_read_one_movie(self):
        r = self.app.get('/api/director/4762/movie/48400')        
        self.assertEqual(r.status_code, 200, "Not Found")

    '''
    testing if the movie is not found in the movie list
    '''
    def test_movie_not_found(self):
        r = self.app.get('/api/director/4762/movie/42324')   
        self.assertEqual(r.status_code, 404) 

    '''
    testing if the name of the director when the get proccess of director_id 4762 executed is correct
    '''
    def test_director_name(self):
        d = d_read_one(4762)
        self.assertEqual(d['name'], "James Cameron", "Name is incorrect")

    '''
    testing if the title of the movie when the get proccess of movie_id 48400 executed is correct
    '''
    def test_movie_title(self):
        m = m_read_one(4762, 48400)
        self.assertEqual(m['title'], "Testing", "Title Is Incorrect")

    

if __name__ == '__main__':
    unittest.main()