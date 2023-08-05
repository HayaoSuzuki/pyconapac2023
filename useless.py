import abc
import collections.abc
import math
import random
from typing import Optional


class Useless(abc.ABC):
    def __init__(self, data: Optional[collections.abc.Iterable] = None):
        if data is not None:
            self._data = [v for v in data]
        else:
            self._data = []


class FibonacciSized(Useless, collections.abc.Sized):
    def __len__(self) -> int:
        phi = 1 + math.sqrt(5) / 2
        return math.floor(
            (1 / math.sqrt(5)) * pow(phi, len(self._data)) + (1 / 2)
        )


class LiarContainer(Useless, collections.abc.Container):
    def __contains__(self, item) -> bool:
        return item not in self._data


class ShuffledIterable(Useless, collections.abc.Iterable):
    def __iter__(self) -> collections.abc.Iterator:
        return iter(random.sample(self._data, k=len(self._data)))
