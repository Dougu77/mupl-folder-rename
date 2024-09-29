import os
from time import sleep

CHAPTERS_FOLDER = 'chapters'

def create_chapters_folder():
    os.makedirs(CHAPTERS_FOLDER, exist_ok=True)

def fix_chapter_numeration():
    folders = os.listdir(CHAPTERS_FOLDER)
    for folder in folders:
        if not folder.isdigit():
            space = folder.find(' ')
            folder_digit = folder[space + 1:]
        else:
            folder_digit = folder

        if folder_digit.startswith('0'):
            folder_final = folder_digit[1:]
        else:
            folder_final = folder_digit

        os.rename(f'{CHAPTERS_FOLDER}/{folder}', f'{CHAPTERS_FOLDER}/{folder_final}')

        print('.', end='', flush=True)

        sleep(0.2)
    
    print('\n')

def rename_folders(work:str):
    folders = os.listdir(CHAPTERS_FOLDER)
    for folder in folders:
        os.rename(f'{CHAPTERS_FOLDER}/{folder}', f'{CHAPTERS_FOLDER}/{work} [pt-br] - c{folder}')
        
        print('.', end='', flush=True)

        sleep(0.2)
    
    print('\n')

def test():
    for c in range(1, 51):
        if c < 10:
            folder_name = f'{CHAPTERS_FOLDER}/Capítulo 0{c}'
        else:
            folder_name = f'{CHAPTERS_FOLDER}/Capítulo {c}'
        os.makedirs(folder_name, exist_ok=True)
