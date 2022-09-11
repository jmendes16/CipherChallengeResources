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

class monoalphasub(edit_message):
			
	def __init__(self, message):
		super(monoalphasub, self).__init__()
		self.message = message
		print "Type in the key for your cipher (upper case)."
		print "> %s" % self.alpha

		key = raw_input("> ")
		key = key.upper()
			
		while sorted(list(key)) != list(self.alpha.upper()):
			print "invalid key, please use all letter once only."
			print "Type in the key for your cipher (upper case)."
			print "> %s" % self.alpha

			key = raw_input("> ")
			key = key.upper()
		self.key = key
	
	def emonosub(self, message, key, alphabet):
		ciphertext = ''
		plaintext = message.lower()
	
		for ch in plaintext:
			if ch in alphabet:
				index = alphabet.find(ch)
				ciphertext += key[index]
			else:
				ciphertext += ch
		self.ciphertext = ciphertext
		return self.ciphertext
	
	def dmonosub(self, message, key, alphabet):
		return self.emonosub(message, alphabet, key)
