# -*- coding:utf-8 -*-
#面向对象

class Student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score

	def print_score(self):
		print('%s:%s' %(self.name, self.score),end=" ")

	def get_grade(self):
		if self.score>=90:
			print ('A')
		elif self.score>=60:
			print ('B')
		else:
		    print ('C')

bart= Student('Bart',59)
lisa= Student('Lisa', 87)

bart.print_score()
bart.get_grade()
lisa.print_score()
lisa.get_grade()