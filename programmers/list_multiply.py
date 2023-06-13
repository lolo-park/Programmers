"""
정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

numbers = [1,2,3]
-> [2,4,6]

각 인덱스에 접근 *2 를 해준다.
for문을 사용하여

numbers = [5,10,3,7,6]
for i in numbers:
  print(i*2) 5*2,10*2,3*2,7*2,6*2
10
20
6
14
12
얘네들을 다시 배열로 묶어주어야함
"""


def solution(numbers):
    answer = []

    for i in numbers:
        answer.append(i * 2)

    return answer


def solution(numbers):
    return [i*2 for i in numbers]
# 위와같은 조건식을 list comprehension이라고 한다


