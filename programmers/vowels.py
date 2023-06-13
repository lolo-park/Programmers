"""
영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다.
문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

-예시-
    my_string = "Hello"
    return = "Hll"
-접근-
    문자열을 하나하나 쪼개어 배열의 인덱스로 만든다
    "Hello" -> [H,e,l,l,o]
    근데 여기서 자음/모음을 어떻게 구별해 아
    if include a,e,i,o,u 이런식으로 접근해야겠네
"""


def solution(my_string):

