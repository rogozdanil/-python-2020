from __future__ import annotations
from abc import ABC, abstractmethod
from lab_python_pt.observer.Observer import Shops, SportShop, ElectronicsShop


class ShopFactory(ABC):
    _SHOP_FACTORY_NAME = None

    @abstractmethod
    def factory_method(self, id):
        pass

    @property
    def shop_factory_name(self):
        return self._SHOP_FACTORY_NAME


class SportShopFactory(ShopFactory):
    _SHOP_FACTORY_NAME = 'SportShopFactory'

    def factory_method(self, id) -> Shops:
        print('{}: Create new shop with id = {}'.format(self._SHOP_FACTORY_NAME, id))
        return SportShop(id)


class ElectronicsShopFactory(ShopFactory):
    _SHOP_FACTORY_NAME = 'ElectronicsShopFactory'

    def factory_method(self, id) -> Shops:
        print('{}: Create new shop with id = {}'.format(self._SHOP_FACTORY_NAME, id))
        return ElectronicsShop(id)


def get_shop(factory: ShopFactory, id):
    return factory.factory_method(id)
