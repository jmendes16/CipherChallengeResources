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

class affine_shift(key_tools):
			
	def __init__(self, message):
		self.message = message
		print "Type in the key for your cipher."
		self.key = []
	
		a = 0
		while a == 0:
			a = raw_input("a = ")
			try:
				a = int(a)
			except ValueError:
				print "Invalid input, integer value required."  
				a = 0
				continue
						
			if not self.coprime(a, 26):
				print "Invalid key, \"a\" is not coprime to 26."
				a = 0
		b = ""
		while type(b) != int:
			b = raw_input("b = ")
			try:
				b = int(b)
			except ValueError:
				print "Invalid input, integer value required (0 is acceptable)."
				b = ""
				continue
		self.key.append(a)
		self.key.append(b)
		
	def ashift(self, message, key):
		ciphertext = ""
		plaintext = message.lower()
		
		for ch in plaintext:
			if ord(ch) > 96 and ord(ch) < 123:
				cich = chr(65 + ((ord(ch) % 97) * key[0] + key[1]) % 26)
				ciphertext += cich
			else:
				ciphertext += ch
		self.ciphertext = ciphertext
		return self.ciphertext

	def deashift(self, message, key):
		dkey = []
	
		for i in range(0, 26):
			if (i*key[0]) % 26 == 1:
				dkey.append(i)
	
		dkey.append(26 - dkey[0]*key[1] % 26)
		return self.ashift(message, dkey).lower()
				
class caesar_shift(affine_shift):

	def __init__(self, message):
		self.message = message
		print "Type in the key for your cipher."
		self.key = [1]
	
		key = 0
		while key == 0:
			key = raw_input("> ")
			try:
				key = int(key)
			except ValueError:
				print "Invalid input, integer value required."  
				key = 0
				continue
		
			if key < 0 or key > 25:
				print "Invalid input, please choose a key between 0 and 25 (inclusive)."
				key = 0
			else:
				self.key.append(key)
			
	def shift(self, message, key):
		self.ciphertext = self.ashift(message, key)
		return self.ciphertext

	def dshift(self, message, key):
		key[1] = 26 - key[1]
		return self.shift(message, key).lower()

class vigenere(edit_message, caesar_shift):
	
	def __init__(self, message):
		super(vigenere, self).__init__()
		self.message = message
		print "Type in the key phrase for your cipher."
		key = ""
	
		while key == "":
			key = raw_input("> ").lower()
			for ch in key:
				if self.alpha.count(ch) != 1:
					print "Invalid choice for key, only letters."
					key = ""
					break
		
		self.key = key
	
	def encrypt(self, message, key):
		ciphertext = ""
		key = self.keep_alpha(key).lower()
		plaintext = message.lower()
		i = 0
	
		for ch in plaintext:
			if self.alpha.count(ch) == 1:
				ciphertext += self.shift(ch, [1, ord(key[i % len(key)]) % 97])
				i += 1
			else:
				ciphertext += ch

		self.ciphertext = ciphertext
		return self.ciphertext

	def decrypt(self, message, key):
		dkey = ""
	
		for ch in key:
			dkey += chr(97 + (26 - ord(ch) % 97) % 26)
			
		return self.encrypt(message, dkey).lower()
