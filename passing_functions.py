def methodception(another):
	return another()

def add_two_numbers():
	return 35 + 77

print(methodception(add_two_numbers))
print(methodception(lambda: 35+77))

my_list = [13, 35,56,77,484]
print (list(filter(lambda x: x!=484, my_list)))

# same as this function

def not_thirteen(x):
	return x !=13

print(list(filter(not_thirteen, my_list)))
print([x for x in my_list if x !=13])