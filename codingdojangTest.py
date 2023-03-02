import time
import math


'''
    어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한숫자라고 정의했을때
    이 때, n을 d(n)의 제네레이터(generator)라고 한다. 위의 예에서 91은 101의 제네레이터이다.

    어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다. 그런데 반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다. 예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.

    1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.

'''
def d(num):
    return (num + sum([int(n) for n in str(num)]))


a = set(range(5000))
b = set([d(num) for num in range(5000)])
print(sum(a-b))



'''
    10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.

    1000미만의 자연수에서 3,5의 배수의 총합을 구하라.
'''

set3 = set(range(3, 1000, 3))
set5 = set(range(5, 1000, 5))

print(sum(set3 | set5))


summ = 0
        
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        summ += i
    else:
        pass
print(summ)



'''
    1~1000에서 각 숫자의 개수 구하기
'''

item = []
for i in range(1, 1001):
    for j in str(i):
        item.append(int(j))

for i in range(10):
    print(f'{i} : {item.count(i)}개')

dic = {i:0 for i in range(0, 10)}

for i in range(1, 1001):
    for j in str(i):
        dic[int(j)] += 1

print(dic)


'''
    1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오. (단 점들의 배열은 모두 정렬되어있다고 가정한다.)

    예를들어 S={1, 3, 4, 8, 13, 17, 20} 이 주어졌다면, 결과값은 (3, 4)가 될 것이다.
'''

import random

s = list(set(random.randint(1,30) for i in range(8)))
s.sort()

n = 20

ss = []
for i, st in enumerate(s):
    
    if i == len(s)-1:
        break
    if s[i+1] - s[i] < n:
        ss.clear()
        n = s[i+1] - s[i]
        ss.extend([s[i], s[i+1]])
    elif s[i+1] - s[i] == n:
        ss.extend([s[i], s[i+1]])
print(ss)


'''
    10~1000까지 각 숫자 분해하여 곱하기의 전체 합 구하기
'''

def p(num):
    return math.prod([int(n) for n in str(num)])


c = [p(num) for num in range(10, 1001)]
print(sum(c))

print(sum([math.prod([int(n) for n in str(num)]) for num in range(10, 1001) if str(num).find('0') < 0]))

d = [p(num) for num in range(10, 1001) if str(num).find('0') < 0]
print(sum(d))



