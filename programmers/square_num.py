"""
어떤 자연수를 제곱(2)했을 때 나오는 정수를 제곱수
매개변수 : n
n이 제곱수라면 1 아니라면 2
3의 2제곱 = 9
144가 제곱수인지 아닌지 어떻게 알 수 있나 ?
144 는 12의 제곱
"""


def solution(n):
    for i in range(n):
        if n == pow(i, 2):

            if i > 0:
                return 1
            elif i.isNull() == True:
                return 2


print(solution(144))  # None 의 이유는 무엇인가
