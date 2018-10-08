def colatz(number):
    x = number
    counter = 1
    while x != 1:
        if x % 2 == 0:
            x = x/2
            counter += 1
        else:
            x = 3*x+1
            counter += 1
    return counter, number

def szukaj(border):
    max = (0,0)
    while border != 1:
       test = colatz(border)
       if test > max:
           max=test
       border -= 1
    return max

i = szukaj(1000000)
print('ilosc stanów:', i[0], '  liczba:', i[1])