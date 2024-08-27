from random import*

count = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5<= time <=15:
        print(f"[O] {i}번째 손님 (소요시간 : {time}분)")
        count += 1
    else:
        print(f"[] {i}번째 손님 (소요시간 : {time}분)")

print(f"\n총 탑승 승객 : {count} 분")
    