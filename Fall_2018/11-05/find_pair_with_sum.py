def FindPairWithSum(data, total):
	comp = set()
	for num in data:
		if num in comp:
			return True
		comp.add(total - num)
	return False

def FindPairWithSum2(data, total):
	lo = 0
	hi = len(data) - 1
	while lo < hi:
		tot = data[lo] + data[hi]
		if tot == total: return True
		if tot < total: lo += 1
		if tot > total: hi -= 1
	return False
