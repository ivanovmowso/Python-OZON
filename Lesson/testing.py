user_name = input("Введите имя: ")
credit = input('Размер кредита: ')
duration = input("Срок кредита: ")
percent = input("Процентная ставка: ")

credit = float(credit)
duration = int(duration)
percent = float(percent)

pay = (credit / duration) + ((credit * percent) / 12)
print(pay)