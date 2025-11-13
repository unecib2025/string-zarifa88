#prog1
name = input("Введите имя пользователя: ")
name = name.strip()
if name.isalnum():
    name = name.lower()
    print("Имя корректно:", name)
else:
    print("Ошибка")

#prog2
password = input("Введите пароль: ")
digits = 0
uppers = 0
for a in password:
    if a.isdigit():
        digits = 1
    if a.isupper():
        uppers = 1
if len(password) >= 8 and digits == 1 and uppers == 1:
    print("Пароль надёжен")
else:
    print("Пароль слаб")

#prog3
log = "ACCESS DENIED"
log1 = log.capitalize() + " – вход запрещён"
print(log1)

#prog4
data = "ERROR connection ERROR failed access"
data1 = data.replace("ERROR","ALERT")
count_alerts = data1.count("ALERT")
print(data1)
print("Количество предупреждений:", count_alerts)

#prog5
email = input("Введите email: ")
if "@" in email:
    parts = email.split("@")
    if len(parts) == 2 and parts[1].endswith((".com", ".ru", ".org")):
        print("Домен:", parts[1])
    else:
        print("Некорректный адрес")
else:
    print("Некорректный адрес")

#prog6
text = input("Введите текст: ")
edited = text.strip().lower().replace(" ", "_")
print("Нормализованный текст:", edited)


#prog7
message = input("Введите сообщение: ")
if message.find("SECRET") != -1:
    message = message.replace("SECRET", "******")
    print(message)
    print("Сообщение содержит конфиденциальную информацию!")
else:
    print("Сообщение безопасно.")

#prog8
word = input("Введите слово: ")
codes = ""
for i in word:
    codes = codes + str(ord(i)) + " "
print("Коды символов:", codes)
decoded = ""
for code in codes.split():
    decoded = decoded + chr(int(code))
print("Восстановленное слово:", decoded)

#prog9
text = "login attempt failed access denied unauthorized access"
a=text.count("failed")
b=text.count("denied")
if a> 0 or b > 0:
    print("Попытка несанкционированного доступа!")
else:
    print("Доступ безопасен.")

#prog10
report = input("Введите отсчет: ")
sentences = report.split(".")
kolvo_sentences =0
for i in sentences:
    kolvo_sentences = kolvo_sentences + 1
delite_spaces = report.replace(" ", "")
count_symbols = len(delite_spaces)
starts_with_report = report.lower().startswith("report")
error_count = report.count("error")
print("Количество предложений:", kolvo_sentences)
print("Количество символов без пробелов:", count_symbols)
print("Начинается с 'Report':", starts_with_report)
if error_count >= 2:
    print("Ошибки найдены")
else:
    print("Ошибок нет")