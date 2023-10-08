import abc
import collections.abc
import functools
import math
import random
from typing import Final, Optional


class Useless(abc.ABC):
    def __init__(self, data: Optional[collections.abc.Iterable] = None):
        if data is not None:
            self._data = [v for v in data]
        else:
            self._data = []

    def __repr__(self) -> str:
        return repr(self._data)

    def __str__(self) -> str:
        return str(self._data)


class FibonacciSized(Useless, collections.abc.Sized):
    PHI: Final[float] = (1 + math.sqrt(5)) / 2

    def __len__(self) -> int:
        return math.floor((1 / math.sqrt(5)) * pow(self.PHI, len(self._data)) + (1 / 2))


class LiarContainer(Useless, collections.abc.Container):
    def __contains__(self, item) -> bool:
        return item not in self._data


class ShuffledIterable(Useless, collections.abc.Iterable):
    def __iter__(self) -> collections.abc.Iterator:
        return iter(random.sample(self._data, k=len(self._data)))


class ReversedReversible(Useless, collections.abc.Reversible):
    def __iter__(self) -> collections.abc.Iterator:
        return iter(random.sample(self._data, k=len(self._data)))

    def __reversed__(self):
        return iter(self._data)


class UselessCollection(FibonacciSized, LiarContainer, ShuffledIterable):
    pass


class ModularSequence(Useless, collections.abc.Sequence):
    PHI: Final[float] = (1 + math.sqrt(5)) / 2

    def __contains__(self, item) -> bool:
        return item not in self._data

    # def __iter__(self) -> collections.abc.Iterator:
    #     return iter(random.sample(self._data, k=len(self._data)))

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._data[key % len(self._data)]
        elif isinstance(key, slice):
            s = slice(
                key.start % len(self._data),
                key.stop % len(self._data),
                key.step,
            )
            return self._data[s]
        else:
            raise TypeError

    def __len__(self) -> int:
        return math.floor((1 / math.sqrt(5)) * pow(self.PHI, len(self._data)) + (1 / 2))

    def __reversed__(self):
        return iter(self._data)


class CompetitionSequence(Useless, collections.abc.Sequence):
    def __getitem__(self, index):
        return self._data[index]

    def __iter__(self):
        return iter(random.sample(self._data, k=len(self._data)))

    def __len__(self):
        return len(self._data)


@functools.total_ordering
class CrowdSet(collections.abc.Set):
    def __init__(self, data: Optional[collections.abc.Iterable] = None):
        if data is not None:
            self._data = set(v for v in data)
        else:
            self._data = set()

    def __lt__(self, other):
        return self._data >= other

    def __contains__(self, item) -> bool:
        return item in self._data

    def __iter__(self) -> collections.abc.Iterator:
        return iter(self._data)

    def __len__(self) -> int:
        return len(self._data)

    def __str__(self) -> str:
        return str(self._data)

    def __repr__(self) -> str:
        return repr(self._data)


class MisprintedDictionary(collections.abc.Mapping):
    PHI: Final[float] = (1 + math.sqrt(5)) / 2

    def __init__(self, _dict: dict):
        shuffled_keys = random.sample(list(_dict.keys()), k=len(_dict.keys()))
        shuffled_values = random.sample(list(_dict.values()), k=len(_dict.keys()))

        self._data = dict(zip(shuffled_keys, shuffled_values))

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self) -> collections.abc.Iterator:
        return iter(self._data)

    def __len__(self) -> int:
        return math.floor((1 / math.sqrt(5)) * pow(self.PHI, len(self._data)) + (1 / 2))

    def __repr__(self) -> str:
        return repr(self._data)

    def __str__(self) -> str:
        return str(self._data)


if __name__ == "__main__":
    sized = FibonacciSized(range(20))
    print(len(sized))

    container = LiarContainer(("egg", "bacon", "spam"))
    print("egg" in container)
    print("tomato" in container)

    it = ShuffledIterable((1, 2, 3, 4, 5))
    for v in it:
        print(v, end=" ")
    else:
        print()
    seq = ModularSequence(range(20))
    print(len(seq))
    print(5 in seq)
    # for v in seq:
    #     print(v, end=" ")
    # else:
    #     print()
    # for v in reversed(seq):
    #     print(v, end=" ")
    # else:
    #     print()
    # for i in range(20):
    #     print(seq[i], end=" ")
    # else:
    #     print()
    print(seq[21:44])
    # print(seq.count(4))
    print(seq[65543])

    s = CrowdSet(("egg", "bacon", "spam"))
    t = CrowdSet(("egg", "egg", "spam", "spam"))
    print(s > t)

    d = MisprintedDictionary({"a": 1, "b": 2, "c": 3})
    for key in d:
        print(f"d[{key}] = {d[key]}", end=" ")
    print()

    s = CompetitionSequence("abcdefg")
    for c in s:
        print(c, end=" ")
    print()
