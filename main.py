import os
import re
import subprocess

# Скрипт выполняет поиск файлов по тексту в их названии и копирует их в указанную папку.
file_with_names = input('Please enter file name where is list of files is stored: ')
with open(file_with_names, 'r') as my_file:
    names_data = my_file.read()
names_data = names_data.split('\n') # получаем лист из названий файлов которые мы хотим искать.

# Введем путь к папке где искать файлы
search_location = input('Please enter the path to the folder where files located: ')
os.chdir(search_location)
# Создадим список из названий файлов в директории 
file_list = os.listdir()

# Введем путь к папке куда копировать файлы
copy_loc = input('Please enter the path to the destination folder where you want files to be copied: ')
try:
    os.makedirs(copy_loc)
except IOError:
    print('Directory already exists')

# обработаем информацию о названиях файлов и скопируем их
for name in names_data:
    try:
        re_name = name.replace('.', '[_\.]*')
    except:
        pass
    try:
        re_name = re_name.replace('/', '_*')
    except:
        pass
    re_name = re_name + '....'
    for file in file_list:
        if re.search(re_name, file):
            path = os.path.join(copy_loc, file)
            status = subprocess.call(f'copy {file} {path}', shell=True)
            copied = True
    if copied:
        print(f'file {name} was found')
print(f'please check directory {copy_loc}')