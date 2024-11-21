def calc():
    #Озвучивание правил пользователю
    print('Правила: введите строковое выражение для калькулятора. Калькулятор поддерживает значения в диапазоне [-99;99], скобки, операции вычитания, сложения и умножения.')
    
    #Прием выражения от пользователя
    string = input('Введите выражение в формате <число> <операция> <число>: ')
    
    #Убираю лишние пробелы в начале и конце строки
    string = string.strip()
    
    #Разделяю список по пробелу и получаю список из элементов  
    listl = string.split(' ')
    
    #Создаю переременную для итогового выражения
    result = ''
    
    #Защита на отправку пустой строки
    if string == '':
        print('Некорректный ввод')
    #Пословный перевод строки в математический вид, используя словарь
    
    #Создаю словарь для перевода самостоятельных значений
    dict = { 'минус' : '-', 'плюс' : '+', 'умножить' : '*', 'на' : '',
'открывается' : '(', 'закрывается' : ')', 'скобка' : '','ноль' : '0', 'один' : '1' , 'два' : '2', 'три' : '3', 'четыре' : '4', 'пять' : '5', 'шесть' : '6',
'семь' : '7', 'восемь' : '8', 'девять' : '9', 'десять' : '10', 'одиннадцать' : '11',
'двенадцать' : '12', 'тринадцать' : '13', 'четырнадцать' : '14', 'пятнадцать' : '15', 'шестнадцать' : '16',
'семнадцать' : '17', 'восемнадцать' : '18', 'девятнадцать' : '19', 'двадцать' : '20',
'тридцать' : '30', 'сорок' : '40', 'пятьдесят' : '50', 'шестьдесят' : '60', 'семьдесят' : '70',
'восемьдесят' : '80', 'девяносто' : '90', 'сто' : '100', 'двести' : '200', 'триста' : '300',
'четыреста' : '400', 'пятьсот' : '500', 'шестьсот' : '600', 'семьсот' : '700', 'восемьсот' : '800',
'девятьсот' : '900', 'одна тысяча' : '1000', 'две тысячи' : '2000', 'три тысячи' : '3000',
'четыре тысячи' : '4000', 'пять тысяч' : '5000', 'шесть тысяч' : '6000', 'семь тысяч' : '7000',
'восемь тысяч' : '8000', 'девять тысяч' : '9000'}

    #В данном случае part - это индекс элемента списка listl, НЕ элемент
    for part in range(0, len(listl)):
        #Проверка: Если элемент списка, взятый по индексу есть в словаре dict
        if listl[part] in dict:
            #Проверка: Входят ли в элемент слова - строку только числа?
            if dict[listl[part]].isnumeric():
                #Проверка: Если мы рассматриваем не первый индекс словаря, и предыдущий элемент в словаре состоит только из чисел?
                if part > 0 and dict[listl[part-1]].isnumeric():
                    pass

                #Проверка: Если мы рассматриваем не последний элемент списка liststring
                elif part != (len(listl) - 1):
                    #Проверка: Если следующий элемент списка находится в словаре
                    if listl[part + 1] in dict:
                        #Проверка: Если следующий элемент словаря состоит только из чисел?
                        if dict[listl[part + 1]].isnumeric():
                            #То к результирующей переменной, являющейся строкой, прибавляем предыдущее и следующее строковое значение из словаря
                            result += str(int(dict[listl[part]]) + int(dict[listl[part+1]]))
                        else:
                            #Иначе прибавляем текущий элемент словаря
                            result += dict[listl[part]]
                    else:
                        #Иначе: неверный ввод
                        return 'Неверный ввод'
                else:
                    #Иначе прибавляем текущий элемент словаря
                    result += dict[listl[part]]
            else:
                #Иначе прибавляем текущий элемент словаря
                result += dict[listl[part]]
        else:
            #Иначе защита
            return 'Попробуйте снова'

#Создаю второй словарь, который является перевернутой версией исходного, чтобы перевести математический результат в число
    invdict = {v: k for k, v in dict.items()}
    #Print(eval(result))
    #Получаю результат выражения с помощью eval()
    if result.count('(') != result.count(')'):
        return 'Не то кол-во скобок'
    intresult = eval(result)
    strresult = str(intresult)
    total = ''

    #Убираю у отрицательных чисел минус и вношу его в итоговый результат
    if intresult < 0:
        total += 'минус '
        strresult = strresult[1:]
        intresult = int(strresult)

    #Поскольку числа [11;19] являются самостоятельными словами, рассматриваю их отдельно, как и ноль
    if 11 <= intresult <= 19 or intresult == 0:
        total += invdict[strresult]
    else:
        #Delit - делитель, с помощью которого я дроблю число, например: 9801 на 9000 800 1
        delitel = '1' + '0' * len(strresult)
        for i in range(len(strresult)):
            if int(str(intresult % int(delitel) - intresult % int(delitel[:-1]))) != 0 and not(11 <= int(str(intresult % int(delitel))) <= 19):
                total += invdict[str(intresult % int(delitel) - intresult % int(delitel[:-1]))] + ' '
            elif 11 <= int(str(intresult % int(delitel))) <= 19:
                total += invdict[str(intresult % int(delitel))]
                break
            delitel = delitel[:-1]
    print(total)
calc()
