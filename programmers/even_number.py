"""
정수 n이 주어질 때, n 이하의 짝수를 모두 더한 값을 return
"""

def number(n):
    answer = 0
    for i in range(n+1): # n+1 해주는 이유는 range()함수는 인풋값을 제외하고 그 전까지의 숫자를 리스트로 출력하기 때문
        if i % 2 == 0:
            answer += i # 연산자 += 왼쪽 변수에 오른쪽 값을 더하고 변수에 그 값을 다시 저장.
    return answer

print(number(10))