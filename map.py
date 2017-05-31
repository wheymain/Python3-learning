# -*- coding:utf-8 -*-
#利用map函数将用户输入的不规范英文名变为首字母大写

def normalize(name):
	return name.capitalize()

L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
print(L2)