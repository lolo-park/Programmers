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

def solutioin(rsp):
    # 딕셔너리를 활용한 접근은 a = b, c = d 처럼 정해진 값이 있을 때
    # 활용하기 용이하다고 분명 공부했었다
    d = {'0':'5', '2':'0', '5':'2'}
    return ''.join(d[i] for i in rsp)
    # ''.join()함수를 활용해 문자열로 합친다
    # d[i] for i in rsp 라고 했을 때,
    # 딕셔너리 '변수명[key값]'을 통해 value를 구할 수 있음


# replace 함수를 써서 더 빠른 시간복잡도
def solution(rsp):
    rsp = rsp.replace('0', 'r')
    # rsp에 replace된 값을 다시 저장
    rsp = rsp.replace('2', 's')
    rsp = rsp.replace('5', 'p')
    rsp = rsp.replace('r', '5')
    rsp = rsp.replace('s', '0')
    rsp = rsp.replace('p', '2')
    return rsp
