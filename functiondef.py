# -*- coding:utf-8 -*-
#定义一个函数quadratic(a,b,c)，接收三个参数，返回一元二次方程ax2+bx+c=0的根
#***本程序亮点在于先判断此方程是否有实数根，如果无实数根会显示“此方程无实数根”，有实数根则显示结果

import math

def quadratic(a,b,c):
	if not isinstance(a,int):
		raise TypeError('bad operand type')
	if not isinstance(b,int):
		raise TypeError('bad operand type')
	if not isinstance(c,int):
		raise TypeError('bad operand type')
	if(b*b-4*a*c)<0:
		return('此方程无实根')
	else:
	    x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
	    x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
	    return x1,x2
print(quadratic(2,3,1))
print(quadratic(1,3,4))