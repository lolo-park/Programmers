"""
첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1,
두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다.
두 분수를 더한 값을 기약 분수로 나타냈을 때
분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

range()함수 : 시작 숫자와 끝 숫자를 지정하려면 range(시작 숫자, 끝 숫자) 형태를 사용하는데, 이때 끝 숫자는 포함 되지 않는다.

denom1 과 denom2 를 최소공배수를 이용하여 맞춰주고
최소공배수를 구했어 만약에 그걸 i 라고 쳤을 때
denom1 * x = i
denom2 * y = i

x = i/denom1
y = i/denom2

a = numer1 * x
b = numer2 * y

answer = [a+b, i]
return



"""

import math


def solution(numer1, denom1, numer2, denom2):
    for i in range(max(denom1, denom2), (denom1 * denom2) + 1):
        # 두 분모중 큰 수 부터 시작 두 분모를 곱한 값까지 for loop을 돌려서

        if i % denom1 == 0 and i % denom2 == 0:  # 둘다 나머지가 0 일경우가 최소 공배수 i 이다
            break

    x = i / denom1  # 최소공배수를 각 분자에 나눈 값을 x와 y에 담아서
    y = i / denom2

    a = math.ceil(numer1 * x)  # 각 분자에 곱해주어 통분 한다
    b = math.ceil(numer2 * y)

    c = a + b
    # 여기서 기약분수 화 해주어야함.
    # c 와 i 의 최대공약수(j)를 구하라
    for j in range(min(c,i), 0, -1): # c와 i 중 작은 수부터 0까지 -1씩 내려가며 loop
        if c % j == 0 and i % j == 0:햣
            break # 위 조건에 만족하면 멈추어라 (j)가 구해진다

    numer = math.ceil(c/j) # 소수점 떨구기
    denom = math.ceil(i/j) # 소수점 떨구기

    answer = [numer, denom]  # 통분하여 분자는 그대로 놔두고 분자만 더해주면 분수의 덧셈 완료
    # 그러나 여기서 기약분수로 만들어 [분자, 분모]를 구하라고 했다.
    # 분자, 분모의 최소공배수를 다시 구해서 각각 나누어 주면 된다.
    return answer
