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
print_two(a=4, b=1)  #invalid
print_two(b=1, a=4)  #invalid
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


