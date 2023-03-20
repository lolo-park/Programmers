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

# 방법 3 -따끈따끈한 f-string도 있다
s = 'coffee'
n = 5
result1 = f'저는 {s}를 좋아합니다. 하루에 {n}잔을 마셔요.'
print(result1)
#JavaScript에서는 ${} 를 사용하여 변수값을 넣어줬었징.