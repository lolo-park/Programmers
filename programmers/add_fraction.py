"""
첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1,
두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다.
두 분수를 더한 값을 기약 분수로 나타냈을 때
분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

range()함수 : 시작 숫자와 끝 숫자를 지정하려면 range(시작 숫자, 끝 숫자) 형태를 사용하는데, 이때 끝 숫자는 포함 되지 않는다.

denom1 과 denom2 를 최소공배수를 이용하여 맞춰주고
최소공배수를 구했어 만약에 그걸 i 라고 쳤을 때
denom1 * x = i
denom2 * y = i

x = i/denom1
y = i/denom2

a = numer1 * x
b = numer2 * y

answer = [a+b, i]
return



"""


def solution(numer1, denom1, numer2, denom2):
    for i in range(max(denom1, denom2), (denom1 * denom2) + 1):

        if i % denom1 == 0 and i % denom2 == 0:
            print(i)  # 3....왜 3이지?
            break

        x = i / denom1
        print(i)

        y = i / denom2

        a = numer1 * x
        b = numer2 * y

        answer = [a + b, i]

        return answer
