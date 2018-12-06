import sys
suma = 0
def is_float(value):
  try:
    float(value)
    return True
  except:
    return False

for arg in sys.argv: #(1)
    if is_float(arg)==True:
        suma +=float(arg)
print("Sum:",suma)
