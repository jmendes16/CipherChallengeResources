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