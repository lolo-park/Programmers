"""
매개변수: 정수 n
조건: 3의 배수들을 제거하고 숫자는 순서대로 진행
출력: n을 조건에 맞게 나온 숫자 로 변경하여 출력
어렵다..

"""
# 1st try
def solution(n):
    answer = []

    for i in range(1, n + 1):
        answer.append(i)  # [1,2,3,4,5]
        for j in answer:
            if j % 3 == 0:
                answer.remove(j)
    # 여기서 answer 리스트가 세팅 되고

    new_list = []
    latest_list = []

    for k in range(len(answer)):
        new_list.append(str(answer[k]))
    # 새로운 빈 리스트 new_list에 리스트 answer의 요소들을 문자열로 세팅
    # new_list = ['1', '2', '4', '5', '7', '8', '10', '11', '13', '14', '16', '17', '19', '20']
    for h in range(len(new_list)):
        if '3' in new_list[h]:
            latest_list.append(new_list[h])  # 여기까지 '13'에 접근

    return latest_list


print(solution(20))  # [1,2,4,5]

# 2nd try
def solution(n):
    answer = []

    for i in range(1, n + 1):
        answer.append(i)  # [1,2,3,4,5]
        for j in answer:
            if j % 3 == 0:
                answer.remove(j)
    # 여기서 answer 리스트가 세팅 되고 [1,2,4,5]

    new_list = []
    latest_list = []

    for k in range(len(answer)):
        new_list.append(str(answer[k]))
    # 새로운 빈 리스트 new_list에 리스트 answer의 요소들을 문자열로 세팅
    # new_list = ['1', '2', '4', '5', '7', '8', '10', '11', '13', '14', '16', '17', '19', '20']
    for h in range(len(new_list)):
        if '3' in new_list[h]:
            latest_list.append(new_list[h])  # 여기까지 ['13']에 접근

    for last in new_list:
        if last in latest_list:
            new_list.remove(last)

    return new_list[len(new_list) - 1]  # 마지막리스트에 접근 하는 건데.. 이건 잘못된 듯

# 3rd try - runtime error
def solution(n):
    numbers = []
    for num in range(1, n + 1):
        numbers.append(num)
    # print('numbers == ',numbers)
    # 1부터 n까지 숫자들이 들어있는 리스트 numbers
    answer = []
    for i in range(1, n*10): # n의 제곱을 range로 두면(n**2) 실행되는 숫자가 기하급수적으로 늘어나서 에러가남..> n*10까지로바꿈
        answer.append(i)  # [1,2,3,4,5]
        for j in answer:
            if j % 3 == 0:
                answer.remove(j)
    # print('answer == ',answer)
    # 3의 배수가 빠진 리스트 answers

    new_list = []
    latest_list = []

    for k in range(len(answer)):
        new_list.append(str(answer[k]))
    # 새로운 빈 리스트 new_list에 리스트 answer의 요소들을 문자열로 세팅
    # new_list = ['1', '2', '4', '5', '7', '8', '10', '11', '13', '14', '16', '17', '19', '20']
    print('new_list == ', new_list)

    for h in range(len(new_list)):
        if '3' in new_list[h]:
            latest_list.append(new_list[h])  # 여기까지 ['13']에 접근
    print('latest_list == ', latest_list)

    for last in latest_list:
        if last in new_list:
            new_list.remove(last)  # 3의 배수와 3이 들어간 숫자를 뺀 리스트 new_list
    # print('new_list == ',new_list)
    print('2nd new_list == ', new_list)

    return new_list[n - 1]  # 마지막리스트에 접근 하는 건데.. 이건 잘못된 듯
# 이게 사실 얼마나 간단한 풀이로 풀리는 것일지.. 보기가 두렵다 ㅎ
def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer
# for _ in range(n) 이렇게 범위를 지정해 줄 때,
# 특별히 사용하지 않을 변수라면 _ 로 그냥 퉁쳐도 된다는 뜻
# 하나씩 증가하다가 3의 배수를 만나거나 3이 포함된 숫자를 만나면 하나 더 더해서 띵군다