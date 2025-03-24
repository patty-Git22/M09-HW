import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self): 
        test_object = BookLover("Brom", "bsolo@movies.com", "scifi")
        test_object.add_book("Eragon", 4)
        self.assertTrue("Eragon" in test_object.book_list['book_name'].values)

    def test_2_add_book(self):
        test_object = BookLover("Frodo", "shire@onering.org", "scifi")
        test_object.add_book("Eragon", 4)
        self.assertEqual(test_object.book_list.shape[0], 1)

    def test_3_has_read(self): 
        test_object = BookLover("Luke", "luke2412@ymail.com", "scifi")
        test_object.add_book("Star Wars", 5)
        self.assertTrue(test_object.has_read("Star Wars"))

    def test_4_has_read(self): 
        test_object = BookLover("Obi-Wan Kenobi", "obiwan@temple.com", "scifi")
        test_object.add_book("Revenge of the Sith", 5)
        self.assertFalse(test_object.has_read("The Notebook"))

    def test_5_num_books_read(self): 
        test_object = BookLover("Chewbacca", "chewie@me.com", "scifi")
        test_object.add_book("The Force Awakens", 5)
        test_object.add_book("The Last Jedi", 4)
        self.assertEqual(test_object.num_books_read(), 2)

    def test_6_fav_books(self):
        test_object = BookLover("Patty", "bestmovies@aol.com", "anime")
        test_object.add_book("Demon Slayer: Kimetsu no Yaiba", 5)
        test_object.add_book("Berserk", 4)
        test_object.add_book("Black Clover",2)
        test_object.add_book("Solo Leveling",5)
        fav_books = test_object.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))
                
if __name__ == '__main__':
    unittest.main(verbosity=3)

