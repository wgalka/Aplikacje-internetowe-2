#Familiar Functions

def print_two(a, b):
    print("Arguments: {0} and {1}".format(a, b))
#print_two()
print_two(4, 1)
#print_two(41)  #invalid
#print_two(a=4, 1)  #invalid
#print_two(4, a=1)  #invalid
#print_two(4, 1, 1)  #invalid
#print_two(b=4, 1)  #invalid
print_two(a=4, b=1) 
print_two(b=1, a=4) 
#print_two(1, a=1)  #invalid
#print_two(4, 1, b=1)  #invalid

print_two(b=6, a=4)

#Default Arguments

def keyword_args(a, b=1, c='X', d=None):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)
    print("-----------------------")
    
keyword_args(5)
keyword_args(a=5)
keyword_args(5, 8)
keyword_args(5, 2, c=4)
keyword_args(5, 0, 1)
keyword_args(5, 2, d=8, c=4)
#keyword_args(5, 2, 0, 1, "") keyword_args() takes at most 4 arguments (5 given)
#keyword_args(c=7, 1) non-keyword arg after keyword arg
keyword_args(c=7, a=1)
keyword_args(5, 2, [], 5)
#keyword_args(1, 7, e=6) keyword_args() got an unexpected keyword argument 'e'
keyword_args(1, c=7)
#keyword_args(5, 2, b=4)  keyword_args() got multiple values for keyword argument 'b'

#Exploring Variadic Argument lists

def variadic(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)
    print("-------------------------")
    
variadic(2, 3, 5, 7)
variadic(1, 1, n=1)
#variadic(n=1, 2, 3) non-keyword arg after keyword arg
variadic()
variadic(cs="Computer Science", pd="Product Design")
#variadic(cs="Computer Science", cs="CompSci", cs="CS") keyword argument repeated
variadic(5, 8, k=1, swap=2)
variadic(8, *[3, 4, 5], k=1, **{'a':5, 'b':'x'})
#variadic(*[8, 3], *[4, 5], k=1, **{'a':5, 'b':'x'}) invalid syntax
#variadic(*[3, 4, 5], 8, *(4, 1), k=1, **{'a':5, 'b':'x'}) invalid syntax
variadic({'a':5, 'b':'x'}, *{'a':5, 'b':'x'}, **{'a':5, 'b':'x'})

#Optional: Putting it all together

def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options):
    print("x:", x)
    print("y:", y)
    print("z:", z)
    print("nums:", nums)
    print("indent:", indent)
    print("spaces:", spaces)
    print("options:", options)

#all_together(2)  TypeError: all_together() missing 1 required positional argument: 'y'
all_together(2, 5, 7, 8, indent=False)
all_together(2, 5, 7, 6, indent=None)
#all_together()  TypeError: all_together() missing 2 required positional arguments: 'x' and 'y'
#all_together(indent=True, 3, 4, 5)  SyntaxError: positional argument follows keyword argument
#all_together(**{'indent': False}, scope='maximum')  TypeError: all_together() missing 2 required positional arguments: 'x' and 'y'
all_together(dict(x=0, y=1), *range(10))
#all_together(**dict(x=0, y=1), *range(10))  SyntaxError: iterable argument unpacking follows keyword argument unpacking
#all_together(*range(10), **dict(x=0, y=1))  TypeError: all_together() got multiple values for argument 'x'
all_together([1, 2], {3:4})
#all_together(8, 9, 10, *[2, 4, 6], x=7, spaces=0, **{'a':5, 'b':'x'})  TypeError: all_together() got multiple values for argument 'x'
all_together(8, 9, 10, *[2, 4, 6], spaces=0, **{'a':[4,5], 'b':'x'})
all_together(8, 9, *[2, 4, 6], *dict(z=1), spaces=0, **{'a':[4,5], 'b':'x'})

#Writing Functions

def speak_excitedly(message, number=1, capitalize=False):
    if capitalize == False:
        print(message, number*'!')
    else:
        print(message.upper(), number*'!')

speak_excitedly('I love Python')
speak_excitedly('Keyword arguments are great',4)
speak_excitedly('I guess Java is okay...', 0)
speak_excitedly("LET'S GO STANFORD",2,True)

#average

def average(*nums):
    if not nums:
        print(None)
    else:
        suma = sum(nums)
        print(suma/nums.__len__())

average()
average(5)
average(6, 8, 9, 11)
average(*[6, 8, 9, 11])

#Challenge: make_table

def make_table(key_justify='left', value_justify='right', **kwargs):

    if key_justify == 'left':
        key_justify = '<'
    elif key_justify == 'right':
        key_justify = '>'
    elif key_justify == 'center':
        key_justify = '^'

    if value_justify == 'left':
        value_justify = '<'
    elif value_justify == 'right':
        value_justify = '>'
    elif value_justify == 'center':
        value_justify = '^'

    max_key_length = max(map(len, kwargs.keys()))
    max_value_length = max(map(len, kwargs.values()))

    total_length = 2 + max_key_length + 3 + max_value_length + 2
    print('=' * total_length)
    for key, value in kwargs.items():
        print('| {:{align1}{length1}} | {:{align2}{length2}} |'.format(key, value,
                                                                                 align1=key_justify,
                                                                                 length1=max_key_length,
                                                                                 align2=value_justify,
                                                                                 length2=max_value_length
                                                                                 ))
    print('=' * total_length)

def test_make_table():
    make_table(
        first_name="Sam",
        last_name="Redmond",
        shirt_color="pink"
    )

    make_table(
        key_justify="right",
        value_justify="center",
        song="Style",
        artist_fullname="Taylor $wift",
        album="1989"
    )

test_make_table()

#Function Nuances

def say_hello():
    print("Hello!")

print(say_hello())  # => ?

def echo(arg=None):
    print("arg:", arg)
    return arg

print(echo())  # => ?
print(echo(5)) # => ?
print(echo("Hello")) # => ?

def drive(has_car):
    if not has_car:
        return
    return 100  # miles

drive(False)  # => ?
drive(True)   # => ?

#Parameters and Object Reference

def reassign(arr):
    arr = [4, 1]
    print("Inside reassign: arr = {}".format(arr))

def append_one(arr):
    arr.append(1)
    print("Inside append_one: arr = {}".format(arr))

l = [4]
print("Before reassign: arr={}".format(l))  # => ?
reassign(l)
print("After reassign: arr={}".format(l))  # => ?

l = [4]
print("Before append_one: arr={}".format(l))  # => ?
append_one(l)
print("After append_one: arr={}".format(l))  # => ?

#Scope

# Case 1
x = 10

def foo():
    print("(inside foo) x:", x)
    y = 5
    print('value:', x * y)

print("(outside foo) x:", x)
foo()
print("(after foo) x:", x)


# Case 2
x = 10

def foo():
    x = 8  # Only added this line - everything else is the same
    print("(inside foo) x:", x)
    y = 5
    print('value:', x * y)

print("(outside foo) x:", x)
foo()
print("(after foo) x:", x)

#Default Mutable Arguments - A Dangerous Game

x = 5

def square(num=x):
    return num * num

x = 6
print(square())
print(square(x))

def append_twice(a, lst=[]):
    lst.append(a)
    lst.append(a)
    return lst


# Works well when the keyword is provided
append_twice(1, lst=[4])  # => [4, 1, 1]
append_twice(11, lst=[2, 3, 5, 7])  # => [2, 3, 5, 7, 11, 11]

# But what happens here?
print(append_twice(1))
print(append_twice(2))
print(append_twice(3))


def fib(n, cache={0: 1, 1: 1}):
   if n in cache:  # Note: default value captures our base cases
       return cache[n]
   out = fib(n-1) + fib(n-2)
   cache[n] = out
   return out


print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(10))

#Investigating Function Objects

def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options):
    print("x:", x)
    print("y:", y)
    print("z:", z)
    print("nums:", nums)
    print("indent:", indent)
    print("spaces:", spaces)
    print("options:", options)

print(all_together.__defaults__) #wszystkie wartosci domyslne poprzedzajace *nums zostaja wypisane
print(all_together.__kwdefaults__)  #wszystkie zmienne oraz wartosci domyslne poprzedzajace **options zostaja wypisane

def my_function():
    """Summary line: do nothing, but document it.

    Description: No, really, it doesn't do anything.
    """
    pass


print(my_function.__doc__)
# Summary line: Do nothing, but document it.
#
#     Description: No, really, it doesn't do anything.

#Code Object (__code__)

def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options):
    """A useless comment"""
    print(x + y * z)
    print(sum(nums))
    for k, v in options.items():
        if indent:
            print("{}\t{}".format(k, v))
        else:
            print("{}{}{}".format(k, " " * spaces, v))


code = all_together.__code__

print(all_together.__doc__)
print(code.co_argcount)
print(code.co_cellvars)
print(code.co_code)
print(code.co_consts)
print(code.co_filename)
print(code.co_firstlineno)
print(code.co_flags)
print(code.co_freevars)
print(code.co_kwonlyargcount)
print(code.co_lnotab)
print(code.co_name)
print(code.co_names)
print(code.co_nlocals)
print(code.co_stacksize)
print(code.co_varnames)

#Security

def nice(): print("You're awesome!")
def mean(): print("You're... not awesome. OOOOH")

# Overwrite the code object for nice
nice.__code__ = mean.__code__
nice()  # prints "You're... not awesome. OOOOH"


#dis module, for "disassemble," exports a dis function that allows us to disassemble Python byte code
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


import dis

dis.dis(gcd)


def annotated(a: int, b: str) -> list:
    return [a, b]
#Parameter Annotations (__annotations__)
print(annotated.__annotations__)
# {'b': <class 'str'>, 'a': <class 'int'>, 'return': <class 'list'>}

#Call (__call__)

def greet(): print("Hello world!")

greet() # "Hello world!"
# is just syntactic sugar for
greet.__call__()  # "Hello world!"
