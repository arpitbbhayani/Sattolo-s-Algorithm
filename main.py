import random
from typing import List, Any

ELEMENTS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


def sattolo_walk(arr: List[Any]):
  indexes: List[int] = list(range(len(arr)))
  for i, x in enumerate(arr):
    if i + 1 == len(indexes):
      yield arr[indexes[i]]
      return
    k = random.randint(i + 1, len(indexes) - 1)
    indexes[i], indexes[k] = indexes[k], indexes[i]
    yield arr[indexes[i]]


for x in sattolo_walk(ELEMENTS):
  print(x)
