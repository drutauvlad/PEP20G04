# my_string = "something {}"
#
# my_string.capitalize()
# print(my_string.capitalize())
#
# my_string.format('new')
# print(my_string.format('new'))
#
# my_int = 3
# print(my_int)
# print(3 ** 2)
# print(my_int.__pow__(3))
# # float
# print(3 / 2)
#
# fl1 = 1.991
# fl2 = 3
#
# print(int(fl1 + fl2))
#
# # complex
# print(3 ** (1/2))
# print(4 ** (1/2))
# print(type((-1) ** (1/2)))
#
# n = 1 + 1j
# print(type(n))
# print(n.__pow__(2))
#
# # exponet
#
# print(type(5.5e10))
# print(0xff)
# print(0o77)
#
#
# def functie(a, b, c):
#     print((-b + (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a))

# functie(3, 4, 5)

# rational operators

# nr1 = 3
# nr2 = 5
# nr3 = 3
# nr4 = -32414352464563456
# nr5 = -32414352464563456
# print(nr1 == nr2)
# print(nr1 == nr3)
# print(nr4 == nr5)
# print('is')
# print(nr1 is nr3)
# print(nr4 is nr5)
# print(id(nr4))
# print(id(nr5))

a = 6
b = 4
c = 5

# This is for homework to print the correct answer

print('##################################################')
def functie(a, b, c):
    print(a < b < c)
    print(b < c < a)
    print(c < a < b)
    print('####################################################')

functie(2, 3, 4)
functie(4, 2, 3)
functie(3, 5, 2)
functie(3, 6, 6)

# type bool and None

def devide(x, y):
    if y == 0:
        return None
    else:
        return (x / y)

print(devide(8, 8))
print(devide(8, 0))


def just_true():
    if True:
        print('just true')



just_true()

print(bool('123'))
print(len(''))

def only_true():
    if 0+0j:
        print('only true')
    else:
        print('only false')

only_true()

print('#####################################')
print(True and False)
print(True or False and True)
print(True or False)


