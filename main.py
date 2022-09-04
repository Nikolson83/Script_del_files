import time
import os


def delete_old_files(total_delete):
    global total_delete_file

    for path, dirs, files in os.walk(total_delete):
        for file in files:
            file_name = os.path.join(path, file)
            file_time = os.path.getmtime(file_name)
            if file_time < age_time:
                total_delete_file += 1
                os.remove(file_name)


def delete_empty_folders(total_delete):
    global total_delete_folder

    for path, dirs, files in os.walk(total_delete):
        if (not dirs) and (not files):
            total_delete_folder += 1
            os.rmdir(path)


def root_script():
    start_time = time.asctime()

    for total_delete in folders_list:
        delete_old_files(total_delete)
        delete_empty_folders(total_delete)

    finish_time = time.asctime()

    print('Start time:', str(start_time))
    print('Delete files:', str(total_delete_file))
    print('Delete folders:', str(total_delete_folder))
    print('Finished time:', str(finish_time))


if __name__ == '__main__':
    time_new = 15  # Сколько дней оставить.

    open_folders = os.path.join('data_file', 'folders_file.txt')  # Путь и имя файла
    with open (open_folders) as folders:  # Менеджеры контекста блокирования и разблокирования ресурсов, автоматического закрытия файлов.
        folders_list = [line.rstrip() for line in folders
                        if line != '/n' and not line.startswith('#')]  # Считать строки и исключить перенос строки и символа \
        # rstrip() также удаляет любой пробел в конце строки и /n

    total_delete_file = 0  # Количество удалённых файлов.
    total_delete_folder = 0  # Количество удалённых папок.

    now_time = time.time()  # Определяем текущую дату.
    age_time = now_time - 60*60*24*time_new  # Вычисляем дату с которой надо удалять файлы.

    root_script()
