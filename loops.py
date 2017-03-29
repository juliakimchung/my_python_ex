my_variable = 'hello'
for e in my_variable: #iterable(string, list, tuples, sets, and more)
    print(e)

my_list = [1,2,3,4,5,6]
for num in my_list:
    print(num ** 2)

user_wants_number = True

while user_wants_number == True:
    print(10)

    user_input = input("Should we print again?(y/n)")
    if user_input == 'n':
        user_wants_number = False