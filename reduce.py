# -*- coding:utf-8 -*-
#利用reduce实现list元素的求积运算

from functools import reduce
def prod(x,y):
	return x*y

L=[3,5,7,9]
print(reduce(prod,L))