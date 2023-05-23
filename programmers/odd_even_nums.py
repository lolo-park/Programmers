"""
정수가 담긴 리스트 num_list가 주어질 때,
num_list의 원소 중 짝수와 홀수의 개수를 담은
열을 return 하도록 solution 함수를 완성해보세요.
"""


def solution(num_list):
    even_nums = []
    odd_nums = []

    for i in num_list:
        if i % 2 == 0:
            even_nums.append(i)
        elif i % 2 != 0:
            odd_nums.append(i)

    answer = [len(even_nums), len(odd_nums)]
    return answer

# 더하기연산자+= , 빼기 연산자 -= 에 좀 더 익숙해지면 심플한 코드가 작성될 수 있을 것 같다.


def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer
