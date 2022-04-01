import shutil
import os

SOURCE_FILE_PATH = r'C:\Users\Feras\Desktop\New folder'


def create_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


for file_name in os.listdir(SOURCE_FILE_PATH):
    extension = os.path.splitext(file_name)[1].replace('.', '').upper()
    dir_path = fr'{SOURCE_FILE_PATH}\{extension}'
    create_dir(dir_path)
    shutil.move(fr'{SOURCE_FILE_PATH}\{file_name}', fr'{dir_path}\{file_name}')



