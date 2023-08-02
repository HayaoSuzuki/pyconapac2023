import abc
import collections.abc
import random
from typing import Optional


class Useless(abc.ABC):
    def __init__(self, data: Optional[collections.abc.Iterable] = None):
        if data is not None:
            self._data = [v for v in data]
        else:
            self._data = []


class ElasticSized(Useless, collections.abc.Sized):
    def __len__(self) -> int:
        return random.randint(0, len(self._data))


class ForgottenContainer(Useless, collections.abc.Container):
    def __contains__(self, item) -> bool:
        return True if random.random() >= 0.5 else False


class ShuffledIterable(Useless, collections.abc.Iterable):
    def __iter__(self) -> collections.abc.Iterator:
        return iter(random.sample(self._data, k=len(self._data)))
