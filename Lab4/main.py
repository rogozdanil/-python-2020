from lab_python_pt.facade.Facade import Facade


def main():
    facade = Facade()
    facade.create_shops(1, 2)
    facade.create_clients(1, 2, 1)
    facade.attach_clients()

    facade.sport_shop_business_logic()
    facade.electronic_shop_business_logic()

    facade.detach_clients()

    facade.sport_shop_business_logic()
    facade.electronic_shop_business_logic()


if __name__ == '__main__':
    main()
