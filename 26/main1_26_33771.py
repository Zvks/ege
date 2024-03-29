f = open('/home/user/pyth/ege/26/26_0.txt')   # Открывается файл
w = f.readline().split()                    # Считывается первая строка и делится на количество строк и N
sum = int(w[1])                             # Считывается N
a,b = [],[]                                 # Создаются 2 списка a и b
for i in f:                                 # Цикл перебирает строки в файле
    s = str(i).split()                      # Считывается строка из файла и делится на цену одного изделия, количество изделий в партии и тип изделия
    if s[2] == 'A':                         # Если тип изделиия A
        a.append([int(s[0]),int(s[1])])     # Список аппендится
    else:                                   # Иначе
        b.append([int(s[0]),int(s[1])])     # Список B добавляет    
sum1,sum2 = 0,0                             # Инициализация переменных sum1 и sum2
for i in b:                                 # Цикл for внутри списка b
    sum1 += i[0]*i[1]                       # Умножается первый элемент на второй элемент и прибавляется к sum1
sum2 = sum - sum1                           # Разница между sum и sum1 присваивается sum2
a.sort(key=lambda x:x[0])                   # Сортировка списка a по первому элементу
count = 0                                   # Инициализация переменной count
for i in a:                                 # Цикл for внутри списка a
    if sum2 - i[0]*i[1] < 0:                # Если разница между sum2 и произведением первого и второго элемента списка a меньше нуля
        count += int(sum2 / i[0])           # Прибавляется целое от деления sum2 на первый элемент списка a к count
        sum2 -= i[0] * int(sum2/i[0])       # Вычетается произведение первого элемента списка a на целое от деления sum2 на первый элемент списка a из sum2
        break                               # Прерывается цикл
    sum2 -= i[0] * i[1]                     # Вычетается произведение первого элемента списка a на второй элемент списка a из sum2
    count += i[1]                           # Прибавляется второй элемент списка a к count
print(count, sum2, sum)                     # Выводятся значения count, sum2 и sum