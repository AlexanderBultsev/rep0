from DBRequests import *
import unittest

class TestDB(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect('Databases/TestCopyDB1.db')
        self.cursor = self.conn.cursor()

    def tearDown(self):
        self.conn.close()

    def test_ProductsOfRarity(self):
        for Product in ProductsOfRarity(self.cursor, 'Arcana'):
            self.assertEqual(Product[2], 'Arcana')
    
    def test_wrong_ProductsOfRarity(self):
        for Product in ProductsOfRarity(self.cursor, 'Arcana'):
            self.assertEqual(Product[2], 'None', 'Должно выдать ошибку неравенства')

    def test_ProductsOfHero(self):
        for Product in ProductsOfHero(self.cursor, 'Pudge'):
            self.assertEqual(Product[3], 'Pudge')

    def test_ProductsOfRarityAndHero(self):
        for Product in ProductsOfRarityAndHero(self.cursor, 'Pudge', 'Arcana'):
            self.assertEqual(Product[2], 'Arcana')
            self.assertEqual(Product[3], 'Pudge')

    def test_ProductsPriceBetween(self):
        Prc = [i for i in range(1000,1701)]
        for Product in ProductsPriceBetween(self.cursor, 1000, 1700):
            self.assertIn(Product[4], Prc)

    def test_ProductsSortedByRarityAndPrice(self):
        Prc = []
        minPrc = 999999
        for Product in ProductsSortedByRarityAndPrice(self.cursor):
            minPrc = min(minPrc, Product[4])
            Prc.append(Product[4])
        self.assertEqual(minPrc, Prc[0])


if __name__ == '__main__':
    unittest.main()