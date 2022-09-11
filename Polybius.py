class edit_message(object):

	def __init__(self):
		self.alpha = "abcdefghijklmnopqrstuvwxyz"
		self.alphanum = "abcdefghijklmnopqrstuvwxyz1234567890"
		self.alphanumspace = "abcdefghijklmnopqrstuvwxyz1234567890 "
	
	def keep_alpha(self, message):
		clean_string = ""
	
		for ch in message:
			if (ord(ch) > 64 and ord(ch) < 91) or (ord(ch) > 96 and ord(ch) < 123):
				clean_string += ch			
	
		return clean_string
	
	def keep_alphanum(self, message):
		clean_string = ""
	
		for ch in message:
			if (ord(ch) > 64 and ord(ch) < 91) or (ord(ch) > 96 and ord(ch) < 123) or (ord(ch) > 47 and ord(ch) < 58):
				clean_string += ch			
	
		return clean_string
	
	def keep_alphanumspace(self, message):
		clean_string = ""
	
		for ch in message:
			if (ord(ch) > 64 and ord(ch) < 91) or (ord(ch) > 96 and ord(ch) < 123) or ch == " ":
				clean_string += ch
		
		return clean_string
		
class polybius(edit_message):

	def __init__(self, message):
		self.message = message
		self.alpha = "abcdefghiklmnopqrstuvwxyz"
		print "Type in the key for your cipher (upper case, 5 different characters, no spaces)."
		
		key = ""
		while len(key) != 5:
			key = raw_input("> ")
			key = self.keep_alpha(key).upper()
		
			if len(key) != 5: 
				print "invalid key, please make sure there are exactly five characters."
			
			for ch in key:
				if key.count(ch) > 1:
					print "invalid key, please make sure that you do not use the same character more than once in your key."
					key = "123456"
		self.key = key
	
	def encrypt(self, message, key):
		keylist = list(key)
		cipherbet = []
		
		for ch in keylist:
			for i in range(0,5):
				cipherbet.append(ch + keylist[i])
	
		ciphertext = ''
		plaintext = message.lower()
		plaintext.replace('j', 'i')
			
		for ch in plaintext:
			if ch in self.alpha:
				index = self.alpha.find(ch)
				ciphertext += cipherbet[index]
			else:
				ciphertext += ch
		self.ciphertext = ciphertext
		return self.ciphertext
		
	def decrypt(self, message, key):
		keylist = list(key)
		cipherbet = []
		
		for ch in keylist:
			for i in range(0,5):
				cipherbet.append(ch + keylist[i])
			
		plaintext = ''
		ciphertext = self.keep_alpha(message).upper()
	
		for i in range(0, len(ciphertext) / 2):
			cipherchar = ciphertext[2*i] + ciphertext[2*i + 1]
			if cipherchar in cipherbet:
				index = cipherbet.index(cipherchar)
				plaintext += self.alpha[index]
			else:
				plaintext += cipherchar
		self.plaintext = plaintext
		return self.plaintext
