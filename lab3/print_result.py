def print_result(func):
    def wrapper(*func_args, **func_kwargs):
        print(func.__name__)
        arr = func(*func_args, **func_kwargs)
        if isinstance(arr, int):
            print(arr)
        elif isinstance(arr, str):
            print(arr)
        elif isinstance(arr, list):
            for i in arr:
                print(i)
        elif isinstance(arr, dict):
            for key, value in arr.items():
                print(key, "=", value)
        return arr
    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()