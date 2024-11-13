string1=input("Введите первую строку: ") #Ввод первой строки
string2=input("Введите вторую строку: ") #Ввод второй строки
string1= string1.replace(" ","").lower() #Убираем пробелы и переводим в строчный вид
string2= string2.replace(" ","").lower() #Убираем пробелы и переводим в строчный вид
sorted1=sorted(string1)
sorted2=sorted(string2)
if sorted1==sorted2: #Проверка на истинность значения 
    print("Эти две строки - анаграммы") #Вывод
else: #Если ложна
    print("Эти две строки - не анаграммы") #Вывод
