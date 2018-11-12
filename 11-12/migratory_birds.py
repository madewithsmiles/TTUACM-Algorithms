def migratoryBirds(arr):
    count = {k : 0 for k in arr}
    for bird in arr:
        count[bird] += 1
    
    maxBird = (0, 0)
    for bird in count:
        if count[bird] > maxBird[1]:
            maxBird = (bird, count[bird])
        if count[bird] == maxBird[1] and bird < maxBird[0]:
            maxBird = (bird, count[bird])
    return maxBird[0]
