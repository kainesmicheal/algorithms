def caesarCipherEncryptor(string, key):
    encryptedWord = []
	key = key % 26
	for i in range(len(string)):
		encryptedWord.append(helper(string[i], key))
	return "".join(encryptedWord)

def helper(string, key):
	val = ord(string) + key
	if val <= 122:
		return chr(val)
	else:
		return chr(96 + (val % 122))
	
#time complexity is o(n) as we have to iterate through the whole string
#space complexity is o(n) as we are creating a new string

def caesarCipherEncryptor(string, key):
	encryptedString = []
	alphabets = list("abcdefghijklmnopqrstuvwxyz")
	key = key % 26
	for i in range(len(string)):
		encryptedString.append(helper(string[i], key, alphabets))
	return "".join(encryptedString)

def helper(string, key, arr):
	val = arr.index(string) + key
	return arr[val % 26]

#time complexity is o(n) as we are iterating through a string
#space complexity is 0(n) as we are creating a new string

