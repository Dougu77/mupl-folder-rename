# Imports
import os
from time import sleep

# Folder constant of where the chapters folders go
CHAPTERS_FOLDER = 'chapters'

# Functions
def create_chapters_folder():
    '''summary_
    Create the folder where the chapters folders go.
    '''
    os.makedirs(CHAPTERS_FOLDER, exist_ok=True)

def fix_chapter_numeration():
    '''summary_
    Padronize the chapter number to the Mupl pattern.
    '''
    
    # Get the folders
    folders = os.listdir(CHAPTERS_FOLDER)
    
    # Iterate in each folder
    for folder in folders:
        
        # Verify if the folder name is only number
        if not folder.isdigit():
            space = folder.find(' ')
            folder_digit_one = folder[space + 1:]
        else:
            folder_digit_one = folder

        # Verify if the folder is 3 digits
        if len(folder_digit_one) == 3:
            
            # Verify if the folder is a special chapter (X.5)
            if folder_digit_one[1] == '.':
                folder_digit_two = folder_digit_one
            else:

                # Verify if the folder is of chapters below 10
                if folder_digit_one[1] == '0':
                    folder_digit_two = folder_digit_one[2]
                else:
                    folder_digit_two = folder_digit_one[1:]
        else:
            folder_digit_two = folder_digit_one
        
        # Verify if the folder is of chapters below 10 
        if folder_digit_two.startswith('0'):
            folder_final = folder_digit_two[1:]
        else:
            folder_final = folder_digit_two

        # Rename the folder
        os.rename(f'{CHAPTERS_FOLDER}/{folder}', f'{CHAPTERS_FOLDER}/{folder_final}')

        # Print "." after renaming the chapter
        print('.', end='', flush=True)

        # Wait 0.2 second to make the next folder rename
        sleep(0.2)
    
    # Break a line in the console after renaming all folders
    print('\n')

def get_volume_or_group(folder:str, volumes_or_group:str):
    '''summary_
    Get the data of which volume or group the chapter belongs.
    
    Args:
        folder (str): The folder that is going the be used to check the data.
        volumes_or_group (str): The list of volumes or groups division of all folders.

    Returns:
        str: The volume or the group that the chapter belongs.
    '''   

    # Get the list of chapters in each volume or group
    list_division = volumes_or_group.split(';')
    
    # Iterate in each part of the list
    for list_chapters in list_division:
        
        # Get the divisors of the data
        volume_or_group_divisor = list_chapters.find(':')
        chapter_divisor = list_chapters.find('-')
        volume_or_group = list_chapters[:volume_or_group_divisor]
        
        # Verify if it's only 1 chapter in the volume or group
        if chapter_divisor == -1:
            chapters_begin, chapters_end = float(list_chapters[volume_or_group_divisor + 1:])
            
        else:
            chapters_begin = list_chapters[volume_or_group_divisor + 1:chapter_divisor]
            chapters_end = list_chapters[chapter_divisor + 1:]
            
        # Convert to float
        chapters_begin_float = float(chapters_begin)
        
        if int(chapters_end) != float(chapters_end):
            chapters_end_float = float(chapters_end)
        else:
            chapters_end_float = float(chapters_end) + 0.9

        # Verifiy if the folder is between the start and end chapters
        if float(folder) >= chapters_begin_float and float(folder) <= chapters_end_float:
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
