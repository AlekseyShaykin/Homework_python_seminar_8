

# def read_csv():
#     with open('PYTHON\Seminar_8\database.csv', 'r', encoding = 'utf-8') as file:
#         # print(file.read())
#         lst=[]
#         return(lst.append(file.split('\n')))

# print(read_csv())


# def read_csv():
#     with open('PYTHON\Seminar_8\database.csv', 'r', encoding = 'utf-8') as file:
#         # print(file.read())
#         myList = []
#         for line in file:
#             if line.strip() != '':
#                 myList.append(line.strip())   # strip разделяем построчно
#     return myList

# print(read_csv())


# метод поиска, добавления, удаления



def Search_method(key):
    with open('PYTHON\Seminar_8\database.txt', 'r') as text:
        line = text.read().split('\n')
        for i in line:
            if i.count(key):
             name, surname, position, salary = i.split(';')
             print(f'{name}\n{surname}\n{position}\n{salary}')
             print('================'+'\n')


def Add_position(element):
    name, surname, position, salary =element
    with open('PYTHON\Seminar_8\database.txt','a') as text:
        element = f'{name};{surname};{position};{salary}'
        text.write(str(f'\n{element}'))

def Delete_method(key):
    with open('PYTHON\Seminar_8\database.txt', 'r',encoding = 'utf-8') as text:
        line = text.read().strip().split('\n')
        sum=0
        # print(line)
        for i in line:
            if i.count(key):
                 sum += i.count(key)
                 line.remove(i)
                #  print(line)
                 print('Сотрудник удален из базы данных')
                 with open('PYTHON\Seminar_8\database.txt', 'w',encoding = 'utf-8') as text:
                    for element in line:
                     text.write(element)
                     text.write('\n')
                    text.close()
            #  name, surname, position, salary = line
            #  line_del = f'{name};{surname};{position};{salary}'
            #  text.write(str(f'{line_del}\n'))
            #  name, surname, position, salary = i.split(';')
            #  print(f'{name}; {surname}; {position}; {salary}')     #print(f'{name}\n{surname}\n{position}\n{salary}') - другой вывод
        if sum ==0:
          print('Элемент не найден')


def Update():
    with open('PYTHON\Seminar_8\database.txt', 'r', encoding='utf-8') as file:
        line = file.read().strip().split('\n')
        # print(line)
        for i in line:
             name, surname, position, salary = i.split(';')
             print(f'{name};{surname};{position};{salary}')
        print('=============================='+'\n')
        print(list(enumerate(line)))
        print('=============================='+'\n')
        index = (int(input('введите номер элемента, который Вы хотите скорректировать: ')))
        print(line[index])
        string = str(input('ВВедите обновленный вариант строки через ";" : '))
        line[index] = string
        print(line)
        with open('PYTHON\Seminar_8\database.txt', 'w',encoding = 'utf-8') as text:
         for element in line:
            text.write(element)
            text.write('\n')
        text.close()

