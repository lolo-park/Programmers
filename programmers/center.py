"""
중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때
가장 중앙에 위치하는 값을 의미합니다.
예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다.
정수 배열 array가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성해보세요.

리스트 안의 값들을 순서대로 정렬 리스트.sort() 사용
리스트 안의 중앙 값을 구하기 statistics 모듈의 median(리스트)를 사용할 수도 있고
수학적으로 접근한다고 생각했을 때 어차피 리스트 안 요소들의 개수는 홀수이고

★ 홀수 값에서 중간에 해당하는 것에 접근하고 싶을 때, 어떻게 해야할지를 몰랐다.
근데 생각해보면 반으로 자른다고 생각을하고
예를 들어 10 을 2로 나눈 5가 중앙에 값에 가까우니까
그렇게 생각을 했을 때
3개면 / 2 => 1.---
5개면 / 2 => 2.---
7개면 / 2 => 3.---- 이렇게 되고 그 리스트의[3]은 리스트의 4번째에 해당하는 값이니 앞 뒤로 3개씩 있게 됨. ㅎ

이렇게 풀어놓고 보면 너무 복잡하지만 그냥 간단히 생각하고 외워야 적용하기 빠르다.
"""


def solution(array):
    array.sort()
    answer = array[len(array) // 2]
    return array

# 요렇게 해도 되고 더 간단히 한다면


def solution(array):
    return array.sort()[len(array//2)]
# 이렇게 하면 TypeError : 'NoneType' object is not subscriptable 이라고 나오는데
# 정수형을 인덱싱/슬라이싱하려고할 때 나오는 에러라고 한다.
# 한번에 return 하지 않고 array.sort()를 먼저 해주고 하면 됨
# 그래서 찾아봤더니 sorted 라는 것이 있었다. sort()와 sorted()의 차이는
# sort() 함수의 리턴값은 NONE 이다. 그 이유는 sort()함수는 원본 자체가 바뀌는 함수다.
# sorted() 함수는 내장함수이고
# 그래서 위에 것이 typeerror가 되는 것이다. array.sort()는 아무것도 리턴하지 않으니까 !

def solution(array):
    return sorted(array)[len(array)//2]
# 그래서 이렇게 해주어야 맞다.
