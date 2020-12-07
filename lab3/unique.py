import types
from gen_random import gen_random


class Unique(object):
    def __init__(self, items, **kwargs):
        self.index = 0
        self.data = items
        self.used_elements = set()
        self.ignore_case = False
        for key in kwargs:
            if key == 'ignore_case':
                self.ignore_case = kwargs[key]
        pass

    def __next__(self):
        while True:
            if type(self.data) == types.GeneratorType:
                current = next(self.data)
            elif self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]
                if type(current) == str and self.ignore_case == True:
                    current = current.lower()
                self.index = self.index + 1
            if current not in self.used_elements:
                self.used_elements.add(current)
                return current
        pass

    def __iter__(self):
        return self


if __name__ == '__main__':
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for i in Unique(data, ignore_case=True):
        print(i)
    print('\n')

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for i in Unique(data, ignore_case=False):
        print(i)
    print('\n')

    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    for i in Unique(data, ignore_case=True):
        print(i)
    print('\n')

    data = gen_random(10, 1, 3)
    for i in Unique(data, ignore_case=True):
        print(i)
