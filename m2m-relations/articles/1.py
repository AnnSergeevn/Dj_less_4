

def change_text(s1: str, str_add: str) -> str:
    s = ""
    for el in s1.split():
       s = el + str_add
    return s


s = 'Мама мыла раму вечером'
s4 = ", елки палки,"
change_text(s, s4)