# -*- coding:utf-8 -*-
#利用property给一个Screen对象加上width和height属性，以及一个只读属性resolution

'a property code'
__author__='wmliu'

class Screen(object):

	@property
	def width(self):
		return self._width

	@width.setter
	def width(self,value):
		self._width=value

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self,value):
		self._height=value

	@property
	def resolution(self):
		return self.width*self.height

s=Screen()
s.width=1024
s.height=768
print('Resolution of the screen is %s' %(s.resolution))
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution