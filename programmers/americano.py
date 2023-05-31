"""
머쓱이는 추운 날에도 아이스 아메리카노만 마십니다.
아이스 아메리카노는 한잔에 5,500원입니다.
머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때,
머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
"""


def solution(money):
    answer = []
    one_americano = 5500

    count_americano = money//one_americano
    changes_money = money%one_americano

    answer = [count_americano, changes_money]
    return answer

# 여기서 내장함수인 divmod( )를 사용한다면 한 단계 더 깔끔해 질 수 있을 것 같다.
def solution(money):
    one_americano = 5500
    answer = list(divmod(money, one_americano))
    return answer
# divmod() 내장함수는 divmod(a, b) 숫자를 2개의 인자로 받는데,
# a를 b에 나누어 몫과 나머지를 튜플로 반환한다.
# 튜플로 반환된 것을 list() 함수를 사용하여 다시 배열로 만들어준다. 


