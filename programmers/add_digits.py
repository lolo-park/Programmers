"""
매개변수 : n (정수)
출력 : n의 각 자리숫자의 합을 출력
"""
def solution(n):
    sum_of_digits = 0
    answer = list(map(int, str(n)))
    for i in range(len(answer)):
        sum_of_digits += answer[i]
    return sum_of_digits
