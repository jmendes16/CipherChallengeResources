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

class kasiski(freq_analysis, key_tools):

	def __init__(self, message):
		super(kasiski, self).__init__(message)
			
	def test(self):
		n = len(self.preanalysis)
		trgaps = []
		qdgaps = []
		qngaps = []
		allgaps = []
		
		for seq in self.trfreqs:
			str = seq[0]
			i = self.preanalysis.find(str) + 1
			gaps = [str]
			while self.preanalysis[i:n].count(str) > 0:
				gaps.append(self.preanalysis[i:n].find(str) + 1)
				i += self.preanalysis[i:n].find(str) + 1
			trgaps.append(gaps)
		
		for seq in self.qdfreqs:
			str = seq[0]
			i = self.preanalysis.find(str) + 1
			gaps = [str]
			while self.preanalysis[i:n].count(str) > 0:
				gaps.append(self.preanalysis[i:n].find(str) + 1)
				i += self.preanalysis[i:n].find(str) + 1
			qdgaps.append(gaps)
		
		for seq in self.qnfreqs:
			str = seq[0]
			i = self.preanalysis.find(str) + 1
			gaps = [str]
			while self.preanalysis[i:n].count(str) > 0:
				gaps.append(self.preanalysis[i:n].find(str) + 1)
				i += self.preanalysis[i:n].find(str) + 1
			qngaps.append(gaps)
		
		print "Trigram\t\tFactors of gaps"
		for i in trgaps:
			print i[0],
			for j in range(1, len(i)):
				factors = self.factorise(i[j])
				for f in self.factorise(i[j]):
					if f > 32 or f < 2:
						factors.remove(f)
				print "\t\t", factors
				for k in factors:
					allgaps.append(k)

		print "Quadgram\tFactors of gaps"
		for i in qdgaps:
			print i[0],
			for j in range(1, len(i)):
				factors = self.factorise(i[j])
				for f in self.factorise(i[j]):
					if f > 32 or f < 2:
						factors.remove(f)
				print "\t\t", factors
				for k in factors:
					allgaps.append(k)
		
		print "Quingram\tFactors of gaps"
		for i in qngaps:
			print i[0],
			for j in range(1, len(i)):
				factors = self.factorise(i[j])
				for f in self.factorise(i[j]):
					if f > 32 or f < 2:
						factors.remove(f)
				print "\t\t", factors
				for k in factors:
					allgaps.append(k)
		
		allgaps = sorted(allgaps)
		g = max(set(allgaps), key = allgaps.count)
		print "The most likely key size is: ", g
		n = allgaps.count(g)
		allgaps2 = allgaps
		for i in range(0, n):
			del allgaps2[allgaps2.index(g)]
		print "The next most likely key size is: ", max(set(allgaps2), key = allgaps2.count)
		
		return g
