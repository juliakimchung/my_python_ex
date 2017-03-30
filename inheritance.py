class Student:
	def __init__(self, name, school):
		self.name = name
		self.school = school
		self.marks = []

	def average(self):
		return sum(self.marks)/len(self.marks)

	@classmethod
	def friend(cls, origin, friend_name, *args, **kwargs):
		return cls(friend_name, origin.school, *args, **kwargs)


class WorkingStudent(Student):
	def __init__(self, name, school, salary, job_title):
		super().__init__(name, school)
		self.salary = salary
		self.job_title = job_title




anna =WorkingStudent("Anna", "Oxford", 20.000, "software developer")
print(anna.salary)
friend = anna.friend(anna, "Greg", 30000, job_title="software developer")
print(anna.name)
print(anna.school)
print(friend.salary)
print(friend.school)
print(friend.job_title)