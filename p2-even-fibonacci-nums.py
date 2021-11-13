def generateFibonnaciSeq(limit):
    x = 1
    y = 1
    res = []
    while(y < limit):
        res.append(y)
        temp = y
        y += x
        x = temp
    return res

def getSumOfEvenValues(nums):
    res = 0
    for num in nums:
        if num % 2 == 0:
            res += num
    return res

print(getSumOfEvenValues(generateFibonnaciSeq(4000000)))