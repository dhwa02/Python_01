url = "http://naver.com"
name = url.replace("http://", "")
name = name[:name.find(".")] # naver
key = name[:3]+str(len(name))+str(name.count("e"))+"!"

print(f"{url}의 비밀번호 : {key}")