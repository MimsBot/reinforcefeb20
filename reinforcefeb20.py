
results = list(range(1, 100))

def odds():
    for number in results:
        if number % 2 != 0:
            print('odd')
        else:
            print('number')

print(odds())


names = ['Mario', 'Bowser', 'Peach']

print('please enter a name')
users_name = input()
for name in names:
    if users_name == name:
        print('Hello {}'.format(users_name))
    else:
        print('Who is this?')
