import os
import re
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
def code2_4_2():
	pattern = re.compile(r"\d+/\d+/\d+")
	text1 = "djksf2016/7/4"
	output = pattern.findall(text1)
	if(output!=None):
		print(name for name in output)

def code2_5_2():
	pattern = re.compile(r"(\d+)/(\d+)/(\d+)")
	text = "today is 11/7/2016"
	print(pattern.sub(r"\3-\1-\2",text))
if __name__ == '__main__':
	code2_5_2()