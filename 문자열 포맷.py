# 방법 1
print("나는 %d살 입니다." % 20) # 정수
print("나는 %s을 좋아합니다." %"사과") # 문자 1개
print("나는 %s와 %s를 좋아합니다." %("사과", " 바나나"))
print("Apple 은 %s로 시작합니다." %"A") # 문자열
print("원주율 : %f..." % 3.141592) # 부동소수

# 방법 2
print("나는 {}살 입니다.".format(20))
print("나는 {}와 {}를 좋아합니다.".format("사과", "바나나"))

# 방법 3
print("나는 {age}살 이며, {fruit}를 좋아합니다.".format(age = 20, fruit = "사과"))

# 방법 4 (중요)
age = 20
fruit = "사과"
print(f"나는 {age}살이며, {fruit}를 좋아합니다.")