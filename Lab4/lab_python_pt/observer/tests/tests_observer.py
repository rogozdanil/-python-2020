import unittest
from lab_python_pt.observer.Observer import \
    SportShop, \
    SportShopClient, \
    ElectronicsShop, \
    ElectronicsShopClient, \
    SportElectronicsShopClient

n = 10

observer_version = [[SportShop, SportShopClient, 5],
                    [ElectronicsShop, ElectronicsShopClient, 7],
                    [SportShop, SportElectronicsShopClient, 5],
                    [ElectronicsShop, SportElectronicsShopClient, 7]]


class TestObserver(unittest.TestCase):
    def test_observers(self):
        for j in range(1, 20):
            for obs in observer_version:
                with self.subTest(j=j, obs=obs):
                    shop = obs[0](0, j)
                    shop_clients = []
                    for i in range(0, n):
                        shop_clients.append(obs[1](i))

                    for i in range(0, n):
                        shop.attach(shop_clients[i])

                    shop.business_logic()

                    for i in range(0, n):
                        if j < obs[2]:
                            self.assertEqual(shop_clients[i].go_to_shop, False)
                        else:
                            self.assertEqual(shop_clients[i].go_to_shop, True)

                    for i in range(0, n):
                        shop.detach(shop_clients[i])


if __name__ == '__main__':
    unittest.main()
