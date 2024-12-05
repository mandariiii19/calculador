def calc(string):
    
    """
    Функция для вычисления математического выражения, заданного в виде строки слов.
    Поддерживает значения в диапазоне [-99;99], скобки, операции вычитания, сложения и умножения.
    Args:
        string(str) - строковая запись математического выражения
    Returns:
        total(str) - строковая запись результата математического выражения
    """
    
    string = string.strip()
    listl = string.split(' ')
    result = ''
  
    if string == '':
        print('Некорректный ввод')
    
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

    for part in range(0, len(listl)):
        if listl[part] in dict:
            if dict[listl[part]].isnumeric():
                if part != (len(listl) - 1):
                    if listl[part + 1] in dict:
                        if dict[listl[part + 1]].isnumeric():
                            result += str(int(dict[listl[part]]) + int(dict[listl[part+1]]))
                        else:
                            result += dict[listl[part]]
                    else:
                        return 'Неверный ввод'
                else:
                    result += dict[listl[part]]
            else:
                result += dict[listl[part]]
        else:
            return 'Попробуйте снова'
            
    invdict = {v: k for k, v in dict.items()}
    
    if result.count('(') != result.count(')'):
        return "Неправильный ввод количества скобок"
    intresult = eval(result)
    strresult = str(intresult)
    total = ''

    if intresult < 0:
        total += 'минус '
        strresult = strresult[1:]
        intresult = int(strresult)
        
    if 11 <= intresult <= 19 or intresult == 0:
        total += invdict[strresult]
        
    else:
        delitel = '1' + '0' * len(strresult)
        for i in range(len(strresult)):
            if (intresult % int(delitel) - intresult % int(delitel[:-1])) != 0 and not(11 <= intresult % int(delitel) <= 19):
                total += invdict[str(intresult % int(delitel) - intresult % int(delitel[:-1]))] + ' '
            elif 11 <= (intresult % int(delitel)) <= 19:
                total += invdict[str(intresult % int(delitel))]
                break
            delitel = delitel[:-1]
    print(total)
print('Правила: введите строковое выражение для калькулятора. Калькулятор поддерживает значения в диапазоне от -99 до 99, скобки, операции вычитания, сложения и умножения.')

user_input = input('Введите выражение в формате <число> <операция> <число>: ')
result = calc(user_input)
if result != None:
    print(result)
