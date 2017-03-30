def my_method(arg1, arg2):
	return arg1 + arg2

my_method(5,6)

def my_long_method(arg1,arg2, arg3,arg4):
	return arg1+arg2+arg3+arg4

def my_list_addition(list_arg):
	return sum(list_arg)

my_long_method(3,5,6,7)
my_list_addition([3,5,6,7,8,9])

def addtion_simplified(*args): # *args works as a list
	return sum(args)

addtion_simplified(3,4,5,6,7,8,9,10)

def what_are_kwargs(*args, **kwargs):
	print(args)
	print(kwargs)

what_are_kwargs(12,24,36, name="Jose", location="UK")