"""
정수 n 매개변수로 주어질 때,
n 이하의 홀수를 배열로 return 하는 함수
"""


def solution(n):  # n 이 10 이라고 치고

    answer = []

    for i in range(1, n+1):  # 1 부터 10까지 loop
        if i % 2 != 0:  # i 가 홀수면은
            answer.append(i) # 빈 배열인 answer에 차례대로 넣어라

    return answer

# 더 좋은 방법
def solution(n):
    return [i for i in range(1, n+1, 2)]
# 배열을 바로 리턴하는데 포문을 돌려서 해당하는 것들만 들어가도록
# i 라는 변수를 배열에 넣어준다
# 1 부터 시작해서 n+2 까지 for loop 돌린다
# 2씩 증가하도록
# ** 근데 이것의 문제는 홀수 인지 아닌지를 정확하게 측정하지 않고 dict의 data를 어느정도 알고 시작한 것이라
# ** 조금 얍삽한 방법이라~ 할 수 있음