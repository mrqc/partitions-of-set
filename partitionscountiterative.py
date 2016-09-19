import sys

def partitions(n, k):
	codeword = [1 for _ in range(0, n)]
	while True:
		print "partitions" + str(n) + "_" + str(k) + ".append(" + str(codeword) + ")"
		startIndex = n - 1
		while startIndex >= 0:
			maxValue = max(codeword[0 : startIndex])
			codewordAtStartIndex = codeword[startIndex]
			if maxValue > k or codewordAtStartIndex > maxValue or codewordAtStartIndex >= k:
				codeword[startIndex] = 1
				startIndex -= 1
			else:
				codeword[startIndex] += 1
				break

# this is an enhanced implementation with caching some values which only makes sense for large sets, still under test

'''
def partitions():
	codeword = [1 for digitIndex in range(0, n)]
	maxValue = 1
	maxValueIndex = 1
	while True:
		#print codeword
		startIndex = n - 1
		maxValue = max(codeword[0 : startIndex])
		maxValueIndex = codeword.index(maxValue)
		while startIndex >= 0:
			#maxValue = max(codeword[0 : startIndex])
			if startIndex < maxValueIndex:
				maxValue = max(codeword[0 : startIndex])
				maxValueIndex = codeword.index(maxValue)
			codewordAtStartIndex = codeword[startIndex]
			if codewordAtStartIndex > maxValue or maxValue > k or codewordAtStartIndex >= k:
				codeword[startIndex] = 1
				startIndex -= 1
				if startIndex >= maxValueIndex:
					maxValue = max(codeword[0 : startIndex])
					maxValueIndex = codeword.index(maxValue)
			else:
				codeword[startIndex] += 1
				if startIndex - 1 >= maxValueIndex and startIndex > 1:
					maxValue = max(codeword[0 : startIndex - 1])
					maxValueIndex = codeword.index(maxValue)
				break
'''

n = 4
k = 4
if len(sys.argv) > 1:
	n = int(sys.argv[1])
	k = n

print "partitions" + str(n) + "_" + str(k) + " = []"

try:
	partitions(n, k)
except:
	pass

