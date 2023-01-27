import data_provider_import_data as d
import view as v
import logger_export as lo




def Add_element():
    return d.Add_position(v.New_employee())

def Find_surname():
    return d.Search_method(v.Ask_surname_search())

def Find_position():
    return d.Search_method(v.Ask_position_search())

def Find_salary():
    return d.Search_method(v.Ask_salary_search())

def Delete_element():
    return d.Delete_method(v.Ask_to_delete())

def Update():
    return d.Update()

def Export_json():
    return lo.Export_data_json(lo.Read_data())

def Export_csv():
    return lo.Export_data_csv(lo.Read_data())



def start():
    print("=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    button = int(input("Введите номер необходимого действия: "))
    if button ==1:
        Find_surname()
        if str(input("Вызвать меню еще раз? (y/n) "))=='y':
            start()
        else:
            exit()
    elif button==2:
        Find_position()
        if str(input("Вызвать меню еще раз? (y/n) "))=='y':
            start()
        else:
            exit()
    elif button ==3:
        Find_salary()
        if str(input("Вызвать меню еще раз? (y/n) "))=='y':
            start()
        else:
            exit()
    elif button ==4:
        Add_element()
        if str(input("Вызвать меню еще раз? (y/n) "))=='y':
            start()
        else:
            exit()
    elif button ==5:
        Delete_element()
        if str(input("Вызвать меню еще раз? (y/n) "))=='y':
            start()
        else:
            exit()
    elif button ==6:
        Update()
        if str(input("Вызвать меню еще раз? (y/n) "))=='y':
            start()
        else:
            exit()
    elif button == 7:
        Export_json()
        if str(input("Вызвать меню еще раз? (y/n) "))=='y':
            start()
        else:
            exit()
    elif button == 8:
        Export_csv()
        if str(input("Вызвать меню еще раз? (y/n) "))=='y':
            start()
        else:
            exit()
    elif button ==9:
            exit()



# def start():
#     options = [[Find_surname,Find_position,Find_salary,Add_element,Delete_element,Update,Export_json,Export_csv,exit_of_program]]
#     return options[v.show_menu() - 1]()

