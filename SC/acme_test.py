import unittest
from acme import Product
from acme_report import generate_products, adj, noun


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)


    def test_default_product_weight(self):
        '''Test default weight being 20'''
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)


    def test_default_product_flammability(self):
        '''Test default flammability being 0.5'''
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    
    def test_explode(self):
        '''Test explosiveness of product'''
        prod1 = Product('Test Product', flammability=0.01, weight=5)
        self.assertEqual(prod1.explode(), "...fizzle.")

        prod2 = Product('Test Product')
        self.assertEqual(prod2.explode(), "...boom!")

        prod3 = Product('Test Product', weight=100, flammability=.75)
        self.assertEqual(prod3.explode(), "...BABOOM!")


class AcmeReportTests(unittest.TestCase):
    '''Making sure Acme Reports are accuracte'''
    def test_default_num_products(self):
        '''Ensure default number is 30'''
        prod = generate_products()
        self.assertEqual(len(prod), 30)

    def test_legal_names(self):
        '''Ensure product names are valid'''
        prod = generate_products()
        for product in prod:
            name = product.name.split()
            self.assertIn(name[0], adj)
            self.assertIn(name[1], noun)



if __name__ == '__main__':
    unittest.main()
