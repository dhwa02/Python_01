def profile(name, age, main_lang):
    print(f"이름 : {name}\t나이 : {age}\t주 사용 언어 : {main_lang}")

profile("A", 20, 'Python')
profile("B", 25, 'Java')

def profile_2(name, age = 20, main_lang = "Python"):
    print(f"이름 : {name}\t나이 : {age}\t주 사용 언어 : {main_lang}")

profile_2("A")
profile_2("B")

def profile_3(name, age, main_lang):
    print(name, age, main_lang)

profile_3(name = "A", main_lang = "Python", age = 20)
profile_3(age = 17, name = "B", main_lang = "Java")