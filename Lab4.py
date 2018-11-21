#Functional Tools

#Lambda

print(((lambda val: val ** 2)(5))) # => 25
print(((lambda x, y: x * y)(3, 8)))  # => 24
print(((lambda s: s.strip().lower()[:2])('  PyTHon')))  # => 'py'

print(*map(lambda a: a, ['12', '-2', '0']))
print(*map(lambda a: len(a), ['hello', 'world']))
print(*map(lambda a: a[::-1], ['hello', 'world']))
print(*map(lambda a: (a, a*a, a*a*a), range(2, 6)))
print(*map(lambda a: a[0]*a[1], zip(range(2, 5), range(3, 9, 2))))

#Filter

print(*filter(lambda a: int(a) > -1, ['12', '-2', '0']))
print(*filter(lambda a: a == "world", ['hello', 'world']))
print(*filter(lambda a: a == "Stanford", ['Stanford', 'Cal', 'UCLA']))
print(*filter(lambda a: a % 3 == 0 or a % 5 == 0, range(20)))

#Other Useful Tools

from functools import reduce

def gcd(a, b):
    """Reference implementation of finding the
    greatest common denominator of two numbers"""
    while b != 0:
        a, b = b, a % b
    return a

def lcm(*args):
    return reduce(lambda a, b: a*b // gcd(a, b), args)

print(lcm(3,5,6 ))
print(lcm(10,2,3))

#---------------------

import operator
from functools import reduce

def fact(n):
    return reduce(lambda x, y: operator.mul(x, y), range(1, n+1))

print(fact(3))
print(fact(7))



def alpha_score(upper_letters):
    """Computers the alphanumeric sum of letters in a string.
    Prerequisite: upper_letters is composed entirely of capital letters.
    """
    return sum(map(lambda l: 1 + ord(l) - ord('A'), upper_letters))

print(alpha_score('ABC'))  # => 6 = 1 ('A') + 2 ('B') + 3 ('C')

def two_best(words):
    words.sort(key=lambda a: alpha_score(filter(str.isupper, a)))
    words = words[::-1]
    return words[0:2]

print(two_best(['hEllO', 'wOrLD', 'i', 'aM', 'PyThOn']))

#Purely Functional Programming

def resolve(score):
    return (score == 1 and "Winner") or (score == -1 and "Looser") or ("Tied")

print(resolve(1))
print(resolve(-1))
print(resolve(21))

#Iterators

it = iter(range(100))
print(67 in it)  # => True
print(next(it)) # => 68
print(37 in it) # => False
print(next(it)) # => False StopIteration

import itertools
import operator

for el in itertools.permutations('XKCD', 2):
    print(el, end=', ')

#for el in itertools.cycle('LO'):
#    print(el, end='')  # Don't run this one. Why not?

itertools.starmap(operator.mul, itertools.zip_longest([3,5,7],[2,3], fillvalue=1))
#challenge
from functools import reduce
def dot_product(u, v):
    return reduce(lambda x, y: x + y, list(map(lambda x, y: x * y, u, v)))

print(dot_product([1, 3, 5], [2, 4, 6]))

def transpose(m):
    return zip(*m)

matrix = (
    (1, 2, 3, 4),
    (5, 6, 7, 8),
    (9,10,11,12))

print(list(transpose(matrix)))

#Generator Expressions

def generate_triangles():
    n = 1
    while True:

        yield n * (n + 1) // 2
        n = n + 1

def triangles_under(n):
    x = 0
    triangles = generate_triangles()
    while x < n:
        print(x)
        x = next(triangles)

triangles_under(100)
