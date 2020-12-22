from __future__ import annotations
from abc import ABC, abstractmethod
from lab_python_pt.observer.Observer import Clients, SportShopClient, ElectronicsShopClient, SportElectronicsShopClient


class ClientFactory(ABC):
    _CLIENT_FACTORY_NAME = None

    @abstractmethod
    def factory_method(self, id):
        pass

    @property
    def client_factory_name(self):
        return self._CLIENT_FACTORY_NAME


class SportShopClientFactory(ClientFactory):
    _CLIENT_FACTORY_NAME = 'SportShopClientFactory'

    def factory_method(self, id) -> Clients:
        print('{}: Create new client with id = {}'.format(self._CLIENT_FACTORY_NAME, id))
        return SportShopClient(id)


class ElectronicsShopClientFactory(ClientFactory):
    _CLIENT_FACTORY_NAME = 'ElectronicsShopClientFactory'

    def factory_method(self, id) -> Clients:
        print('{}: Create new client with id = {}'.format(self._CLIENT_FACTORY_NAME, id))
        return ElectronicsShopClient(id)


class SportElectronicsShopClientFactory(ClientFactory):
    _CLIENT_FACTORY_NAME = 'SportElectronicsShopClientFactory'

    def factory_method(self, id) -> Clients:
        print('{}: Create new client with id = {}'.format(self._CLIENT_FACTORY_NAME, id))
        return SportElectronicsShopClient(id)


def get_client(factory: ClientFactory, id):
    return factory.factory_method(id)
