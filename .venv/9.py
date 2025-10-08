def toBool(arg):
    if arg == "да": return True
    return False
if toBool(input("Собака короткошерстной породы? ")):
    if toBool(input("Рост собаки менее 50 см?")):
        if toBool(input("У собаки короткий хвост?")):
            print("английский бульдог")
        elif toBool(input("У собаки длинные уши?")):
            print("гончая")
        elif toBool(input("У собаки короткое тело?")):
            print(мопс)
        else:
            print("чихуахуа")

    elif toBool(input("Собака весит более 50 кг?")):
        print("датский дог")
    else:
        print("фоксхаунд")
else:
    if toBool(input("Рост собаки менее 50 см?")):
        if toBool(input("У собаки доброжелательный характер?")):
            print("кокер-спаниэль")
        else:
            print("ирландский сеттер")
    elif toBool(input("Рост собаки менее 70 см?")):
        if toBool(input("У собаки длинные уши?")):
            print("большой вндейский грифон")
        else:
            print("колли")
    elif  toBool(input("Окрас рыжий с белыми отметинами?")):
        print("сенбернар")
    elif toBool(input("Белоснежный окрас?")):
        print("ирландский волкодав")
    else:
        print("ньюфаундленд")

