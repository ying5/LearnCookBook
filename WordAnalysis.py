import Global
import WordDict
class WordAnalysis(object):
	def __init__(self):
		self.__word = ""
		self.__dict = ["int","string","float","void"]
		self.__Retract = 0
		self.__index = 0
	def setFile(self,filepath):
		self.__filepath = filepath
		
	def __getCharGenerator(self):
		for char in self.__string:
			yield char
	def __getchar(self):
		try:
			char = next(self.__generator)
			self.__char = char
			if str.isdigit(char):
				return Global.DIGIT
			if char =='.':
				return Global.POINT
			if char == '+':
				return Global.PLUS
			if char == '-':
				return Global.MINUS
			if char == '\n':
				return Global.ENTER
			if char == '<':
				return Global.LEFTEQUAL
			if char == '>':
				return Global.RightEQUAL
			if char == '=':
				return Global.EQUAL
			if str.isalpha(char):
				return Global.Letter
			if char == ' ':
				return Global.SPACE
			return Global.Other
		except:
			return Global.EOF
	def excute(self,state,char):
		if state == 0:
			if char == Global.Letter:
				self.__state = 1
				self.__word = self.__word+self.__char
			elif char == Global.DIGIT:
				self.__state = 3
				self.__word = self.__word+self.__char
			elif char == Global.LEFTEQUAL:
				self.__state = 5
				self.__word = self.__word+self.__char
			elif char == Global.EQUAL:
				self.__state = 9
				self.__word = self.__word+self.__char
			elif char == Global.RIGHTEQUAL:
				self.__state = 10
			else:
				self.__state = Global.EndState
				self.__index = "WRONG"
				self.__word = "WRONG"
		if state == 1:
			if char == Global.Letter or char ==Global.DIGIT:
				self.__word = self.__word+self.__char
			#if char == Global.ENTER or char == Global.SPACE or char ==Global.EOF:
			else:
				if self.__word in self.__dict:
					self.__index = WordDict.KEYWORD
				else:
					self.__index = WordDict.IDENTIFY
				self.__Retract = 1
				self.__state = Global.EndState
		if state == 3:
			if char == Global.DIGIT:
				self.__word = self.__word+self.__char
			else:
				self.__index = WordDict.NUMBER
				self.__state = Global.EndState
		if state == 5:
			if char == Global.EQUAL:
				self.__index = WordDict.OPERATOR_LE
				self.__state = Global.EndState
				self.__word = self.__word+self.__char
			elif char == Global.LEFTEQUAL:
				self.__index = WordDict.OPERATOR_LE
				self.__state = Global.EndState
				self.__word = self.__word + self.__char
			else:
				self.__index = WordDict.OPERATOR_L
				self.__state = Global.EndState
				self.__Retract = 1
		if state == 9:
			self.__state = Global.EndState
			self.__index = WordDict.OPERATOR_E
			self.__Retract = 1
		if state == 10:
			if char == Global.EQUAL:
				self.__state = Global.EndState
				self.__index = WordDict.OPERATOR_RE
				self.__word = self.__word +self.__char
			else:
				self.__Retract = 1
				self.__index = WordDict.OPERATOR_R
				self.__state = Global.EndState


	def getWord(self):
		with open(self.__filepath) as f:
			for line in f:
				self.__string = line
				self.__generator = self.__getCharGenerator()
				char = self.__getchar()
				while(char!=Global.ENTER and char !=Global.EOF):
					self.__state = Global.StartState
					while(self.__state != Global.EndState):
						self.excute(self.__state,char)
						if self.__Retract == 0:
							char = self.__getchar()
						else:
							self.__Retract = 0
					if self.__word !="WRONG":
						yield self.__index,self.__word
					self.__word = ""
if __name__ == '__main__':
	l = WordAnalysis()
	l.setFile("D://in.txt")
	t = l.getWord()
	for i in t:
		print(i)