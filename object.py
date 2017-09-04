class Student(object):
	"""docstring for Student"""
	def __init__(self, name, age):
		super(Student, self).__init__()
		self.__name = name
		self.__age = age

	def getName(self):
		print('%s' % self.__name)

	@property
	def age(self):
		return self.__age;

	@age.setter
	def age(self, age):
		if not isinstance(age, int):
			raise ValueError('age must be an integer')
		if age < 0 or age > 100:
			raise ValueError('age must between 0~100')
		self.__age = age


s = Student('jingjing', 18)
s.getName()
s.age = 20	# 通过装饰器设置属性
print(s._Student__age)	# 强取私有属性
print(dir(Student))	# 获取类属性和方法
