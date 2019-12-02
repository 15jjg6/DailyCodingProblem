def P1(array, n):
    numsSeen = {}
    for elem in array:
        if elem in numsSeen:
            return True
        numsSeen[n - elem] = elem
    return False


print(P1([10,10], 20))