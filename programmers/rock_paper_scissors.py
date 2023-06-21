# 가위는 2 바위는 0 보는 5
# 매개변수: 가위 바위 보를 내는 순서대로 나타낸 문자열 rsp
# 출력: rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열
# 예) rsp = '2', return = '0'
# 예) rsp = '205' return = '052'

def solution(rsp):
    answer = ''
    for i in range(len(rsp)):
        if rsp[i] == '2':
            answer += '0'
        elif rsp[i] == '0':
            answer += '5'
        elif rsp[i] == '5':
            answer += '2'
    return answer
# 하지만 이건 너무 단편적이다.