from __future__ import annotations
from typing import List, Dict, Union, Tuple
class Permutation(dict):
    def __init__(self, data: Union[List,Dict]) -> None:
        if type(data) == list:
            data = dict(enumerate(data))
        if set(data.keys()) != set(data.values()):
            raise 'not biinjection'
        super().__init__(data)

    def to_matrix(self) -> List[Tuple]:
        return list(zip(*self.items()))

    def __mul__(self, other: Permutation):
        if set(self.keys()) != set(other.keys()):
            raise 'different set'
        return Permutation({i:self[other[i]] for i in other})
        

    def fix(self, x):
        return self[x] == x
    def move(self, x):
        return self[x] != x

    def to_cycles(self) -> List[Tuple]:
        visited = set()
        cycles = []
        for i in self:
            if i not in visited:
                visited.add(i)
                cycle = [i]
                while self[i] not in visited:
                    i = self[i]
                    visited.add(i)
                    cycle.append(i)
                cycles.append(tuple(cycle))
        return cycles

            

