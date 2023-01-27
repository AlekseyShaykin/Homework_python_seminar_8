# Стартовая страница, Вводим нового сотрудника

def New_employee():
    a = str((input("Input name: "))+';')
    b = str(input("Input surname: ")+';')
    c = str(input("Input position: ")+';')
    d = str(input("Input salary: "))
    lst= a+b+c+d
    element = list(lst.split(';'))
    return element

def Ask_surname_search():
    return str(input('Ведите фамилию сотрудника для поиска: '))

def Ask_salary_search():
    return str(input('Ведите зарплату для поиска сотрудников: '))

def Ask_position_search():
    return str(input('Ведите должность сотрудника для поиска: '))

def Ask_to_delete():
    return str(input('Ведите фамилию сотрудника для удаления: '))

