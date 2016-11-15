from decimal import Decimal
import numpy as np
import cmath
def code3_1_2():
	print(round(12.5,-1))
	print(format(2.33,'0.2f'))
	print("value is {:0.3f}".format(134.2234))
def code3_3_2():
	str1 = 12.34
	print(format(str1,"^10.1f"))
def code3_4_2():
	x = 1234
	print(format(x,'b'))
	print(oct(x))
	print(hex(x))
def code3_5_2():
	data = b'\x00\x124V\x00\x90\xab\x00\xcd'
	print(int.from_bytes(data,"little"))
def code3_6_2():
	a = np.array([2,3,4,5])
	print(cmath.sqrt(-1))
def code3_8_2():
	#grid = np.zeros(shape = (10000,10000),dtype = float)
	a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
	#print(grid+2)
	print(a[:1])
if __name__ == '__main__':
	code3_8_2()