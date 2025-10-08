print("Вы поедете на бал?")
answer=input("Имя персонажа: ")
if not(answer.lowercase() in ["да", "нет"]):
    print("Верно")
else:
    print("Неверно")