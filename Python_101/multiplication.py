
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end="") #print함수에 parameter로 end 설정해주면 결과값을 다음줄로 넘기지 않음
    print('') #프린트함수에서 ''는 두번째 for문이 끝나면 다음줄로 넘김


# 1 - List Comprehension : 리스트 안에 for문 포함하기
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)

# 2 - 위의 for문을 List Comprehension을 사용해보자
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result) #Ta-da! 이렇게 간단하게 표현할 수 있음

# 3 - 여기다 또 조건을 붙이고 싶다면
a = [1,2,3,4]
result = [num*3 for num in a if num % 2 == 0]
print(result)

# 4 - 구구단의 모든 결과를 리스트에 넣어보자
result = [x*y for x in range(2,10)
              for y in range(1,10)]
print(result)