"""
양꼬치 10인분에 음료수 1개 서비스
양꼬치1인분 12,000 음료수 2,000
양꼬치 n인분, 음료수 k개 얼마를 지불하는지 return하는 solution 함수
n = 10, k = 1

n = 20, k = 2
"""

def solution(n, k):

    lamb = n * 12000
    drink = k * 2000

    if n % 10 == 0: # n이 10의 배수일경우에만 하면 되겠다. 아니야..
        k =+ 1

    answer =