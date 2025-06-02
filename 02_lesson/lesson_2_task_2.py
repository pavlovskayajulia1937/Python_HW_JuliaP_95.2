# Функция проверки високосного года
def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False
    

# Проверяем год
year = input("Введите год для проверки: ")
result = is_year_leap(int(year))
print("год", year, ":", result)
