import unittest
from lab_python_pt.factory.ShopFactory import \
    SportShopFactory, \
    ElectronicsShopFactory, \
    get_shop

factories = [[SportShopFactory(), 'SportShopFactory', 'SportShop'],
             [ElectronicsShopFactory(), 'ElectronicsShopFactory', 'ElectronicsShop']]


class TestsShopsFactory(unittest.TestCase):
    def test_create_factory(self):
        for j in range(1, 20):
            for factory in factories:
                with self.subTest(j=j, factory=factory):
                    self.assertEqual(factory[0].shop_factory_name, factory[1])
                    client = get_shop(factory[0], j)
                    self.assertEqual(client.id, j)
                    self.assertEqual(client.get_shop_name(), factory[2])


if __name__ == '__main__':
    unittest.main()
