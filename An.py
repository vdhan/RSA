"""
An's Python library
Author: Hoàng Ân
Copyright © All rights reserved
"""
import math, fractions, hashlib

def isPrime(n = 0):
	"""Check whether a number is prime"""
	if n < 2 or math.isfinite(n) == False:
		return False

	if n % 2 == 0:
		return False if n != 2 else True

	if n % 3 == 0:
		return False if n != 3 else True

	if n % 5 == 0:
		return False if n != 5 else True

	m = math.floor(n ** 0.5)
	for i in range(7, m + 1, 2):
		if n % i == 0:
			return False

	return True

def trim(m):
	"""Trim string"""
	l = m.split()
	return ' '.join(l)

def gcd(*a):
	"""Return the greatest common divisor for 2 or more numbers"""
	if len(a) < 2:
		raise TypeError('gcd() takes at least 2 arguments')

	for i in a:
		if not math.isfinite(i):
			raise TypeError('Parameter Error!')

	b = fractions.gcd(a[0], a[1])
	for i in range(2, len(a)):
		b = fractions.gcd(b, a[i])

	return b

def lcm(*a):
	"""Return the least common multiple for 2 or more numbers"""
	if len(a) < 2:
		raise TypeError('lcm() takes at least 2 arguments')

	for i in a:
		if not math.isfinite(i):
			raise TypeError('Parameter Error!')

	b = bcnn(a[0], a[1])
	for i in range(2, len(a)):
		b = bcnn(b, a[i])

	return b

def bcnn(a, b):
	"""Return the least common multiple for 2 numbers"""
	if math.isfinite(a) == False or math.isfinite(b) == False:
		raise TypeError('Parameter Error!')

	return a * b / fractions.gcd(a, b)

def isFinite(n):
	"""Check if finite number"""
	try:
		a = float(n)
		return math.isfinite(a)
	except:
		return False

def isNum(n):
	"""Check if number (include infinity)"""
	try:
		a = float(n)
		return not math.isnan(a)
	except:
		return False

def isInt(n):
	"""Check if integer"""
	try:
		return n[1:].isdigit() if n[0] in ('-', '+') else n.isdigit()
	except:
		pass

	try:
		return int(n) == n
	except:
		return False

def inverse(a, z = 26):
	"""Return the modular multiplicative inverse of given number"""
	if math.isfinite(a) == False or math.isfinite(z) == False:
		raise TypeError('Parameter Error!')

	a = int(a)
	z = int(z)
	if a < 0:
		a %= z

	if gcd(a, z) == 1:
		n, y, y2 = z, 1, 0
		while a != 0:
			q = z // a
			z, a = a, z % a
			y, y2 = y2 - q * y, y
		return y2 % n

	return 0

def base36encode(n):
	"""Convert integer to hexatridecimal"""
	if not math.isfinite(n):
		raise TypeError('Parameter Error!')

	n = int(n)
	alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	base = ''
	sign = ''

	if n < 0:
		sign = '-'
		n = -n

	if n in range(36):
		return sign + alpha[n]

	while n != 0:
		n, i = n // 36, n % 36
		base = alpha[i] + base

	return sign + base

def encrypt(m, algorithm = 'sha512'):
	"""Hash function for given cryptography (default SHA-512)"""
	h = hashlib.new(algorithm)
	h.update(m.encode('utf-8'))
	return h.hexdigest()

def permutation(n, r):
	"""Return the number of r-permutations of a set with n elements"""
	return math.factorial(n) // math.factorial(n - r)

def combination(n, r):
	"""Return the number of r-combinations of a set with n elements"""
	return math.factorial(n) // math.factorial(n - r) // math.factorial(r)

def rounding(x):
	"""Return the rounding of x"""
	if x < 0:
		x = int(x - 0.5)
	else:
		x = int(x + 0.5)

	return x

def bfs(g, s, d):
	"""Breadth first search"""
	queue = [[s]]

	while queue:
		path = queue.pop(0)
		node = path[-1]
		if node == d:
			return path

		for adjacent in g.get(node, []):
			new_path = list(path)
			new_path.append(adjacent)
			queue.append(new_path)

def dfs(g, s, d, p = None):
	if not p:
		p = []

	p = p + [s]
	if s == d:
		return p

	for node in g[s]:
		if node not in p:
			newpath = dfs(g, node, d, p)
			if newpath:
				return newpath

def isSquare(n):
	"""Check whether a number is square number (i.e. perfect square number)"""
	x = 0
	if n >= 0:
		while x * x < n:
			x += 1

		if x * x == n:
			return True

	return False

def safe_list_get(l, idx, value = None):
	"""List/ tuple safe get"""
	try:
		return l[idx]
	except (IndexError, TypeError):
		return value

if __name__ == '__main__':
	print("An's Python library\nAuthor: Hoàng Ân\nCopyright © All rights reserved")