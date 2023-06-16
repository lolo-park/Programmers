"""
문자열 my_string이 매개변수로 주어집니다.
my_string안의 모든 자연수들의 합을
return하도록 solution 함수를 완성해주세요.

"""
def solution(my_string):
    answer = 0
    for num in my_string:
        if my_string.isdigit():
            result = list(map(int), num)
            for i in range(len(result)):
                answer += result[i]
    return answer


def solution(my_string):
    answer = 0
    for i in my_string: # my_string 문자열안의 요소 하나하나에 접근
        try:
            answer = answer + int(i) # int 인 것을 answer에 더한다
        except:
            pass # 아닌 것은 pass
    return answer