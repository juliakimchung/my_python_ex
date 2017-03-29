my_variable = 'hello'
grade_one = 77
grade_two = 80
grade_three = 90

grades = [43,66,70,77,80,83,88,90,99,100]# ordered list & append item goes last
tuple_grades = (77,88,89,91,92,99)#immutable
set_grades = {77,88,99,100, 100, 100} # unique & unordered
grades.append(108)
grades.append(110)
print(grades)
print(sum(grades)/len(grades))
tuple_grades = tuple_grades + (100, )
print(tuple_grades)
set_grades.add(60)
print(set_grades)

your_num = { 1,2,3,4,5}
winning_num= {1,3,5,7,9,11}

print(your_num.intersection(winning_num))
print(your_num.union(winning_num))
print(winning_num.difference({1,2}))