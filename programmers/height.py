"""
머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다.
머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때,
머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.

array = [] (키를 의미하는 정수 배열)
height = 정수(머쓱이의 키)

리턴 --
    머쓱이보다 키 큰 사람의 수를 리턴해라
해결 --
    리스트의 인덱스 하나하나에 접근해서 height랑 비교
    height보다 큰 사람들 빼서 다른 리스트에 넣기


"""
def solution(array, height):
    answer = []

    for heights in array: # for문은 index[0]부터 scan 해서 많아질 수록 부담이 될 수도
        if heights > height:
            answer.append(heights)

    return len(answer)
# 진짜 계속 이렇게 전통적인 방식으로밖에 접근이 안된다 하하하


def solution(array, height):
    array.append(height) # height를 바로 array에 추가시킨다
    array.sort(reverse=True) # 큰 숫자부터 정렬될 수 있도록 sort(reverse = True)
    return array.index(height) # array 리스트에서 height의 index 번호를 return 한다
# return 전에 height가 170이고 array가 [183, 182, 181, 180,170,160] 이었다면,
# height(170)의 index는 4
# 리스트의 index 번호는 [0]부터 매겨지기때문에 내가 구하고자 하는 요소의 index 번호가 곧
# 그 앞에 개수를 나타내는 거지
# 와 여기까진 그냥 생각 못했을 것 같다 !
