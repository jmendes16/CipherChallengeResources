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


class freq_analysis(edit_message): 
	
	def __init__(self, message):
		super(freq_analysis, self).__init__()
		preanalysis = self.keep_alpha(message).lower()
		n = len(preanalysis)
		slfreq = []
		dbfreq = []
		trfreq = []
		qdfreq = []
		qnfreq = []
						
		for ch in self.alpha:
			slfreq.append([ch, preanalysis.count(ch)])

		self.slfreqs = sorted(slfreq, key = lambda freq: freq[1], reverse = True)

		for i in range(0, n - 1):
			chs = preanalysis[i] + preanalysis[i + 1]
			if dbfreq.count([chs, preanalysis.count(chs)]) == 0:
				if preanalysis.count(chs) > 2:
					dbfreq.append([chs, preanalysis.count(chs)])

		self.dbfreqs = sorted(dbfreq, key = lambda freq: freq[1], reverse = True)

		for i in range(0, n - 2):
			chs = preanalysis[i] + preanalysis[i + 1] + preanalysis[i + 2]
			if trfreq.count([chs, preanalysis.count(chs)]) == 0:
				if preanalysis.count(chs) > 2:
					trfreq.append([chs, preanalysis.count(chs)])

		self.trfreqs = sorted(trfreq, key = lambda freq: freq[1], reverse = True)
		
		for i in range(0, n - 3):
			chs = preanalysis[i] + preanalysis[i + 1] + preanalysis[i + 2] + preanalysis[i + 3]
			if qdfreq.count([chs, preanalysis.count(chs)]) == 0:
				if preanalysis.count(chs) > 2:
					qdfreq.append([chs, preanalysis.count(chs)])

		self.qdfreqs = sorted(qdfreq, key = lambda freq: freq[1], reverse = True)
		
		for i in range(0, n - 4):
			chs = preanalysis[i] + preanalysis[i + 1] + preanalysis[i + 2] + preanalysis[i + 3] + preanalysis[i + 4]
			if qnfreq.count([chs, preanalysis.count(chs)]) == 0:
				if preanalysis.count(chs) > 2:
					qnfreq.append([chs, preanalysis.count(chs)])

		self.qnfreqs = sorted(qnfreq, key = lambda freq: freq[1], reverse = True)
			
		self.preanalysis = preanalysis
		
	def analyse(self):
		print "Single character frequencies:\tDouble character frequencies:\tTriple character frequencies:\n"
		gpsz = sorted([[self.slfreqs, len(self.slfreqs)], [self.dbfreqs, len(self.dbfreqs)], [self.trfreqs, len(self.trfreqs)]], key = lambda freq: freq[1])

		for i in range(0, gpsz[2][1] - gpsz[1][1]):
			gpsz[1][0].append([" ", " "])

		for i in range(0, gpsz[2][1] - gpsz[0][1]):
			gpsz[0][0].append([" ", " "])

		for i in range(0, gpsz[2][1]):
			print self.slfreqs[i][0], self.slfreqs[i][1], "\t\t\t\t", self.dbfreqs[i][0], self.dbfreqs[i][1], "\t\t\t\t", self.trfreqs[i][0], self.trfreqs[i][1]
		return
