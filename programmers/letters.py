"""
머쓱이는 할머니께 생신 축하 편지를 쓰려고 합니다.
할머니가 보시기 편하도록 글자 한 자 한 자를 가로 2cm 크기로 적으려고 하며,
편지를 가로로만 적을 때, 축하 문구 message를 적기 위해
필요한 편지지의 최소 가로길이를 return 하도록 solution 함수를 완성해주세요.
*공백 하나도 문자 크기로 간주
1 =< message <= 50
글자 한자가 2cm 라고 했을때 "잘 지내니?" -> 6 * 2 = 12 cm 가 return 되어야한다는 것이다.
string -> split 하여 list 에 담아주자
"""

# 매개변수 message 는 문자열이다


def solution(message):

    answer = list(message)

    return len(answer) * 2

# 이렇게 해도 되지만, len()함수를 사용하면 바로 배열로 인식하고 인덱스 하나하나를 (공백 포함) 인식한다