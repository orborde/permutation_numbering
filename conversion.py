import itertools
import math
from typing import *

def perm2num(permutation: Tuple[int]) -> int:
    assert set(permutation) == set(range(len(permutation)))
    permutation = permutation[:]
    remainder = list(range(len(permutation)))
    pindex = []
    for item in permutation:
        idx = remainder.index(item)
        pindex.append(idx)
        remainder = remainder[:idx] + remainder[(idx+1):]
    return pindex2num(pindex)

def num2perm(n: int, length: int) -> Tuple[int]:
    pindex = num2pindex(n, length)
    remainder = list(range(length))
    result = []
    for idx in pindex:
        result.append(remainder[idx])
        remainder = remainder[:idx] + remainder[(idx+1):]
    return tuple(result)

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



def test_pindex(length: int):
    found = set()
    for n in range(math.factorial(length)):
        img = tuple(num2pindex(n, length))
        rev = pindex2num(img)
        print(n, img, rev)
        assert rev == n, n
        assert img not in found, img
        found.add(img)
    assert len(found) == math.factorial(length)

def test_perm(length: int):
    found = set()
    for perm in itertools.permutations(range(length)):
        n = perm2num(perm)
        rev = num2perm(n, len(perm))
        print(perm, n, rev)
        assert rev == perm, perm
        assert n not in found, n
        found.add(n)
    assert len(found) == math.factorial(length)


if __name__ == '__main__':
    # test_pindex(5)
    # test_perm(5)

    val = 8
    for n in range(math.factorial(val)):
        print(n, num2perm(n, val), num2pindex(n, val))
