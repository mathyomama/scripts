class converter:
	"""This class will make conversion to and from Roman numerals easy"""

	def __init__(self, romanNumeral):
		"""Takes in a Roman numeral string"""
		self.romanNumeral = romanNumeral
		self.value = self.r_to_d(romanNumeral)
		self.romanNumeralMinimal = self.d_to_r_minimal(self.value)

	def r_to_d(self, romanNumeral):
		"""converts roman numerals to decimal form"""
		dictionary = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
		prevDigit = 0
		value = 0
		for i in reversed(romanNumeral):
			nextDigit = dictionary[i]
			#subtractive pair rule
			if nextDigit < prevDigit:
				value -= nextDigit
			else:
				value += nextDigit
			prevDigit = nextDigit
		return value

	def d_to_r_minimal(self, number):
		"""converts decimal form to minimal Roman numerals"""
		dictionary = {4:('M',), 3:('C', 'D'), 2:('X', 'L'), 1:('I', 'V')}
		#thousand's and beyond digit
		string = (number//1000)*dictionary[4][0]
		#The rest of the digits
		for i in reversed(range(1, 4)):
			digit = (number//10**(i - 1))%10
			if digit == 9:
				string += dictionary[i][0] + dictionary[i + 1][0]
			elif digit < 9 and digit > 4:
				string += dictionary[i][1] + (digit%5)*dictionary[i][0]
			elif digit == 4:
				string += dictionary[i][0] + dictionary[i][1]
			elif digit < 4:
				string += (digit%5)*dictionary[i][0]
		return string

	def get_roman_numeral(self):
		return self.romanNumeral

	def get_value(self):
		return self.valuet

	def get_roman_numeral_minimal(self):
		return self.romanNumeralMinimal

	def get_excess(self):
		return (len(self.get_roman_numeral()) - len(self.get_roman_numeral_minimal()))


foo = open("roman.txt")
sum = 0
for line in foo:
	romanNumeral = line.strip()
	x = converter(romanNumeral)
	sum += x.get_excess()


print(sum)

