my_list = [0, 1, 2, 3, 4]
an_equal_list = [x for x in range(5)] # [0,1,2,3,4]
multiply_list = [x*3 for x in range(5)]
print(multiply_list)

print(8%3)

list_of_even_num = [x for x in range(25) if x%2 == 0]
print(list_of_even_num)

people_you_know = ['Rolf', "john",   "anna",   "GREG"]
normalize_people = [x.strip().lower() for x in people_you_know]
print(normalize_people)