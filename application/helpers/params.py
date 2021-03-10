from typing import Optional, List, Tuple, Iterator, KeysView, Dict

Pair = Tuple[str, Optional[str]]
Value = str
Values = List[str]


class Params(object):
    params: Dict[str, str]

    def __init__(self, params: Dict[str, str]):
        self.params = params

    def get(self, key: str) -> Optional[Value]:
        return self.params.get(key)

    def get_list(self, key: str, delimiter: str = ",") -> Optional[Values]:
        value = self.params.get(key)

        if not value:
            return None

        return value.split(delimiter)

    def keys(self) -> KeysView[str]:
        return self.params.keys()

    def values(self) -> Iterator[Pair]:
        for key in self.params.keys():
            yield key, self.params.get(key)
