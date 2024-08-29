def profile(name, age, *language):
    print(f"이름: {name}\t나이: {age}", end= " ")
    for lang in language:
        print(lang, end = " ")
    print()

profile("A", 20, "Python", "Java", "C")
profile("B", 23, "Python", "Java", "C", "C++", "C#")
