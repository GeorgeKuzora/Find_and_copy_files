import os
import re
import subprocess

def input_drawings_numbers() -> list:
    """
    Эта функция возвращает лист из номеров чертежей которые мы хотим искать,
    на основании данных введенных пользователем.
    """
    right_input = False
    while not right_input:
        file_with_names = input('Please enter file name where is list of files is stored: ')
        try:
            with open(file_with_names, 'r') as my_file:
                names_data = my_file.read()
        except FileNotFoundError:
            print(f'There is not such file: {file_with_names}\nUse absolute path if neccesary')
        else:
            right_input = True
    names_data = names_data.split('\n')
    return names_data

def input_files_location() -> str:
    """Эта функция возвращает путь к папке в которой храняться файлы чертежей.
    На основании данных введенных пользователем"""
    result = False
    while not result:
        files_location = input('Please enter the path to the folder where files located: ')
        try:
            result = os.path.exists(files_location)
            if not result:
                raise FileNotFoundError
        except FileNotFoundError:
            print(f'There is no such directory: {files_location}\nUse absolute path if neccesary')
    return files_location

def input_copy_location() -> str:
    """Эта функция возвращает(при необходимости создает) путь к папке,
    куда найденые файлы будут скопированы. На основании данных введенных пользователем"""
    copy_loc = input('Please enter the path to the folder where you want files to be copied (new folder will be created if neccesary): ')
    try:
        os.makedirs(copy_loc)
    except IOError:
        print(f'Directory already exists: {copy_loc}')
    else:
        print(f'New directory was created: {copy_loc}')
    return copy_loc

def create_files_list(files_location: str) -> list:
    """Эта функция возвращает лист названий всех файлов в указанной директории."""
    try:
        files_list = os.listdir(files_location)
    except IOError:
        print(f'There is no such directory: {files_location}')
    return files_list   

def rename_draw_num(names_data: list) -> list:
    """Эта функция возвращает лист с названиями файлов,
    подготовленных для поиска модулем re. На основании данных из листа
    полученного из файла загруженного пользователем."""
    re_names_data = []
    for draw in names_data:
        try:
            re_draw = draw.replace('.', r'[\s_.]*')
        except:
            pass
        try:
            re_draw = re_draw.replace('/', r'[\s_.]*')
        except:
            pass
        re_names_data.append(re_draw)
    return re_names_data

def find_copy_files(files_location: str,
                    copy_loc: str,
                    files_list: list,
                    re_names_data: list) -> None:
    """
    Эта функция сравнивает названия файлов из списка файлов в директории
    указанной пользоватлем и названия полученные путем обработки модулем re
    номеров внесенны пользователем
    При совпадении стандартного выражения и названия файла
    файл копируется в указанную папку.
    """
    for re_name in re_names_data:
        for file in files_list:
            if re.search(re_name, file, re.IGNORECASE):
                file_path = os.path.join(files_location, file)
                copy_path = os.path.join(copy_loc, file)
                status = subprocess.call(f'copy {file_path} {copy_path}', shell=True)
                print(f'file {file} was found')
                break
    print(f'please check directory {copy_loc}')

if __name__ == '__main__':
    names_data = input_drawings_numbers()
    files_location = input_files_location()
    copy_loc = input_copy_location()
    files_list = create_files_list(files_location)
    re_names_data = rename_draw_num(names_data)
    find_copy_files(files_location, copy_loc, files_list, re_names_data)
