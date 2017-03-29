my_set = {1,2,5}
my_dict = {'name': "Julia", 'age': 90, 'grades': [13,21,33,100]}
another_dict = {1:15, 2:75, 3:150}

lottery_player = [
{
	'name': "Roy",
	'numbers': (13,25,44,66,71)
},
{
	'name': "Poy",
	'numbers': (14,25,44,66,71)
},
{
	'name': "Soy",
	'numbers': (15,25,44,66,71)
},
{
	'name': "Joy",
	'numbers': (16,25,44,66,71)
},
{
	'name': "Toy",
	'numbers': (17,25,44,66,71)
},
{
	'name': "Yoy",
	'numbers': (18,25,44,66,71)
}
]

university = [{
	'name': "Oxford",
	'location': "UK"
},
{
	'name': "MIT",
	'location': 'US'
}

]

another_dict_in_dict = {
	"key": {
	"name": "Julia"
	}
}

print(sum(lottery_player['numbers']))

print(lottery_player['name'])

lottery_player.total()


student = {
    'name': 'Jose',
    'school': 'Computing',
    'grades': (66, 77, 88)
}

student_list = [
{
    "name":"Jose",
    "school":"Computing",
    "grades":(66,77,88)
},
{
    "name":"Jose",
    "school":"Computing",
    "grades":(68,77,88)
},
{
    "name":"Jose",
    "school":"Computing",
    "grades":(69,77,88)
},
{
    "name":"Jose",
    "school":"Computing",
    "grades":(63,77,88)
},
{
    "name":"Jose",
    "school":"Computing",
    "grades":(61,77,88)
}
]

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades =  data['grades']
    return sum(grades) / len(grades)



print(average_grade(student))

def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
       total +=sum(student['grades'])
       count +=len(student['grades'])

    return total / count



print(average_grade_all_students(student_list))

