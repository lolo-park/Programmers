"""
매개변수: 문자열 my_string
출력: 소문자는 대문자로, 대문자는 소문자로 바꾼 문자열 return
"""


def solution(my_string):
    answer = ''
    for letter in my_string:
        if letter.islower() == True:
            answer += letter.upper()
        else:
            answer += letter.lower()


# 내장함수 swapcase() 확인해보기.. 매우간단 .. ㅎ
def solution(my_string):
    return my_string.swapcase()

# 내 풀이를 좀 더 간단하게 리스트 컴프리헨션스타일로 만들어보자
# 근데 너무 길어져서 별로인 것 같기도
def solution(my_string):
    answer = ''.join([my_string[i].upper()
                      if my_string[i].islower()
                      else my_string[i].lower()
                      for i in range(len(my_string))])
    return answer
#이게 더 별로인 것 같다