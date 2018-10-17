# zad1 ...

s = [0] * 3
s[0] += 1
print(s)

s = [''] * 3
s[0] += 'a'
print(s)

s = [[]] * 3
s[2] += [1]
print(s)

s = [[]] * 3
s[0] = s[0] + [1]
print(s)

s = [[[]]] * 3
print(s)
s[0] += [1]
print(s)

a = 2
a += 3
print(a)
a = 2
a = a + 3
print(a)

# zad2
def gcd(a, b):
    while b:
        a, b = b, a % b
    return print(a)



gcd(10, 25)  # => 5
gcd(14, 15)  # => 1
gcd(3, 9)  # => 3
gcd(1, 1)  # => 1

# zad3

my_map = {"CA": "US", "NY": "US", "ON": "CA"}


def flip_dict(my_dict):
    inv_map = {}
    for key, value in my_dict.items():
        inv_map[value] = inv_map.get(value, [])
        inv_map[value].append(key)
    print(inv_map)


flip_dict(my_map)

# zad4

print('1', [x for x in [1, 2, 3, 4]])
print('2', [n - 2 for n in range(10)])
print('3', [k % 10 for k in range(41) if k % 3 == 0])
print('4', [s.lower() for s in ['PythOn', 'iS', 'cOoL'] if s[0] < s[-1]])

# Something is fishy here. Can you spot it?
arr = [[3, 2, 1], ['a', 'b', 'c'], [('do',), ['re'], 'mi']]
print(arr)
print('5',[el.append(el[0] * 4) for el in arr] ) # What does this return?
# What is the content of `arr` at this point?

print('6', [letter for letter in "pYthON" if letter.isupper()])
print('7', {len(w) for w in ["its", "the", "remix", "to", "ignition"]})

#Write a comprehension to transform the input data structure into the output data structure

print([x*2+1 for x in [0, 1, 2, 3]])
print([x % 3 == 0 for x in [3, 5, 9, 8]])
print([x.split('_')[1] for x in ["TA_sam", "TA_guido", "student_poohbear", "student_htiek"]if x.startswith('TA')])
print([x.upper()[0] for x in['apple', 'orange', 'pear']])
print([x for x in['apple', 'orange', 'pear'] if x != 'orange'])
print([(x, x.__len__()) for x in['apple', 'orange', 'pear']])
print({x: x.__len__() for x in['apple', 'orange', 'pear']})
