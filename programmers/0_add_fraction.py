"""
첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1,
두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다.
두 분수를 더한 값을 기약 분수로 나타냈을 때
분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
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
    # 여기서 기약분수 화 해주어야함. -> 아니 !! 최소공배수를 통한 통분은 약분하지 않아도 된다 (제일 밑에 다시 풀이)
    # c 와 i 의 최대공약수(j)를 구하라
    for j in range(min(c,i), 0, -1): # c와 i 중 작은 수부터 0까지 -1씩 내려가며 loop
        if c % j == 0 and i % j == 0:
            break # 위 조건에 만족하면 멈추어라 (j)가 구해진다

    numer = math.ceil(c/j) # 소수점 떨구기
    denom = math.ceil(i/j) # 소수점 떨구기

    answer = [numer, denom]  # 통분하여 분자는 그대로 놔두고 분자만 더해주면 분수의 덧셈  완료
    # 그러나 여기서 기약분수로 만들어 [분자, 분모]를 구하라고 했다.
    # 분자, 분모의 최소공배수를 다시 구해서 각각 나누어 주면 된다.
    return answer

# 더 clever한 풀이 ......
import math


def solution(numer1, denom1, numer2, denom2):

    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    gcd = math.gcd(numer, denom) # gcd는 인자로 들어온 숫자들의 최대 공약수(정수)를 반환합니다.
    return [numer//gcd, denom//gcd]


# 내 풀이 최종 수정
import math


def solution(numer1, denom1, numer2, denom2):

    for gcd in range(max(denom1, denom2), (denom1*denom2)+1):
        # 두 분모 중에 큰 값 부터 - 두 분모를 곱한 값 까지
        #
        if gcd % denom1 == 0 and gcd % denom2 == 0:
            break #

    reduc_num_1 = int(gcd / denom1)
    reduc_num_2 = int(gcd / denom2)
    # 최대공배수로 분모를 맞추고 거기에 곱해진 값을 분자에 각각 곱해주어야하니까
    # 곱해진 값을 알기 위해서 최대공배수 나누기 분모1,2를 해주었다.
    # 최대공배수가 되기위해 얼마를 곱해야 분모1,2가 되는지를 알아야하니까

    result_reduction_1 = numer1 * reduc_num_1
    result_reduction_2 = numer2 * reduc_num_2

    numer_add = result_reduction_1 + result_reduction_2

    answer = [numer_add, gcd]
    return answer

# 변수명이 너무 개똥망 -> 그래서 수정함
# reduction : 통분
# simplify : 약분
# gcd : 최대공배수

