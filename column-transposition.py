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
		
class key_tools(object):
	
	def gcd(self, a, b):
		while b!= 0:
			a, b = b, a % b
		return a

	def coprime(self, a, b):
		return self.gcd(a, b) == 1
	
	def factorise(self, num):
		if type(num) != int:
			return("Error: Input is not an integer.")
		
		factors = []
	
		for i in range(1, num + 1):
			test = num % i
		
			if test == 0:
				factors.append(i)
			
		return factors

class ctransposition(key_tools, edit_message):

	def __init__(self, message):
		super(ctransposition, self).__init__()
		self.message = self.keep_alpha(message)
		n = len(self.message)
			
		print "possible keys are: ", self.factorise(n)
		print "Type in the key for your cipher."

		self.key = int(raw_input("> "))
	
	def ctranspose_encrypt(self, message, key):
		self.ciphertext = ''
		i = 0
		while i < key:
			for p in range(0, len(message)/key):
				self.ciphertext += message[i + p * key].upper()
			i += 1
		return self.ciphertext
	
	def ctranspose_decrypt(self, message, key):
		dkey = len(message)/key
		return self.ctranspose_encrypt(message, dkey).lower()
