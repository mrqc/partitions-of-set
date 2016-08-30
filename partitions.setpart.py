# 1st proposed algorithm from "a fast algorithm for generating set partitions", the computer journal, vol 32 no 3 1989
# actually in this algorithm is a mistake so this currently is not working
def setpart1(n):
	r = 0
	c = {}
	c[0] = 0
	nl = n - 1
	g = {}
	g[0] = 0

	while True:
		while r < nl:
			r = r + 1
			c[r] = 1
			g[r] = g[r - 1]
		for j in range(1, g[nl] + 2):
			c[n] = j
			print c
		while c[r] > g[r - 1]:
			r = r - 1
		c[r] = c[r] + 1
		if c[r] > g[r]:
			g[r] = c[r]
		if r == 1:
			break
setpart1(4)

# 2nd proposed algorithm from "a fast algorithm for generating set partitions", the computer journal, vol 32 no 3 1989
# actually in this algorithm is a mistake so this currently is not working
def setpart2(n):
	r = 1
	c = {}
	c[1] = 1
	j = 0
	b = {}
	b[0] = 1
	nl = n - 1
	while True:
		while r < nl:
			r = r + 1
			c[r] = 1
			j = j + 1
			b[j] = r
		for j in range(1, n - j + 1):
			c[n] = j
			print c
			print b
		r = b[j]
		c[r] = c[r] + 1
		if c[r] > r - j:
			j = j - 1
		if r == 1:
			break
setpart2(4)


