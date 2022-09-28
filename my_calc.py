def sum_1(x, y):
    return x + y

def sub_2(x, y):
    return x - y

def mult_3(x, y):
    return x * y

def div_4(x, y):
    try:
        return round(x / y, 2)
    except ZeroDivisionError:
        print("Don't division by 0")

