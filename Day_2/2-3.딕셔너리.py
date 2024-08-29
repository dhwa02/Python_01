cabinet = {7:"A", 77:"B"}
print(cabinet[7])
print(cabinet[77])

print(cabinet.get(7))
print(cabinet.get(77))

print(cabinet.get(777,"C"))

print(7 in cabinet) # True
print(6 in cabinet) # False

cabinet_2 = {"A":"Apple", "B":"Banana"}
cabinet_2["A"] = "Abocado" # 덮어쓰기
cabinet_2["C"] = "Cherry" # 추가
print(cabinet_2)

del cabinet_2["A"] # 삭제
print(cabinet_2)

print(cabinet_2.keys()) # key 값만 출력
print(cabinet_2.values()) # value 값만 출력
print(cabinet_2.items()) # key, value 모두 출력

cabinet_2.clear() # 모두 삭제
print(cabinet_2)