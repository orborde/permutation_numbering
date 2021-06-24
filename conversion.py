import math
from typing import *

def perm2num(permutation: List[int]) -> int:
    pass

def pindex2num(pindex: List[int]) -> int:
    radix = 1
    result = 0
    for position, idx in enumerate(pindex):
        result += radix * idx
        radix *= (len(pindex) - position)
    return result

def num2pindex(n: int, length: int) -> List[int]:
    radix = math.factorial(length)
    rev_result = []
    for i in range(length):
        quotient  = n // radix
        remainder = n % radix
        rev_result.append(quotient)
        n = remainder
        radix = radix // (i+2)
    return list(reversed(rev_result))



def test(length: int):
    found = set()
    for n in range(math.factorial(length)):
        img = tuple(num2pindex(n, length))
        rev = pindex2num(img)
        print(n, img, rev)
        assert rev == n, n
        assert img not in found, img
        found.add(img)
    assert len(found) == math.factorial(length)

if __name__ == '__main__':
    test(5)