# -*- coding:utf-8 -*-
#输入身高、体重，根据BMI指数输出相应健康信息

height=float(input('请输入您的身高(m)：'))
weight=float(input('请输入您的体重(kg)：'))
BMI=weight/(height*height)
if(BMI<18.5):
	print('您体重过轻')
elif(BMI<25):
	print('您体重正常')
elif(BMI<28):
	print('您体重过重')
elif(BMI<32):
	print('您体重肥胖')
else:
	print('您严重肥胖')