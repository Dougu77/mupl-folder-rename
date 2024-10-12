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

def get_volume_or_group(folder:str, volumes_or_group:str):
    list_division = volumes_or_group.split(';')
    for list_chapters in list_division:
        volume_or_group_divisor = list_chapters.find(':')
        chapter_divisor = list_chapters.find('-')
        volume_or_group = list_chapters[:volume_or_group_divisor]
        chapters_begin = list_chapters[volume_or_group_divisor + 1:chapter_divisor]
        chapters_end = list_chapters[chapter_divisor + 1:]
        for chapter in range(int(chapters_begin), int(chapters_end) + 1):
            if str(chapter) == folder:
                return volume_or_group

def rename_folders(work:str, volumes:str, chapter_title:str, groups:str):
    folders = os.listdir(CHAPTERS_FOLDER)
    for folder in folders:
        
        if volumes != '':
            if volumes.find(';') == -1:
                formated_volume = f' (v{volumes.strip()})'
            else:
                formated_volume = f' (v{get_volume_or_group(folder, volumes)})'
        else:
            formated_volume = volumes
        
        if groups.find(';') == -1:
            formated_group = groups.strip()
        else:
            formated_group = get_volume_or_group(folder, groups)
        
        os.rename(f'{CHAPTERS_FOLDER}/{folder}', f'{CHAPTERS_FOLDER}/{work} [pt-br] - c{folder}{formated_volume}{chapter_title} [{formated_group}]')
        
        print('.', end='', flush=True)

        sleep(0.2)
    
    print('\n')

def folder_creation_test():
    for c in range(1, 51):
        if c < 10:
            folder_name = f'{CHAPTERS_FOLDER}/Capítulo 0{c}'
        else:
            folder_name = f'{CHAPTERS_FOLDER}/Capítulo {c}'
        os.makedirs(folder_name, exist_ok=True)
