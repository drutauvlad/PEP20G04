print(True < 2)
print(True + False + 1)
myvar1 = [1,2]
myvar2 = [3]
print(myvar1 + myvar2)
print(dir(myvar1))
print(dir(3))
sumlist = myvar1 + myvar2
# print(sumlist - 3)

print(bin(10))

print(True & True)
print(True & False)
print(10 & 10)
print(11 | 9)
print(11 >> 2)
print(11 << 1)
print(~ 11)
print(~(-5))
print(11 ^ 20)
print(31 ^ 20)
print('#############################################')
print(chr(ord('a') ^ ord('x')))
print(ord(chr(25)) ^ ord('x'))
#print(chr(97))

print('#################################################')


print('############################################################')

def if_statement(number):
    if number < 2:
        print('True')
    elif number > 3:
        print('more than 3')
    elif number == 3:
        print('number is 3')
    else:
        print('this is else')

if_statement(2)

#def functie():
#    str2 = input('text:')
#    if str2 == 'if':
#        print('este if')
#    elif str2 == "elif":
#        print('este elif')
#    else:
#        print('este altceva')

#functie()



def functie2(numar, litera):
    if numar == ord(litera):
        print(litera)
    elif ord(litera) < numar:
        print('letter is to small')
    else:
        print('letter to big')

functie2(9, 'a')

def valoare(my_str, lit, index):
    if lit == my_str[index]:
        print("Litera este aici.")
    else:
        print("Litera este la alta pozitie.")

valoare("abcd","b",1)


print(type("my_str".__iter__()))


my_iter = "my_str".__iter__()

def fun(my_str):
    for a in my_str:
        print(a)
b = [3, 4, 5, 6, 7, 8]
fun(b)


def crypt(my_str, key):
    result = ''
    for var in my_str:
        new_chr = chr(ord(var) ^ key)
        print(new_chr)

crypt('my_str', 128)

def crypt(my_str, key):
    result = ''
    for var in my_str:
        new_chr = chr(ord(var) ^ key)
        result += new_chr
        print(result)
crypt('my_str', 128)