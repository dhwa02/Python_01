from random import*
id = list(range(1,21))
shuffle(id)
winner = sample(id, 4)

three_winning = sample(id, 3)
print("-- 당첨자 발표 --")
print(f"치킨 당첨자 : {winner[0]}")
print(f"커피 당첨자 : {winner[1:]}")
print("-- 축하합니다 --")