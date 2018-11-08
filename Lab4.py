#Functional Tools

#Lambda

print((lambda val: val ** 2)(5))  # => 25
print((lambda x, y: x * y)(3, 8))  # => 24
print((lambda s: s.strip().lower()[:2])('  PyTHon'))  # => 'py'

#Other Useful Tools
#Module: functools

from functools import reduce

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(*args):
    return reduce(lambda x, y: x * y // gcd(x, y), args)

print(lcm(1, 4))
print(lcm(1, 2, 5))

#Module: operator

import operator
print(operator.add(1, 2))  # => 3
print(operator.mul(3, 10))  # => 30
print(operator.pow(2, 3))  # => 8
print(operator.itemgetter(1)([1, 2, 3])) # => 2


#Use reduce in conjunction with a function from the operator module to compute factorials in one line of Python:
import operator
from functools import reduce

def fact(n):
    return reduce(operator.mul, range(1,n+1))

print(fact(3))  # => 6
print(fact(7))  # => 5040

words = ['pear', 'cabbage', 'apple', 'bananas']
print(min(words))  # => 'apple'
print(words.sort(key=lambda s: s[-1]))  # Alternatively, key=operator.itemgetter(-1)
print(words)  # => ['cabbage', 'apple', 'pear', 'bananas'] ... Why 'cabbage' > 'apple'?
print(max(words, key=len))  # 'cabbage' ... Why not 'bananas'?
print(min(words, key=lambda s: s[1::2]))  # What will this value be?

def alpha_score(upper_letters):
    """Computers the alphanumeric sum of letters in a string.
    Prerequisite: upper_letters is composed entirely of capital letters.
    """
    return sum(map(lambda l: 1 + ord(l) - ord('A'), upper_letters))

alpha_score('ABC')  # => 6 = 1 ('A') + 2 ('B') + 3 ('C')

def two_best(words):
	words.sort(key=lambda word: alpha_score(filter(str.isupper, word)), reverse=True)
	return words[:2]

print(two_best(['hEllO', 'wOrLD', 'i', 'aM', 'PyThOn']))


#Purely Functional Programming



