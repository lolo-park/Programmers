# 1 - print를 활용한 데이터 입출력

print("life", "is", "too short") # => life is too short

print("life" "is" "too short") # => lifeistooshort

# 한 줄에 결과값을 출력하고 싶을 땐 두번째 인자에 end=''를 주면 된다
for i in range(10):
    print(i, end='') # => 0123456789

# 2 - 파일을 통한 입출력 방법
f = open("new_file.txt", 'w')
for i in range(1, 11):
    data = "%d th line.\n" % i
    f.write(data) # 생성한 파일에다가 데이터를 적는 것.
f.close()

f = open("/Users/lullu/git/pythonPractice/programmers_problems/new_file.txt", 'r')
line = f.readline()
print(line)
f.close()
