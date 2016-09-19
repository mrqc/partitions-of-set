
def partitions():
	global n
	global k
	codeword = [1 for digitIndex in range(0, n)]
	while True:
		print codeword
		codeword = increment(codeword, n - 1)

def increment(codeword, startIndex):
	global n
	global k
	maxValue = max(codeword[0 : startIndex])
	if codeword[startIndex] > maxValue:
		codeword[startIndex] = 1
		codeword = increment(codeword, startIndex - 1)
	else:
		if maxValue <= k and codeword[startIndex] < k:
			codeword[startIndex] += 1
		else:
			codeword[startIndex] = 1
			codeword = increment(codeword, startIndex - 1)
	return codeword

n = 4
k = 4
try:
	partitions()
	pass
except:
	pass

