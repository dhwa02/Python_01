def std_weight(height, gender):
    if gender == "남자":
        weight_M = round(((height)/100)**2*22,2)
        print(f"키 {height}cm 남자의 표준 체중은 {weight_M}입니다.")
    elif gender == "여자":
        weight_W = round(((height)/100)**2*21,2)
        print(f"키 {height}cm 여자의 표준 체중은 {weight_W}입니다.")
    else:
        print("성별을 다시 입력하세요.")


std_weight(170, "남자")
std_weight(169, "여자")

std_weight(222, "??")

