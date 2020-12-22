import unittest
from lab_python_pt.factory.ClientFactory import \
    SportShopClientFactory, \
    ElectronicsShopClientFactory, \
    SportElectronicsShopClientFactory, \
    get_client

factories = [[SportShopClientFactory(), 'SportShopClientFactory', 'SportShopClient'],
             [ElectronicsShopClientFactory(), 'ElectronicsShopClientFactory', 'ElectronicsShopClient'],
             [SportElectronicsShopClientFactory(), 'SportElectronicsShopClientFactory', 'SportElectronicsShopClient']]


class TestsClientsFactory(unittest.TestCase):
    def test_create_factory(self):
        for j in range(1, 20):
            for factory in factories:
                with self.subTest(j=j, factory=factory):
                    self.assertEqual(factory[0].client_factory_name, factory[1])
                    client = get_client(factory[0], j)
                    self.assertEqual(client.id, j)
                    self.assertEqual(client.get_client_name(), factory[2])


if __name__ == '__main__':
    unittest.main()
