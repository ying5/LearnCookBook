from collections import deque
import heapq

def search(lines,pattern,history=1):
	pre_lines = deque(maxlen = history)
	for line in lines:
		if pattern in line:
			yield line,pre_lines
		pre_lines.append(line)

def code1_3_2():
	with open("1.txt") as f:
		for line,que in search(f,"aa",2):
			for pline in que:
				print(pline,end='')
			print(line)
			print('-'*20)

def code1_4_2():
	nums = [1,5,3,5,6,7,8,2,4,5]
	temp = list(nums)
	heapq.heapify(nums)
	i = 0
	for i in range(0,5):
		heapq.heappop(nums)
	print(temp)
	#print(heapq.nlargest(3,nums))
	#print(heapq.nsmallest(3,nums))
def code1_4_2_2():
	bookdict = [
		{"bookname":"vc","price":100,"num":20},
		{"bookname":"python","price":120,"num":10},
		{"bookname":"vb","price":140,"num":9},
		{"bookname":"c++","price":150,"num":8}
	]
	print(heapq.nlargest(2,bookdict,key = lambda x:x["price"]))
if __name__ == '__main__':
	code1_4_2()
