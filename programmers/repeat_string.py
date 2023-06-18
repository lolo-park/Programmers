"""
매개변수 : 문자열 my_string 과 정수 n
출력 : my_string에 있는 문자를 n 만큼 반복한 문자열
예시) my_string = hello, n = 2
     출력 = hheelllloo
"""

def solution(my_string, n):
    # 1. 문자열을 리스트로 만들어서 요소들에 쉽게 접근하는 것
    # 2. 반복문을 통해 첫번째 요소부터 접근하여 그 다음번호에 똑같은 것을 n 개씩 넣어주는 방법
    answer = [] # 빈배열을 이용해 밀어넣어준다
    for i in range(len(my_string)):
        answer.insert(i+1, my_string[i]*n)
        # 빈 배열 answer에 insert 해준다
        # i+1 번 요소에
        # my_string[i]를 n개씩 넣어준다
    return ''.join(answer)
    # 리스트에 몰린 문자열들을 붙여서 문자열로 리턴

# 좀 복잡하게 생각했던 것 같고,
# 문자열이 + 로 합쳐질 수 있다는 것을 생각했다면 !
def solution(my_string, n):
    answer = ''
    for str in my_string:
        answer += (str*n)
    return answer