import unittest
from lab_python_pt.facade.Facade import Facade

shops = ['SportShop', 'ElectronicsShop']
clients = ['SportShopClient', 'ElectronicsShopClient', 'SportElectronicsShopClient']


class TestsFacade(unittest.TestCase):
    def test_facade_create_shop(self):
        for i in range(1, 20):
            for j in range(1, 20):
                with self.subTest(i=i, j=j):
                    facade = Facade()
                    facade.create_shops(i, j)
                    sport_shops = facade.sport_shops
                    electronics_shops = facade.electronics_shops

                    for sp in sport_shops:
                        self.assertEqual(sp.get_shop_name(), shops[0])

                    for es in electronics_shops:
                        self.assertEqual(es.get_shop_name(), shops[1])

    def test_facade_create_clients(self):
        for i in range(1, 20):
            for j in range(1, 20):
                for k in range(1, 20):
                    with self.subTest(i=i, j=j, k=k):
                        facade = Facade()
                        facade.create_clients(i, j, k)
                        sport_shops_clients = facade.sport_shop_clients
                        electronics_shops_clients = facade.electronics_shop_clients
                        sport_electronics_shop_clients = facade.sport_electronics_shop_clients

                        for ssc in sport_shops_clients:
                            self.assertEqual(ssc.get_client_name(), clients[0])

                        for esc in electronics_shops_clients:
                            self.assertEqual(esc.get_client_name(), clients[1])

                        for sesc in sport_electronics_shop_clients:
                            self.assertEqual(sesc.get_client_name(), clients[2])


if __name__ == '__main__':
    unittest.main()
