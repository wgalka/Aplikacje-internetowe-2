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