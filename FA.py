import Global
import WordDict
def getGenerator():
	for s in Global.STRING:
		if s == '\n':continue
		yield s
def getChar(temp):
	try:
		char = next(temp)
		print(char)
		if str.isdigit(char):
			Global.CurrentNum = int(char)
			return Global.DIGIT
		if char =='.':
			return Global.POINT
		if char =='e' or char =='E':
			return Global.Letter
		if char == '+':
			return Global.PLUS
		if char == '-':
			return Global.MINUS
		return Global.Other
	except:
		return Global.EOF
def excute(state,char):
		if state == 0:
			if char == Global.DIGIT:
				Global.CurrentState = 1
				Global.Result = Global.CurrentNum
			else:
				Global.CurrentState = Global.EndState

		#########终止状态#############################
		if state == 1:  
			if char == Global.DIGIT:
				Global.Result = Global.Result*10 + Global.CurrentNum
			elif char == Global.POINT:
				Global.CurrentState = 2
				Global.DigitPoint = 0
			elif char == Global.Letter:
				Global.CurrentState = 4
				Global.DigitE = 0
			else:
				if char == Global.EOF:
					Global.CurrentState = Global.EndState
					Global.Answer = Global.Result
		##########################################################
		if state == 2:
			if char == Global.DIGIT:
				Global.CurrentState = 3
				Global.Result = Global.Result * 10 +Global.CurrentNum
				Global.DigitPoint = Global.DigitPoint+1
			else:
				Global.CurrentState = Global.EndState
		if state == 3:
			if char == Global.DIGIT:
				Global.Result = Global.Result*10 + Global.CurrentNum
				Global.DigitPoint = Global.DigitPoint+1
			elif char == Global.Letter:
				Global.CurrentState = 4
				Global.DigitE = 0
			elif char == Global.EOF:
				Global.Answer = Global.Result / (10**Global.DigitPoint)
				Global.CurrentState = Global.EndState
			else:
				Global.CurrentState = Global.EndState
		if state == 4:
			if char == Global.DIGIT:
				Global.IndexSymbol = 1
				Global.CurrentState = 6
				Global.Result = Global.Result * 10 * Global.CurrentNum
			elif char == Global.MINUS:
				Global.CurrentState = 5
				Global.IndexSymbol = -1
			else:
				Global.CurrentState = Global.EndState

		if state == 5:
			if char == Global.DIGIT:
				Global.Result = Global.Result / (10 * Global.CurrentNum)
		if state == 6:
			pass
def init():
	Global.CurrentState = Global.StartState
	Global.Result = 0
	Global.Answer = -1
	Global.DigitE = 0
	Global.DigitPoint = 0
	Global.IndexSymbol = 0
	Global.Index = 0
if __name__ == '__main__':
	with open("D://in.txt") as f:
		for line in f:
			if line.startswith('#'):continue
			Global.STRING = line
			init()
			temp = getGenerator()
			while(Global.CurrentState != Global.EndState):
				char = getChar(temp)
				#print(char)
				excute(Global.CurrentState,char)
			print(Global.Answer)