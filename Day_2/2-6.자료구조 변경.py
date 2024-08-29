menu = {"아메리카노", "라떼", "쉐이크"}
print(menu, type(menu)) # {} <class 'set'>

menu = list(menu)
print(menu, type(menu)) # [] <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) # () <class 'tuple'>