import collections
import functools


class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned
   (not reevaluated).
   '''

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # uncacheable. a list, for instance.
            # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__

    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)


d = 2  # distance
heighs = [3, 3, 3]  # heights array


def magic():
    return round(max(fun(heighs.__len__() - 2, 0, 1)[0], fun(heighs.__len__() - 2, 0, heighs[heighs.__len__() - 1])[0]),
                 2)


@memoized
def fun(pointer, wires_len, previous_height):
    if pointer > 0:
        res1 = fun(pointer - 1, length(d, previous_height, 1) + wires_len, 1)
        res2 = fun(pointer - 1, length(d, previous_height, heighs[pointer]) + wires_len, heighs[pointer])
    if pointer == 0:
        res1 = (length(d, previous_height, 1) + wires_len, 1)
        res2 = (length(d, previous_height, heighs[pointer]) + wires_len, heighs[pointer])
    if res1[0] > res2[0]:
        wires_len = res1[0]
        current_height = res1[1]
    else:
        wires_len = res2[0]
        current_height = res1[1]
    return wires_len, current_height


def length(distance, h1, h2):
    h = max(h1, h2) - min(h1, h2)
    return (h ** 2 + distance ** 2) ** 0.5


print(magic())
