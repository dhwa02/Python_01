import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4))

# 은행 대기순번표
for num in range(1, 21):
    print("대기번호 : " +str(num).zfill(3))

answer = input("값을 입력하세요 : ")
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")