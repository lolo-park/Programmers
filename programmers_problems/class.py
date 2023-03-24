# 과자 틀 = 클래스 class
# 과자 = 객체 object
# class로 만든 객체들은 서로 아무 영향도 주지 않는다

class Cookie:
    pass

a = Cookie()
b = Cookie()
# Cookie()의 결과값을 돌려받은 a 와 b 가 객체이다, a 와 b 는 Cookie의 인스턴스이다
# (인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용)

class FourCal:
    def setdata(self, first, second): # class안에 구현된 함수 = Method
        self.first = first
        self.second = second

answer = FourCal()
answer.setdata(4, 2)
# setdata 메서드의 첫번째 매개변수 self에는 setdata메서드를 호출한 객체 a가 자동으로 전달
print(answer.first)# ===> 4 answer객체에 객체변수 first와
print(answer.second)# ===> 2 second가 생성되었음을 알 수 있다.

c = FourCal() # c라는 객체
d = FourCal() # d라는 객체
c.setdata(4, 2) # 숫자 4와 2를 c에 지정
print(c.first) # ===> 4 | 객체 변수 first
d.setdata(3, 7) # 숫자 3과 7을 d에 지정
print(d.first) # ===> 3

#곱하기 빼기 나누기 기능이 있는 클래스 FourCal 로 만들어보자

class FourCal2:
    def __init__(self, first, second):  #init_(self, first, second): #생성자로인식되어 객체가 생성되는 시점에 자동으로 호출
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

# 요렇게 Class FourCal2 를 만들었다. 클래스 FourCal2의 객체들을 활용해보자

z = FourCal2(10, 10)
print(z.add()) # 20
print(z.sub()) # 0
print(z.mul()) # 100
print(z.div()) # 1.0

one = FourCal2(10,10)
two = FourCal2(10, 10)
# one.setdata(4, 2)
# two.setdata(3, 8)
print(one.add()) # 20
print(two.add()) # 20
print(one.mul()) # 100
print(one.div()) # 1.0
print(one.sub()) # 0

# __init__ 메서드는 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출된다
# (이것만빼고 setdata 메서드와 동일함)
# 생성자의 매개변수 first와 second에 해당하는 값이 전달되지않으면
# __init__ 메서드를 쓸 경우 오류가 나게 된다.
# 그래서 a = FourCal2() 만 부르면 안되고
# a = FourCal2(4, 2) 이렇게 first, second에 해당하는 값을 전달해야함

"""
★ 그래서 __init__ 이나 setdata 중에 하나만 사용해야하는 것 같다 ★

< 참고 사항 > 
FourCal 클래스의 인스턴스 a에 setdata 메서드를 수행하지 않고
add 메서드를 먼저 수행하면 | FourCal object has no attribute 'first' | 라는 오류가 발생
WHY? setdata 메서드를 수행해야 객체 a의 객체변수 first와 second가 생성되기 때문

이렇게 객체에 first, second와 같은 초기값을 설정해야 할 필요가 있을 때는 
setdata와 같은 메서드를 호출하여 초기값을 설정하기보다는 
생성자를 구현하는 것이 안전 
생성자란 객체가 생성될 때 자동으로 호출되는 메서들를 의미

__init__ 을 사용하면 이 메서드는 생성자가 된다
이렇게 FourCal 클래스에 생성자를 추가한 것이 
class FourCal:
    def __init__(self, first, second):
    self.first = first 
    self.second = second 
    
    def add(self):
        result = self.first + self.second
        return result 
"""










