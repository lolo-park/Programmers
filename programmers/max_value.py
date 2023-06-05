"""
정수 배열 numbers가 매개변수로 주어집니다.
numbers의 원소 중 두 개를 곱해 만들 수 있는
최댓값을 return하도록 solution 함수를 완성해주세요.
"""


def solution(numbers):
  answer = sorted(numbers)
  max_value = answer[len(answer)-1] *answer[len(answer)-2]

  return max_value

# 위와 같이 푸는 것이 가장 기본적인 접근 방법일 것 같은데 상당히 찝찝하게 생겼음.
# 좀 더 스마트한 접근방법은 없을까

def solution(numbers):

  a = max(numbers) # numbers 배열에서 가장 큰 숫자를 a 변수에 저장
  numbers.remove(a) # numbers 에서 가장 큰 숫자 였던 a 제거
  b = max(numbers) # a가 제거 된 numbers 배열에서 가장 큰 숫자 b 변수에 저장

  return a * b
  # 근데 여기서 만약 가장 큰 숫자가 중복이었다면 remove()에서는 하나만 지워짐 (가장앞에있는)
  # 아 하긴 어차피 상관없는게 가장 큰 숫자 두개 곱하는 문제여도 위에 알고리즘으로 가능하다! 

