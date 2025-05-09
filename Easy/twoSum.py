def twoSum(list, target):
    indexNum = []
    sum = 0
    for i in range(len(list)):
        for n in range(len(list)):
            if list[i] == list[n]:
                sum = 0
            else:
                sum = list[i] + list[n]
                if sum == target:
                    indexNum.append(i)
                    indexNum.append(n)
        if len(indexNum) == 2:
            break
    return indexNum
