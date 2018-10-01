# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

# unique(s) iff s has all unique characters (with hashmap)
def unique(s):
	seen = {}
	for c in s:
		if c in seen:
			return False
		seen[c] = 1
	return True

# What if we can't use any additional data structures?
def unique2(s):
	for i in range(len(s)):
		for j in range(len(s)):
			if j != i:
				if s[i] == s[j]:
					return False
	return True
