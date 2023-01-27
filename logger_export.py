# экспортируем простые данные  в csv файл (не словарем!)

import csv
import json


def Read_data():                      #сначала считываем данные из файла csv (можно txt указать)
    with open('PYTHON\Seminar_8\database.txt') as file:     
        reader = csv.reader(file) 
        reader = list(reader)   #преобразуем список в список списков для того, чтобы можно было его записать в другой csv файл в нормальном виде
        # print(reader)
        return reader



def Export_data_csv(reader):    # метод по экспорту данных в csv файл
    myFile = open('PYTHON\Seminar_8\Export_data_csv.csv', 'w')  
    with myFile:
      writer = csv.writer(myFile)
      writer.writerows(reader)
      print("File has written as .csv")



def Export_data_json(reader):
    data_json = json.dumps(reader)     # из словаря делаем строку
    with open("PYTHON\Seminar_8\Export_data_json.json", "w") as my_file:
       my_file.write(data_json)
       print("File has written as .json")











# МЕТОД, который одновременно считыает данные из файл и записывает в csv


# def Export_data_csv():
#     with open('PYTHON\Seminar_8\database.csv') as file:     #сначала считываем данные из файла csv
#         reader = csv.reader(file) 
#         reader = list(reader)   #преобразуем список в список списков для того, чтобы можно было его записать в другой csv файл в нормальном виде
#         print(reader)
#     myFile = open('PYTHON\Seminar_8\Export_data_csv.csv', 'w')  
#     with myFile:
#       writer = csv.writer(myFile)
#       writer.writerows(reader)