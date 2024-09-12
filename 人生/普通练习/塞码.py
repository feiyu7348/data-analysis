
def func(n):
    hashtable = [0] * 20
    res = 0
    for nums in n:
        gap = nums[1] - nums[0]
        if gap == 1:
            if hashtable[nums[1]] == 0:
                hashtable[nums[1]] += 1
            else:
                res += 1
        elif gap > 1:
            for i in range(gap):
                if hashtable[nums[0] + 1 + i] == 0:
                    hashtable[nums[0] + 1 + i] += 1
                else:
                    res += 1
                    break

    return res

#
# n = [[1, 2], [1, 2], [1, 2]]
# n = [[1, 2], [2, 3], [3, 4], [1, 3]]
# print(func(n))

n = input().lstrip('[')
n = n.rstrip(']')
n = n.strip(' ')
m = n.split(', ')
n = []
for i in m:
    k = [int(i[1]), int(i[3])]
    n.append(k)

print(func(n))
