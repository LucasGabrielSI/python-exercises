import sys

arguments = sys.argv # arg1 = metod // arg2 = n1, arg3 = n2

def sum(number1, number2):
    return number1 + number2

def sub(number1, number2):
    return number1 - number2

if arguments[1] == 'sum':
    resp = sum(float(arguments[2]), float(arguments[3]))
elif arguments[1] == 'sub':
    resp = sub(float(arguments[2]), float(arguments[3]))

print(resp)