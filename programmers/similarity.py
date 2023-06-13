"""
두 배열이 얼마나 유사한지 확인해보려고 합니다.
문자열 배열 s1과 s2가 주어질 때
같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.

"""


def solution(s1, s2):
    answer = 0

    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                answer += 1

    return answer

# 근데 여기서 set() 자료구조를 이용하면 한줄로 끝난다.
def solution(s1, s2):
    return len(list(set(s1)&set(s2)))

# 여기서 set()함수는 {} 객체를 리턴한다며

#근데
def solution(s1, s2):
    return len(set(s1)&set(s2))
#이렇게도 된다고 한다

# 총 정 리
# set()를 사용하여 {} 객체를 리턴할 수 있다.
# len()함수를 사용하여 {} 객체의 길이도 구할 수 있다! 