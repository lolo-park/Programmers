#test_list = ['one', 'two', 'three']
#for i in test_list:
#    print(i)

#a = [(1,2), (3,4), (5,6)] # 리스트 안의 요소가 튜플
#for (first, last) in a:
#    print(first + last)
"""
marks = [90, 25, 67, 45, 80]

number = 0 #각각의 학생에게 번호를 붙여주려고 변수 number를 사용한 것
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격" % number)
    else:
        print("%d번 학생은 불합격" % number)

# 1 - for문에서의 continue
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue # 60점 미만인 조건이 참일 경우 아래 print가 시행되지않고 처음으로 돌아감
    print("%d번학생, 축하드립니다 합격입니다" % number)
"""
# 2 - range 함수 : 숫자 리스트를 자동으로 만들어줌
a = range(10)
print(a)
# => range(0,10) range(10)은 0부터 10미만의 숫자를 포함하는 range객체를 생성한다

# 3 - 1부터 10까지를 더해보자
add = 0
for i in range(1, 11): # i 는 1 에서 10까지의 숫자다
    add = add + i
print(add)

# 4 - 1번에서 작성하였던 for문을 range 함수 len함수를 이용해 간단하게 만들어보자
# len 함수 : 리스트 안의 요소 개수를 돌려주는 함수
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)): #len(marks) => 5 , range(5) => 0,1,2,3,4
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다" % (number+1)) # number 가 0 부터 시작하기때문에 1을 더해줘야함

#for문을 활용한 구구단 구현하기 다음 PR로 넘긴다 ..