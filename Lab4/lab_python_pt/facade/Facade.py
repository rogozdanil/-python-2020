from __future__ import annotations
from lab_python_pt.factory.ShopFactory import SportShopFactory, ElectronicsShopFactory, get_shop
from lab_python_pt.factory.ClientFactory import SportShopClientFactory, ElectronicsShopClientFactory, \
    SportElectronicsShopClientFactory, get_client


class Facade:

    def __init__(self, sport_shops=None,
                 electronics_shops=None,
                 sport_shop_clients=None,
                 electronics_shop_clients=None,
                 sport_electronics_shop_clients=None):
        if sport_electronics_shop_clients is None:
            sport_electronics_shop_clients = []
        if electronics_shop_clients is None:
            electronics_shop_clients = []
        if sport_shop_clients is None:
            sport_shop_clients = []
        if electronics_shops is None:
            electronics_shops = []
        if sport_shops is None:
            sport_shops = []
        self.__sport_shops = sport_shops
        self.__electronics_shops = electronics_shops
        self.__sport_shop_clients = sport_shop_clients
        self.__electronics_shop_clients = electronics_shop_clients
        self.__sport_electronics_shop_clients = sport_electronics_shop_clients

    @property
    def sport_shops(self):
        return self.__sport_shops

    @property
    def electronics_shops(self):
        return self.__electronics_shops

    @property
    def sport_shop_clients(self):
        return self.__sport_shop_clients

    @property
    def electronics_shop_clients(self):
        return self.__electronics_shop_clients

    @property
    def sport_electronics_shop_clients(self):
        return self.__sport_electronics_shop_clients

    def sport_shop_business_logic(self):
        print('Sport shop business logic:')
        for i in range(0, len(self.__sport_shops)):
            self.__sport_shops[i].business_logic()
        print('\n')

    def electronic_shop_business_logic(self):
        print('Electronics shop business logic:')
        for i in range(0, len(self.__electronics_shops)):
            self.__electronics_shops[i].business_logic()
        print('\n')

    def create_shops(self, sport_shop_count, electronics_shops_count):
        print('Factory shops:')
        self.__create_shops('sport',
                            self.__sport_shops,
                            sport_shop_count,
                            SportShopFactory())

        self.__create_shops('electronics',
                            self.__electronics_shops,
                            electronics_shops_count,
                            ElectronicsShopFactory())

        print('\n')

    def create_clients(self,
                       sport_shop_clients_count,
                       electronics_shop_clients_count,
                       sport_electronics_shop_clients_count):

        print('\nFactory clients:')
        self.__create_clients('sport',
                              self.__sport_shop_clients,
                              sport_shop_clients_count,
                              SportShopClientFactory())

        self.__create_clients('electronics',
                              self.__electronics_shop_clients,
                              electronics_shop_clients_count,
                              ElectronicsShopClientFactory())

        self.__create_clients('sport electronics',
                              self.__sport_electronics_shop_clients,
                              sport_electronics_shop_clients_count,
                              SportElectronicsShopClientFactory())

        print('\n')

    def attach_clients(self):
        print('Observer attach:')
        self.__attach_clients('sport',
                              self.__sport_shops,
                              self.__sport_shop_clients)

        self.__attach_clients('electronics',
                              self.__electronics_shops,
                              self.__electronics_shop_clients)

        self.__attach_clients('sport electronics',
                              self.__sport_shops,
                              self.__sport_electronics_shop_clients)

        self.__attach_clients('sport electronics',
                              self.__electronics_shops,
                              self.__sport_electronics_shop_clients)

        print('\n')

    def detach_clients(self):
        print('Observer detach:')
        self.__detach_clients('sport',
                              self.__sport_shops,
                              self.__sport_shop_clients)

        self.__detach_clients('electronics',
                              self.__electronics_shops,
                              self.__electronics_shop_clients)

        self.__detach_clients('sport electronics',
                              self.__sport_shops,
                              self.__sport_electronics_shop_clients)

        self.__detach_clients('sport electronics',
                              self.__electronics_shops,
                              self.__sport_electronics_shop_clients)
        print('\n')

    def __create_shops(self, str, shops_list, count, factory):
        print('\nCreate {} {} shops:'.format(count, str))
        for i in range(0, count):
            shops_list.append(get_shop(factory, i))

    def __create_clients(self, str, clients_list, count, factory):
        print('\nCreate {} {} shop clients:'.format(count, str))
        for i in range(0, count):
            clients_list.append(get_client(factory, i))

    def __attach_clients(self, str, shop_list, clients_list):
        print('\nAttach {} {} shop clients:'.format(len(clients_list), str))
        for i in range(0, len(shop_list)):
            for j in range(0, len(clients_list)):
                shop_list[i].attach(clients_list[j])

    def __detach_clients(self, str, shop_list, clients_list):
        print('\nDetach {} {} shop clients:'.format(len(clients_list), str))
        for i in range(0, len(shop_list)):
            for j in range(0, len(clients_list)):
                shop_list[i].detach(clients_list[j])
