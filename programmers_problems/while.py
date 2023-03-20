# while 조건이 Ture인 동안에 while문 안의 동작 반복 실행
# while은 반복문 if는 조건문


treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다" % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다")

# 자료형 Formatting 방법
# 방법 1 - % 사용하기
names = ['kim', 'park', 'lee']
for name in names:
    print('my name is %s' % name)

money = 10000
s2 = 'give me %d won' % money
print(s2)

d = 3.14592
print('value %f' % d)

# Formatting 해야할 변수 값이 두 개 이상일 때는 ?

s1 = 'my name is %s. age : %d' % ('진주', 31)
print(s1)

age = 80
money = 20000
name = 'kim'
weight = 80.12
etc = 'abcedfg'
s2 = 'My name is %s, age : %d, weight: %f, money : %d, etc : %s' % (name, age, weight, money, etc)
print(s2)

# 방법 2 - str.format
month = 1
while month <=12:
    print(f'2023년{month}월')
    month = month + 1

# 방법 3 - 따끈따끈한 f-string도 있다
s = 'coffee'
n = 5
result1 = f'저는 {s}를 좋아합니다. 하루에 {n}잔을 마셔요.'
print(result1)
#JavaScript에서는 ${} 를 사용하여 변수값을 넣어줬었징.

"""
coffee = 10
money = 300
while money:
    print('Got the money, Give Coffee')
    coffee = coffee - 1
    print('Coffee Left : %d' % coffee)
    if coffee == 0:
        print('Coffee - None')
        break

# break 를 통해 특정 조건이 끝났을 경우 빠져나가도록 설정한다.
# 여기서 break 가 걸리지 않으면 coffee 가 0개가 되더라도 money = 300 이 계속 유지되면서
# 무한 루프를 돌게 된다.
"""

# 위의 상황을 좀 더 구체화 시켜보자
coffee = 10
while True:
    money = int(input("insert money: "))
    if money == 300:
        print("Get the Coffee")
        coffee = coffee -1
    elif money > 300:
        print("Get the change %d with Coffee" % (money -300))
        coffee = coffee -1
    else:
        print("Get the money without Coffee")
        print("%d Coffee Left" % coffee)
    if coffee == 0:
        print("No Coffee Left. Stop Processing")
        break