try:
    print("나누기 전용 계산기")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1]))

    print(f"{nums[0]} / {nums[1]} = {nums[2]}")

except ValueError:
    print("올바른 값을 입력하시오.")

except ZeroDivisionError as err: # 0으로 나누려고 할 때 발생하는 오류
    print(err)

except Exception as err: # 어떤 에러가 발생하였는지 확인 가능
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)