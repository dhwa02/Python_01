# 방법 1
for i in range(1, 6):
    with open(str(i)+"주차.txt", "w", encoding="utf8") as report_file:
        report_file.write(f"- {i} 주차 주간보고 -\n")
        report_file.write("부서 : \n")
        report_file.write("이름 : \n")
        report_file.write("업무 요약 : ")

# 방법 2
for i in range(1, 6):
    report_file = open(f"{i}주차.txt", "w", encoding="utf8")
    print(f"- {i} 주차 주간보고 -", "부서 : ", "이름 : ", "업무 요약 : ", sep="\n", file=report_file)