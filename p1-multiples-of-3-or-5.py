def getMultiples(number1, number2, limit):
    res = []
    for num in range(limit):
        if num % number1 == 0 or num % number2 == 0:
            res.append(num)
    return res

def getSum(numbers):
    res = 0
    for num in numbers:
        res += num
    return res

print(getSum(getMultiples(3, 5, 1000)))