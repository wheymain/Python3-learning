# -*- coding:utf-8 -*-
#面向对象、访问限制

class Student(object):
	def __init__(self,name,score):
		self.__name=name
		self.__score=score

	def print_score(self):
		print('%s:%s' %(self.__name, self.__score),end=" ")

	def get_grade(self):
		if self.__score>=90:
			print ('A')
		elif self.__score>=60:
			print ('B')
		else:
		    print ('C')

	def get_name(slef):
		return self.__name

	def get_score(self):
		return self.__score

	def set_score(self,score):
		if 0<=score<=100:
			self.__score=score
		else :
			raise ValueError('Wrong Score')

bart= Student('Bart',59)
lisa= Student('Lisa', 87)

bart.print_score()
bart.get_grade()
lisa.print_score()
lisa.get_grade()

bart.set_score(90)
bart.print_score()
bart.get_grade()