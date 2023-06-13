"""
문자열 배열 strlist가 매개변수로 주어집니다.
['hi', 'what', 'wow']

strlist 각 원소의 길이를 담은 배열을 retrun 하도록 solution 함수를 완성해주세요.

[2,4,3] 요래
[index(0), index(1), ---]

index에 접근해서 len(index(0)) 이렇게 구하면 되겠구나 !

"""


def solution(strlist):

    answer = []

    for i in range(len(strlist)):
        return answer.append(len(strlist[i]))

    return answer


# 이 for 문을 좀 더 깔끔하게

def solution2(string_list):
    empty_list = []
    for i in string_list:
        empty_list.append(len(i))

    return empty_list


