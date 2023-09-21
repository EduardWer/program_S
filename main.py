# Программа для нахождения прощади прямоугольника

def rentagle_area(width,height):
    ploshad = width*height
    return ploshad

print(rentagle_area(20,30))

# Программа для нахождения суммы чисел
def is_evel(namber):
    if namber % 2 == 0:
        return True
    else:
        return False

print(is_evel(2))

def sum_digits(namber):
    namber = list(str(namber))
    sum = 0
    for i in namber:
        i = int(i)
        sum = sum + i
    return sum

print(sum_digits(343))