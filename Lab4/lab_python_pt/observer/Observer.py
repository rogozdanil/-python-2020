from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Shops(ABC):
    _SHOP_NAME = None

    def __init__(self, id, count=0):
        self._id = id
        self._count_new_items = count
        self._clients: List[Clients] = []

    @classmethod
    def get_shop_name(cls):
        return cls._SHOP_NAME

    @property
    def id(self):
        return self._id

    def attach(self, client: Clients) -> None:
        print('{} {}: Attached an observer = {} {}'.format(self._SHOP_NAME, self._id, client.get_client_name(),
                                                           client.id))
        self._clients.append(client)

    def detach(self, client: Clients) -> None:
        print('{} {}: Detached an observer = {} {}'.format(self._SHOP_NAME, self._id, client.get_client_name(),
                                                           client.id))
        self._clients.remove(client)

    def notify(self) -> None:
        print('{} {}: {} observers'.format(self._SHOP_NAME, self._id, len(self._clients)))
        if len(self._clients) != 0:
            print('{} {}: Notifying observers...'.format(self._SHOP_NAME, self._id))
            for client in self._clients:
                client.update(self)

    @abstractmethod
    def business_logic(self) -> None:
        pass

    @property
    def count_new_items(self):
        return self._count_new_items

    @property
    def clients(self):
        return self._clients


class SportShop(Shops):
    _SHOP_NAME = 'SportShop'

    def business_logic(self) -> None:
        if self._count_new_items == 0:
            self._count_new_items = randrange(0, 10)

        print('\n{} {}: I received {} new items'.format(self._SHOP_NAME, self._id, self._count_new_items))

        self.notify()


class ElectronicsShop(Shops):
    _SHOP_NAME = 'ElectronicsShop'

    def business_logic(self) -> None:
        if self._count_new_items == 0:
            self._count_new_items = randrange(0, 15)

        print('\n{} {}: I received {} new items'.format(self._SHOP_NAME, self._id, self._count_new_items))

        self.notify()


class Clients(ABC):
    _CLIENT_NAME = None

    def __init__(self, id):
        self._id = id
        self._go_to_shop = False

    @classmethod
    def get_client_name(cls):
        return cls._CLIENT_NAME

    @abstractmethod
    def update(self, shop: Shops) -> None:
        pass

    @property
    def id(self):
        return self._id

    @property
    def go_to_shop(self):
        return self._go_to_shop


class SportShopClient(Clients):
    _CLIENT_NAME = 'SportShopClient'

    def update(self, shop: Shops) -> None:
        self._go_to_shop = False
        if shop.count_new_items >= 5:
            print('{} {}: Reacted to the event'.format(self._CLIENT_NAME, self._id))
            self._go_to_shop = True


class ElectronicsShopClient(Clients):
    _CLIENT_NAME = 'ElectronicsShopClient'

    def update(self, shop: Shops) -> None:
        self._go_to_shop = False
        if shop.count_new_items >= 7:
            print('{} {}: Reacted to the event'.format(self._CLIENT_NAME, self._id))
            self._go_to_shop = True


class SportElectronicsShopClient(Clients):
    _CLIENT_NAME = 'SportElectronicsShopClient'

    def update(self, shop: Shops) -> None:
        self._go_to_shop = False
        if shop.count_new_items >= 5 and shop.get_shop_name() == 'SportShop':
            print('{} {}: Reacted to the event'.format(self._CLIENT_NAME, self._id))
            self._go_to_shop = True

        if shop.count_new_items >= 7 and shop.get_shop_name() == 'ElectronicsShop':
            print('{} {}: Reacted to the event'.format(self._CLIENT_NAME, self._id))
            self._go_to_shop = True
