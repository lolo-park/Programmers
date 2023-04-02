def add(a, b):
    return a + b

def sub(a, b):
    return a - b


# 현재 이 파일 mod1.py 이 모듈이다
# import mod1 명령어를 통해서 모듈을 사용할 수 있다
# print(mod1.add(3,4)) 이렇게

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
# 아래의 설명에 덧붙이자면, 즉
# 터미널에서 모듈 mod1을 import 한뒤
# mod1.__name__ 을 출력하면 모듈이름 mod1 이 나온다.
# 하지만 python3 mod1.py 명령어를 통해 파일을 실행할 경우에는
# __name__ 변수에 __main__ 값이 저장된다라는 뜻이다.

# 결국 python3 mod1.py 명령어를 통해서만 파일의 메서드에 지정한 입력값을 print 하는 것이고
# 그냥 mod1 모듈만 import 해 올 경우에는 이 입력값들을 print 하지 않는다는 것!




"""
파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름이다. 
만약 C:\doit>python mod1.py처럼 직접 mod1.py 파일을 실행할 경우 mod1.py의 __name__ 변수에는
 __main__ 값이 저장된다. 하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod1을 import 할 경우에는 
 mod1.py의 __name__ 변수에는 mod1.py의 모듈 이름 값 mod1이 저장된다.
"""