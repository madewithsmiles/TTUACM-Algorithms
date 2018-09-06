import math

def Euler4():
	def IsPalindrome(s):
		return s[::-1] == s 			# Check if s stepped through backwards is the same as s
	largest = 0
	for i in range(100, 1000):			# Loop through all 3 digit numbers
		for j in range(100, 1000):		# Loop through all 3 digit numbers
			prod = i * j
			if IsPalindrome(str(prod)): # If the product is a palindrome
				if prod > largest: 		# And prod is bigger than our current largest product
					largest = prod 
	return largest

def euler7():
	def isPrime(n):
		if n < 2: return False
		for i in range(2, int(math.sqrt(n))+1):
			if n % i == 0: return False
		return True
	total = 0
	n = 0
	while total < 10001:
		n += 1
		if isPrime(n): total += 1
	return n

def euler8():
	num = """73167176531330624919225119674426574742355349194934
	96983520312774506326239578318016984801869478851843
	85861560789112949495459501737958331952853208805511
	12540698747158523863050715693290963295227443043557
	66896648950445244523161731856403098711121722383113
	62229893423380308135336276614282806444486645238749
	30358907296290491560440772390713810515859307960866
	70172427121883998797908792274921901699720888093776
	65727333001053367881220235421809751254540594752243
	52584907711670556013604839586446706324415722155397
	53697817977846174064955149290862569321978468622482
	83972241375657056057490261407972968652414535100474
	82166370484403199890008895243450658541227588666881
	16427171479924442928230863465674813919123162824586
	17866458359124566529476545682848912883142607690042
	24219022671055626321111109370544217506941658960408
	07198403850962455444362981230987879927244284909188
	84580156166097919133875499200524063689912560717606
	05886116467109405077541002256983155200055935729725
	71636269561882670428252483600823257530420752963450"""

	num = num.replace('\n\t', '')

	largestProd = 0
	for i in range(len(num) - 12):
		# If the product begins with a 0, the end product will be 0
		if num[i] == "0": continue

		# Start off our product
		prod = int(num[i])

		# Loop through the next 12 digits and multiply
		for j in range(1,13):
			prod *= int(num[i+j])
			if prod == 0: break

		if prod > largestProd: 
			largestProd = prod

	return largestProd

print(euler8())

def euler9():
	for a in range(1,1000):
		for b in range(1,1000):
			c = math.sqrt(a**2 + b**2)
			if a + b + c == 1000:
				return a*b*c

def euler10():
	def isPrime(n):
		if n < 2: return False
		for i in range(2, int(math.sqrt(n))+1):
			if n % i == 0: return False
		return True
	total = 0
	for n in range(2000000):
		if isPrime(n): total += n
	return total

def euler12():
	def numDivisors(n):
		return len([i for i in range(1,n) if n % i == 0])
	triNum = 1
	step = 2
	while numDivisors(triNum) <= 500:
		triNum += step
		step += 1
	return triNum

def euler14():
	def collatz(n):
		if n % 2 == 0: return n // 2
		return 3 * n + 1
	largest = 0
	largestLen = 0
	for start in range(1,1000000):
		cur = start
		length = 1
		while cur != 1:
			cur = collatz(cur)
			length += 1
		if length > largestLen: 
			largestLen = length
			largest = start
	return largest

def euler15():
	def sumSquares(n, size):
		total = 0
		for i in range(size**2):
			total += n ** 2
			n += 1
		return total
	return sumSquares(2,20)


def euler16(n):
	return sum([int(i) for i in str(math.factorial(n))])

def euler21():
	
	# Returns the sum of the divisors of n 
	def sumDivs(n):
		return sum([i for i in range(1, n) if n % i == 0])

	# Returns a tuple containing the sumDivs(n) and n if sumDivs(sumDivs(n)) is equal to n, otherwise (None, None)
	def amicable(n):
		total = sumDivs(n)
		return (total, n) if sumDivs(total) == n else (None, None)

	# Initialize seen list, keeps track of all amicable numbers we have seen in the past
	seen = []
	total = 0

	# Loop through all numbers under 10,000
	for i in range(10000):
		x,y = amicable(i)
		# Problem specifies that x cannot equal y, also if x is None, then the number is not amicable
		if x == y or x == None: continue
		# Do not add repeats to the total
		if x not in seen:
			# Add numbers to total and to list of seen numbers
			total += x + y
			seen.extend([x,y])
	return total

def euler25():
	def fib(n):	return ((1+math.sqrt(5))**n-(1-math.sqrt(5))**n)/(2**n*math.sqrt(5))
	print(len(fib(1004)))

def euler29():
	a = b = range(2,101)
	nums = []
	for x in a:
		for y in b:
			if x**y not in nums:
				nums.append(x**y)
	return len(nums)

def euler36():
	def d2b(n):
		if n == 0: return '0'
		return bin(n)[2:]
	def pal(n):
		return n == n[::-1]
	total = 0
	for i in range(1000000):
		if pal(d2b(i)) and pal(str(i)):
			total += i
	return total

def euler36v2():
	def d2b(n):	return '0' if not n else bin(n)[2:]
	def pal(s): return s == s[::-1]
	return sum([i for i in range(1000000) if pal(d2b(i)) and pal(str(i))])


def euler74():
	def sumFacs(n):
		return sum([math.factorial(int(i)) for i in str(n)])
	totalChains = 0
	for i in range(1000000):
		pastNums = []
		start = i
		chains = 0
		while start not in pastNums:
			pastNums.append(start)
			start = sumFacs(start)
			chains += 1
		if chains == 60:
			totalChains += 1
	return totalChains





