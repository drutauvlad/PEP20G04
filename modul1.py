# def add_a(message=' '):
#    print('a', message, 'a')
#
#add_a('sdfadsf')

def add_a(message=' '):
    full_message = 'a ' + message + ' a'
    print(full_message)
add_a('new message')

print((add_a('new')))


def print_number_twice(number):
    print(number * 3)

print_number_twice(3)
print_number_twice(True)

empty_string = ''
zero_value = 0
null = None

print('#################')


def add_b(message = 'daaab'):
    print('a' + message + 'a')
    return 'a' + message + 'a'

new_message = add_b()
print(new_message)


print("\"I'm\"")
print('""da""')
print('"""da"""')

################################

my_string = "my text"
dir(my_string)
print(dir(my_string))
print(len(my_string))
a = .__len__()

print(my_string.upper())