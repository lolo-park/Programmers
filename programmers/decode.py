"""
매개변수: 문자열 cipher, 정수 code
조건: cipher에서 code의 배수번째 글자만 진짜 암호
출력: 암호 문자열
"""


def solution(cipher, code):
    answer = ''
    for i in range(1, len(cipher)+1):
        if i % code == 0:
            answer += cipher[i-1]
    return answer
# 문자열에 추가하는 것은 ''+'' 연산자로 가능하다

# 간단한 방법
# array[::] 처음부터 끝까지 반환
# array[::2] 처음부터 끝까지 2칸 간격으로
# array[1::2] 인덱스 1 부터 2칸 간격으로



def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer
# 만약 solution("hello", 2) 라면
# 인덱스와 상관없이 2번째, 4번째, 6번째 위치한 글자들만 출력하는 것이라고 했을 때
# index로 보면 2-1 = index 1번이 곳 두번째 글자이기때문에 ..
