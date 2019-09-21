print("Hello world!")
msg = "Hello world!"
print(msg)
first_name = "Sriram"
last_name = "Chalamacharla"
full_name = first_name + ' ' + last_name
print(full_name)
consoles = ['xbox', 'playstation', 'stadia']
first_console = consoles[0]
last_console = consoles[-1]
for console in consoles:
    print(console)
consoles = []
consoles.append('xbox')
consoles.append('playstation')
consoles.append('stadia')
squares = []
for x in range(1, 11):
    squares.append(x**2)
squares = [x**2 for x in range(1, 11)]
winners = ['Einstein', 'Newton', 'Bob', 'Jeff']
first_two = winners[:2]
copy_of_consoles = consoles[:]
dimensions = (1920, 1080)
# equals: x == 42
# not equal: x != 42
# greater than: x > 42
#    or equal to: x >= 42
# less than: x < 42
#    or equal to: x <= 42
#  'xbox' in consoles
#  'computer' not in consoles
# game_active = True
# can_edit = False
#if age >= 18:
    # print("You can vote!")

# if age <4:
    # ticket_price = 0
# elif age < 18:
    # ticket_price = 10
# else:
    # ticket_price = 15
alien = {'color': 'green', 'points': 5}
print("The alien's color is " + alien['color'])
alien['x_position'] = 0
fav_numbers = {'eric': 17, 'ever': 4}
for name, number in fav_numbers.items():
    print(name + ' loves ' + str(number))
for name, number in fav_numbers.keys():
    print(name + ' loves a number')
for name, number in fav_numbers.values():
    print(str(number) + ' is a favorite')

name = input("What's you name? ")
print("Hello, " + name + "!")
age = input("How old are you? ")
age = int(age)

pi = input("What's the value of pi? ")
pi = float(pi)

current_value = 1
while current_value <= 5:
    print(current_value)
    current_value += 1

msg = ''
while msg != 'quit':
    msg = input("What's your message? ")
    print(msg)

def greet_user():
    print("Namaste!")

greet_user()

def greet_user(username):
    print("Namaste, " + username + "!")

greet_user('FaZe Sway')

def make_pizza(topping = 'brocolli'):
    print("Have a " + topping + " pizza!")
    make_pizza()
    make_pizza("Spinach")

def add_numbers(x, y):
    return x + y

sum = add_numbers(6, 9)
print(sum)

class Dog():
    def __init__(self, name):
        self.name = name

    def sit(self):
        print(self.name + " is sitting.")

my_dog = Dog('Sway')

print(my_dog.name + " is a great dog!")
my_dog.sit()

class SARDog(Dog):
    def __init__(self, name):
        super().__init__(name)

print("hi")

