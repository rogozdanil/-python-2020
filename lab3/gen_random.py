import random


def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield random.randrange(begin, end + 1)


if __name__ == '__main__':
    g = gen_random(5, 1, 3)

    for i in gen_random(5, 1, 3):
        print(i)
    print('\n')