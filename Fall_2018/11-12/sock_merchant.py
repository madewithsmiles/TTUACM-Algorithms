def sockMerchant(n, ar):
    
    count = {k : 0 for k in ar}
    pairs = 0
    for sock in ar:
        count[sock] += 1
        if count[sock] == 2:
            pairs += 1
            count[sock] = 0
    return pairs
