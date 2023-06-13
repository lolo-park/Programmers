"""
두 정수 A와 B를 입력 받은 다음, A+B를 출력하는 프로그램을 작성하시오.
"""
# def add (A, B):
#     result = A + B
#     return result
#
# print(add(3, 4))

# 놀랍게도 틀림. 질문 게시판을 보니 입력 방식에 따라 함수가 달라져야한다.
# 예를 들어 문제에서 요구하는 사항은 ** 두 정수 A, B를 '입력'받은 다음, '첫째 줄에 A + B 를 출력'한다 ** 였다.
# 파이썬에서는 데이터를 입력받을 때, input()함수를 사용한다.

# 파이썬에서는 input()함수를 통해 한 줄의 입력을 받을 수가 있다.
input_data = input().split(' ')
# input()함수를 통해 데이터를 입력받고 입력받은 데이터를 splint(' ')함수를 통해 중간에 공백을 기준으로 나눠준다.
# A = input_data[0]
# B = input_data[1]
# input()함수를 통해 들어온 데이터는 문자열 데이터이다. 그래서 문자열로 바꾸어 주어야한다.
A = int(input_data[0])
B = int(input_data[1])
# 그리고 나서
print(A+B)

