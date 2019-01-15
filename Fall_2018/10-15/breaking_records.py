def breakingRecords(scores):
    l, h = 0, 0
    ls, hs, = scores[0], scores[0]
    for score in scores:
        if score > hs:
            h += 1
            hs = score
        if score < ls:
            l += 1
            ls = score
    return [h, l]
