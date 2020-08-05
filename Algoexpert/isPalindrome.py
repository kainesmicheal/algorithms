def isPalindrome(string):
	newString = ""
	for i in reversed(range(len(string))):
		newString += string[i]
	return string == newString
#time complexity is o(n^2) as the string contcatation take o(n)
#space complexity is o(n) as use a new string

def isPalindrome(string):
	arrayOfChars = []
	for i in reversed(range(len(string))):
		arrayOfChars.append(string[i])
	return string == "".join(arrayOfChars)
#time complexity is o(n) as we are using arrary join
#space complexity is o(n) as we are using an extra array

def isPalindrome(string, i = 0):
	j = len(string) - 1 - i
	return True if i >= j else string[i] == string[j] and isPalindrome(string, i+1)

#time complexity is o(n) as we are iterating through a whole string
#space complexity is 0(n) as no. of frames in call stack due to recusion

def isPalindrome(string):
    leftIdx = 0
	rightIdx = len(string) - 1
	while leftIdx < rightIdx:
		if string[leftIdx] != string[rightIdx]:
			return False
		leftIdx += 1
		rightIdx -= 1
	return True
#time complexity is o(n) as we iterating through the full string
#space complexity is o(1) as we not using any other space 
