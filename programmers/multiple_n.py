"""
매개변수 : 정수 n과 정수 배열 numlist
return : numlist에서 n의 배수가 아닌 수들을 제거한 배열
"""
def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)
    return answer

# 리스트 컴프리헨션
def solution(n, numlist):
    answer = [i for i in numlist if i % n == 0]
    return answer

