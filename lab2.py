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
inv_map = {value: key for key, value in my_map.items()}
inv_map = {}
for key, value in my_map.items():
    inv_map[value] = inv_map.get(value, [])
    inv_map[value].append(key)

print(inv_map)

# zad4

