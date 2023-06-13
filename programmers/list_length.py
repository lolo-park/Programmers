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

"""
for i in string_list: 에서는 
어쨌든 range 를 string_list 안으로 지정한 것이기때문에 
괜찮다고 볼 수 있다. 
그리고 string_list 요소들에 하나씩 접근해서 
len(i) 를 구하게 되고 
리스트.append()함수 안에 넣어줌으로써 요소들의 length 로 이루어진 새로운 리스트 생성 """


