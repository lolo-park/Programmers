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
    def setdata(self, first, second): # Class안에 구현된 함수 = Method
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
one = FourCal2()
two = FourCal2()
one.setdata(4, 2)
two.setdata(3, 8)
print(one.add()) # ===> 6
print(two.add()) # ===> 11







