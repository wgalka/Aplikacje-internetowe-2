class OutOfRangeError(ValueError):
    pass

def get_age():
    while True:
        try:
            age = input("How old are you?")
            if age.isdigit() and int(age) in range(0, 123):
                print(age)
            else:
                raise OutOfRangeError
        except OutOfRangeError:
            print("Invalid integer input.")
        else:
            print("Valid input.")
            break

get_age()
