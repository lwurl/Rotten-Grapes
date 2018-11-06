from _wine_database import _wine_database
import unittest

class TestWineDatabase(unittest.TestCase):
        """unit tests for python primer homework"""

        #@classmethod
        wdb = _wine_database()
        #wdb.load_all('data/wine_data.csv') #TODO COMMENT OUT AND AND PUT BACK IN INDIVIDUAL RESETS

        def reset_data(self):
                "reset data is required because we cannot promise an order of test case execution"
                # note that our load_all function clears all data in the system before reloading
                self.wdb.load_all("data/wine_data.csv")
        
        # these tests work already
        '''
        def test_get_wine(self):
                self.reset_data()
                wine = self.wdb.get_wine(28950)
                self.assertEquals(wine['title'], 'Citation 2004 Pinot Noir (Oregon)')
                self.assertEquals(wine['variety'], 'Pinot Noir')

        def test_get_wine_null(self):
                self.reset_data()
                wine = self.wdb.get_wine(-1)
                self.assertEquals(wine, None)
        
        def test_set_wine(self):
                self.reset_data()
                wine = self.wdb.get_wine(28950)
                wine['title'] = 'youve been tested!'
                self.wdb.set_wine(28950, wine)
                wine = self.wdb.get_wine(28950)
                self.assertEquals(wine['title'], 'youve been tested!')

        def test_delete_wine(self):
                self.reset_data()
                self.wdb.delete_wine(28950)
                wine = self.wdb.get_wine(28950)
                self.assertEquals(wine, None)
        
        def test_get_user(self):
                self.reset_data()
                user = self.wdb.get_user(15)
                self.assertEquals(user['name'], 'Roger Voss')
                self.assertEquals(user['twitter'], '@vossroger')

        def test_set_user(self):
                self.reset_data()
                user = self.wdb.get_user(15)
                user['name'] = 'Mr. Test'
                user['twitter'] = '@mrtesty'
                self.wdb.set_user(15, user)
                user = self.wdb.get_user(15)
                self.assertEquals(user['name'], 'Mr. Test')
                self.assertEquals(user['twitter'], '@mrtesty')

        def test_delete_user(self):
                self.reset_data()
                self.wdb.delete_user(15)
                user = self.wdb.get_user(15)
                self.assertEquals(user, None)
        
        def test_get_review(self):
                self.reset_data()
                review = self.wdb.get_review(9, 79521)
                score = review['score']
                descrip = review['description']
                self.assertEquals(score, 87)
                self.assertEquals(descrip, "Aromas include tropical fruit, broom, brimstone and dried herb. The palate isn't overly expressive, offering unripened apple, citrus and dried sage alongside brisk acidity.")
        
        
        def test_get_variety_review(self):
                self.reset_data()
                review = self.wdb.get_variety_review(690)
                self.assertEquals(review['featured_wines'][0]['score'], 97)
                self.assertEquals(review['average_rating'], 87.35296610169492)
                self.assertEquals(review['variety'], "White Blend")
        
        '''
        
        
        
        # these are shreyas old tests
        '''
        def test_set_user_movie_rating_1(self):
                self.reset_data()
                self.mdb.set_user_movie_rating(41, 787, 2)
                rating = self.mdb.get_rating(787)
                self.assertEquals(rating, 4.25)

        def test_set_user_movie_rating_2(self):
                self.reset_data()
                self.mdb.set_user_movie_rating(41, 787, 2)
                self.mdb.set_user_movie_rating(101, 787, 4)
                rating = self.mdb.get_rating(787)
                self.assertEquals(rating, 4.2)

        def test_set_and_get_movie_ratings(self):
                self.reset_data()
                self.mdb.set_user_movie_rating(41, 787, 2)
                self.mdb.set_user_movie_rating(101, 787, 4)
                hrm_mid = self.mdb.get_highest_rated_movie()
                hrm_rating = self.mdb.get_rating(hrm_mid)
                hrm = self.mdb.get_movie(hrm_mid)
                hrm_name = hrm[0]
                self.assertEquals(hrm_mid, 989)
                self.assertEquals(hrm_name, 'Schlafes Bruder (Brother of Sleep) (1995)')
                self.assertEquals(hrm_rating, 5.0)

        def test_get_user_movie_rating(self):
                self.reset_data()
                rating = self.mdb.get_user_movie_rating(6030, 32)
                self.assertEquals(rating, 5)
        '''
if __name__ == "__main__":
    unittest.main()

