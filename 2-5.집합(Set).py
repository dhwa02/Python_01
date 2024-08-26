# 중복 X, 순서 없음
my_set = {1,2,3,3,3}
print(my_set) # {1, 2, 3}

java = {"A", "B", "C"}
python = set(["A", "D"])

# 교집합
print(java & python) # 방법 1
print(java.intersection(python)) # 방법 2

# 합집합
print(java | python) # 방법 1
print(java.union(python)) # 방법 2

# 차집합
print(java - python) # 방법 1
print(java.difference(python)) # 방법 2

# 추가
java.add("A")
print(java)

# 삭제
python.remove("A")
print(python)
