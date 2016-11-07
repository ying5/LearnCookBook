import os
from fnmatch import fnmatch,fnmatchcase
def code2_2_2():
	files = os.listdir('.')
	print([name for name in files if name.endswith('.py')])
def code2_3_2():
	names = ['data1.csv','data2.csv','data3.csv','data2.txt','d']
	print([name for name in names if fnmatch(name,'data[1-9]*')])
def code3_2_2():
	a = 4.2
	b = 2.1
	print (a+b)
if __name__ == '__main__':
	code3_2_2()