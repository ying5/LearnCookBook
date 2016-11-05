import heapq
from collections import defaultdict
from collections import OrderedDict
from collections import Counter
from operator import itemgetter
from operator import attrgetter
from itertools import groupby
import json
class PriorityQueue(object):
	def __init__(self):
		self._queue = []
		self._index = 0
	def push(self,item,priority):
		heapq.heappush(self._queue,(-priority,self._index,item))
		self._index+=1
	def pop(self):
		return heapq.heappop(self._queue)[-1]
class Items(object):
	def __init__(self,name):
		self._name = name;
	def __repr__(self):
		return self._name
class User(object):
	def __init__(self,uid,name):
		self._id = uid
		self._name = name
	def __repr__(self):
		return 'User({})'.format(self._id)

def code1_5_3():
	return (5,Items("ST"))>(5,Items("ying_5"))

def code1_6_2():
	d = defaultdict(list)
	d['a'].append("ddd")

def code1_7_2():
	d = OrderedDict()
	d['foo'] = 1
	d['bar'] = 2
	d['spam'] = 3
	d['grok'] = 4
	print(json.dumps(d))

def code1_9_2():
	a={'x':1, 'y':2, 'z':3 } 
	b={'x':1, 'w':2, 'h':3 }
	print(a.keys()&b.keys(),a.keys()-b.keys(),a.items()&b.items())
def code1_10_2(items,key=None):
	s  = set()
	for item in items:
		val = item if key is None else key(item) 
		if val not in s:
			yield val
		s.add(val)
def code1_11_2(items):
	share = slice(5,50,2)
	print(share.indices(len(items)))
	for i in range(*share.indices(len(items))):
		print(items[share])
	#print(share.step)
	#del(items[share])
	#print(items)
	#print(l)
def code1_12_2():
	word=['look','look','look','look','look','look','look','look','into','into','into','into','into','into',
	'into','into','the','the','the','the','the','eyes','eyes','eyes','eyes','eyes','eyes','eyes']
	c = Counter(word)
	print(c.most_common(3))
def code1_13_2():
	word = [
		{'fname':'Brian','lname':'Jones','uid':1003,'age':20},
		{'fname':'David','lname':'Beazley','uid':1002,'age':21},
		{'fname':'John','lname':'Cleese','uid':1001,'age':19},
		{'fname':'Big','lname':'Jones','uid':1000,'age':18},
	]
	#print(sorted(word,key=itemgetter('age')))
	print(sorted(word,key = lambda r:(r['age'],r['uid'])))
def code1_14_2():
	users = [User(4,'st'),User(2,'ying_5'),User(3,'yzm')]
	print(sorted(users,key = lambda x:x._id))
	print(sorted(users,key = attrgetter('_id')))

def code1_15_2():
	rows = [
		{'address':'5412 N CLARK','date':'07/01/2012','num':2},
		{'address':'5148 N CLARK','date':'07/04/2012','num':3},
		{'address':'5800 N CLARK','date':'07/02/2012','num':2},
		{'address':'2122 N CLARK','date':'07/03/2012','num':4},
		{'address':'5645 N CLARK','date':'07/01/2012','num':2},
		{'address':'1060 N CLARK','date':'07/05/2012','num':3}
	]
	rows.sort(key = itemgetter('date','num'))
	for sts,items in groupby(rows,itemgetter('date','num')):
		date,num = sts
		print(date,num)
		for item in items:
			print(item)


if __name__ == '__main__':
	#print(list(code1_10_2(l,lambda x:x+1)))
	s = "HelloWorld"
	code1_15_2()