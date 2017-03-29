should_continue = True
if should_continue:
    print("hello")

known_people = ['John', "anna", "mary"]
person = input("enter the person you know")
if person in known_people:
    print("you know {}!".format(person))
else:
    print ("you don't know{}!".format(person))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Modify the method below to make sure only even numbers are returned.
def even_numbers():
    evens = []
    for num in numbers:
        
        if num%2 ==0:
            evens.append(num)
    return evens

print(even_numbers())
# Modify the below method so that "Quit" is returned if the choice parameter is "q".
# Don't remove the existing code
def user_menu(choice):
    if choice == "a":
        return "Add"
    elif choice == "q":
        return "Quit"
        
def who_do_you_know():
    #ask the user for a list of people they know
    #split the string into a list
    #return the list
    
    peoples = input("enter names you know separated by commas:  ")
    
    names = [nam.strip() for nam in peoples.split(",")
        ]

    return names

def ask_user():
    #ask user for a name
    #see if the name is in the list of people they know
    #print out that they know the person
    p = input("enter a name of someone you know: ")
    if p in who_do_you_know():
        print("you know {}".format(p))

print(ask_user())
