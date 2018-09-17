def digitSum(n, k):
    # Complete this function
    if len(n) == 1: return n
    else:
        total = 0
        for digit in n:
          total += int(digit)
        total *= k
        return digitSum(str(total), 1)
