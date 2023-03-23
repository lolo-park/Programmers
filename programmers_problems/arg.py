# 1 - 리턴값이 없는 함수
def add(a, b):
    print("%d와 %d의 합은 %d 입니다." % (a, b, a+b))
add(3, 4) # ===> 3와 4의 합은 7 입니다.

a = add(3, 4)
print(a) # ===> None. 리턴값이 없는 함수였기에 None을 출력

# 2 - 여러 개의 입력값을 받는 함수
def add_many(*args):#매개변수이름앞에 * : 모든 입력값을 모아 튜플로 만든다
    result = 0
    for i in args:
        result = result + i
    return result
result = add_many(1,2,3)
print(result) # ===> 6 모든 매개변수들(*args)를 더하는 함수였기에

result_two = add_many(1,2,3,4,5,6,7,8,9,10)
print(result_two)# ===> 55

# 3 - 키워드 매개변수 : **를 사용하여 입력받은 매개변수를 딕셔너리로 출력함
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1) # ===> {'a':1}
print_kwargs(name='foo', age=3)# ===> {'name': 'foo', 'age': 3}

# 4 - 리턴값은 항상 하나이다 하나로 묶어서 출력한다 !
def add_and_mul(a, b):
    return a+b, a*b
result = add_and_mul(3,4)
print(result)# ===> (7, 12)

result1, result2 = add_and_mul(3, 4)
print(result1)# ===> 7
print(result2)# ===> 12

# 5 - return 을 사용하여 함수를 빠져나가보자
def say_nick(nick):
    if nick == '바보':
        return #입력값이 '바보'면 return 을 통해 함수를 바로 빠져나가버림
    print("나의 별명은 %s 입니다" % nick)

say_nick('바보')# ===> 출력 되는것이 없음
say_nick('야호')# ===> 나의 별명은 야호입니다

# 6 - 매개변수에 초깃값 미리 설정하기
def say_myself(name, age, man=True): # man=True 매개변수의 초기값 설정
    print('나의 이름은 %s 입니다' % name)
    print('나는 %d살 입니다.' % age)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")

say_myself("박진주", 32) # ===> '남자입니다'까지 나옴
#man이라는 변수에는 입력값을 주지 않았지만 초기값이 True로 세팅되어있었기 때문에
say_myself("박진주", 32, True)
say_myself("박진주", 32, False)
# 초기값을 세팅하고 싶은 매개변수는 항상 제일 나중에 위치시키도록 하자

# 7 - 함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a = a + 1

vartest(3)
print(a)# ===> 출력 : 1  함수 안에서 사용한 매개변수는 함수 밖의 변수 이름과 상관이 없다

def vartest2(a):
    a = a + 1
    print(a)
vartest2(3)# ===> 출력 : 4

# 8 - 함수 안에서 함수 밖의 변수를 변경
b = 1
def vartest3(b):
    b = b + 1
    return b

b = vartest3(b)
print('vartest3 ==== ',b)

# global 명령어 사용하기
c = 1
def vartest4():
    global c
    c = c + 1

vartest4()
print('vartest4 ==== ', c)
# global명령어를 사용하므로서 함수 밖에서도 변수 c 를 사용하겠다라는 것인데
# 함수는 독립적으로 존재하는 것이 권장되므로 외부 변수에 종속되는 함수는 좋은 함수가 아님

# 9 - lambda 예약어 = def : def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에

# 함수를 함수 이름 없이 선언할 수 있음
# 리스트를 정렬하는 sort()함수, map()함수, filter()함수 등에서 잘 쓰임

add_lambda = lambda e, f: e+f
result_lambda = add_lambda(3, 4)
print(result_lambda)

# map(), filter() 함수와 같이 어떻게 쓰일 수 있는지 확인해보자
list_in = [1,2,3,4,5,6,7,8,9]

list_out_1 = map(lambda x: x * x, list_in)
list_out_2 = filter(lambda x: x % 2 == 0, list_in)

print(list(list_out_1)) # ===> [1, 4, 9, 16, 25, 36, 49, 64, 81] list_in 리스트 요소들 제곱하여 리스트화
print(list(list_out_2)) # ===> [2, 4, 6, 8]
# map()과 filter() 함수가 제너레이터이기 때문에 list()함수를 이용하여 강제로 리스트 자료형으로 변환해주어야함