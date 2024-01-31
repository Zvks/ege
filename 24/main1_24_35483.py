with open("/home/user/pyth/ege/24/24_demo.txt", "r") as file:                                            # Открываем файл для чтения
    text = file.read()                                                          # Считываем содержимое файла в строку

max_len = 0                                                                     # Максимальная длина цепочки
current_len = 0                                                                 # Текущая длина цепочки
char_num = 1                                                                    # Счетчик символов в цепочке

for char in text:                                                               # Проходимся по каждому символу в строке
    if (char == "X") and (char_num == 1):
        current_len += 1
        char_num += 1
    elif (char == "Y") and (char_num == 2):
        current_len += 1
        char_num += 1
    elif (char == "Z") and (char_num == 3):
        current_len += 1
        char_num = char_num - 2
    else:
        char_num = 1
        current_len = 0                                                         # Если текущая последовательность не является XYZ, 
                                                                                # сбрасываем значения счетчиков символов в ноль        

    if current_len > max_len:                                                   # Если текущая последовательность является XYZ и 
                                                                                # current_len больше max_len, обновляем max_len
        max_len = current_len

print(max_len)
