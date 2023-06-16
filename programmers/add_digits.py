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

# 더 간단하게
def solution(n):
    answer = sum(list(map(int, str(n))))
    return answer

# 더 간단하게
def solution(n):
    return sum(int(i) for i in str(n))

# while 문을 사용한 풀이
def solution(n):
		answer = 0
		while n:
			n, r = divmod(n, 10) # n에서 10을 나눈 몫과 나머지를 저장
			answer += r # answer 변수에 r을 계속 더해나간다
		return answer
# n = 1234 라면
# 1234 // 10 = n 123
# 1234 % 10 = r 4
# 1234/10 = 123.4 니까 ! 아하 계속 한자리씩 줄어들게 되는 군...