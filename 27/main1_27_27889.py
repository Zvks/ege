f = open('27-0_demo.txt')                   # открывается файл
n = int(f.readline())                       # считывается количество строчек из первой строки файла и перевел в int
s = 0                                       # задается переменную миниальной суммы
minn = 20001                                # задается переменную миниальной разности
d = 0                                       # задается переменную текущей разности 
for i in range(n):                          # цикл в котором переираются все строки файла
    x, y = map(int, f.readline().split())   # считывается строка цикла, содержащая пару чисел, затем она разбивается на две строи, содержащие по числу,
                                            # после эти строки приводятся к int
    s += min(x, y)                          # к мин сумме прибавляется мин число из пары
    d = abs(x-y)                            # вычисляется модуль разности чисел данной пары
    if d % 3 != 0:                          # если разность данной пары не делится без остатка на три
        minn = min(d, minn)                 # то мин разность сравнивается с разностью данной пары чисел и минимальное число считается мин разностью
if s % 3 !=0:                               # если мин сумма делится на три без остатка
    print(s)                                # то выводится она
else:                                       # если нет
    print(s+minn)                           # то сумма мин суммы с мин разностью
f.close()           
