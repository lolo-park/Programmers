"""
10만원 이상 5%
30만원 이상 10%
50만원 이상 20%
매개변수 : 옷의 가격 price
return : 지불해야할 금액
"""
# 내 풀이
import math


def solution(price):
  if price >= 0 and price < 100000:
    return price
  elif price >= 100000 and price < 300000:
    return math.floor(price - (price * 0.05))
  elif price >= 300000 and price < 500000:
    return math.floor(price - (price * 0.1))
  elif price >= 500000:
    return math.floor(price - (price * 0.2))

#더 간단한 풀이 **큰 숫자 부터 내려가면 중간에 따로 걸릴일이 없다**
def solution(price):
    if price >= 500000:
        return int(price-(price*0.2))
    elif price >= 300000:
        return int(price-(price*0.1))
    elif price >= 100000:
        return int(price-(price*0.05))
    else:
        return price

def solution(price):
    if price>=500000:
        price = price *0.8 # 바로 곱해서 할인금액 받을 수 있게
    elif price>=300000:
        price = price *0.9
    elif price>=100000:
        price = price * 0.95
    return int(price) # return 은 한번에 ! 