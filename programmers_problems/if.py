"""
조건문 Conditionals
money = False

if money:
    print("택시")
else:
    print("걷기")

money = True

if money:
    print("돈있으면 택시")
else:
    print("돈 없으면 걷기")

pocket = ['paper', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

===> 카드를 꺼내라

money = 2000
if money >= 3000:
    print ("taxi")
else:
    print("walk")

===> walk

    # and , or , not
money = 2000
card = True
if money >= 3000 or card:
    print("taxi")
else:
    print("walk")
    # ===> taxi

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("get the taxi") #아무것도 print하고 싶지않다면 그냥 pass 쓰면 된다
else:
    print("just walk")

pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print("grab a taxi")
else:
    if card:
        print("grab a taxi")
    else:
        print("just walk")
    # 위의 코드가 너무 산만하다고 느껴진다면
    # elif 사용하기
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("grab a taxi")
elif card:
    print("grab a taxi")
else:
    print("just walk")
# 더 간략하게 코드 작성하기
pocket = ['cellphone', 'headset']
card = True

if 'money' in pocket: pass
else: print("Use the card")


if score >= 60:
    message = "success"
else:
    message = "failure"
"""
# ===> 더 간단하게 바꿔보자

score = 80
message = "success" if score >= 60 else "failure"
print(message)
