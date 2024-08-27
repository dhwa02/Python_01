absent = [3, 7]
no_book = [4]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print(f"{student}는 교무실로")
        break
    print(f"출석 : {student}")
