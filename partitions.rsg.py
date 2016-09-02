def gen(s, largest, currentLength, desiredLength):
	if currentLength == desiredLength:
		print s
		return
	for i in range(0, largest + 1):
		gen(int(s) + i, i + 1, currentLength + 1, desiredLength)

gen("1234", 1, 4, 3)
