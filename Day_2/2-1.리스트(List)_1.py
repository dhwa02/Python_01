subway = ["A","B","C"]
print(subway.index("A"))

subway.append("D") # 마지막 index에 D 추가
print(subway)

subway.insert(1,"E") # index 1에 E추가 (A와 B 사이)
print(subway)

subway.pop() # 마지막 index 제거 (D제거)
print(subway)

print(subway.count("A"))