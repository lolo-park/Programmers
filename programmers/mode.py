"""
최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다.
정수 배열 array가 매개변수로 주어질 때,
최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

매개변수 : 정수배열 array ex : [1,2,3,3]
return : 최빈값 3
조건 : 최빈값이 여러개면 -1을 리턴해라
"""
def solution(array):
    for i in array:
        return array.count(i) # array[0] 만 return 하게 됨..