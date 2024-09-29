from utils.data_validation import *

def language_selection():
    language = validate_option('Escolha o idioma | Select the language [PT-BR | ENG]: ',
                               'Digite somente "PT-BR" ou "ENG" | Type only "PT-BR" or "ENG".',
                               ['PT-BR', 'PTBR', 'ENG'])
    
    print()
    
    if language == 'PTBR':
        return 'PT-BR'
    else:
        return language

def program_title(language:str):
    if language == 'PT-BR':
        title = 'Renomeador de pastas para o uploader em massa do One'
        length = 64
    else:
        title = "Renamer of folders to One's mass uploader"
        length = 53

    print('-' * length)
    print(f'{"-" * 5} {title} {"-" * 5}')
    print('-' * length)
    print()

def program_explanation(language:str):
    if language == 'PT-BR':
        print('-> Esse programa renomeia as pastas para estarem dentro do padrão de upload do programa do One.')
        print('-> Link para o uploader: ', end='')
    else:
        print('-> This program renames the folders to conform the upload standard of One\'s program.')
        print('-> Link to the uploader: ', end='')
    
    print('https://github.com/OneDefauter/mupl' + '\n')

def explain_create_chapters_folder(language:str):
    if language == 'PT-BR':
        print('Coloque as pastas dos capítulos dentro da recém criada pasta "chapters".\n')
    else:
        print('Place the chapter folders inside the newly created folder "chapters".\n')

def confirm_chapters_folder_insertion(language:str):
    if language == 'PT-BR':
        args = {'msg_input': 'Digite "OK" depois de colocar as pastas no local indicado: ',
                'msg_error': 'Digite somente "OK".'}
    else:
        args = {'msg_input': 'Type "OK" after putting the folders in the indicated place: ',
                'msg_error': 'Type only "OK".'}
    
    args['options'] = ['OK']
    validate_option(**args)
    print()

def start_fix_chapter_numeration(language:str):
    if language == 'PT-BR':
        print('Padronizando dos números dos capítulos:\n')
    else:
        print('Standardizing the chapter numbers:\n')

def finish_fix_chapter_numeration(language:str):
    if language == 'PT-BR':
        print('A padronização dos números dos capítulos foi finalizada.\n')
    else:
        print('The standardization of chapter numbers was finished.\n')

def define_work(language:str):
    if language == 'PT-BR':
        args = {'msg_input': 'Digite o nome da obra, o mesmo colocado no Mapa de IDs: ',
                'msg_error': 'O nome da obra não pode conter espaços. Utilize "_" ou "-" ao invés disso.'}
    else:
        args = {'msg_input': 'Type the name of the work, the same one used in the ID Map: ',
                'msg_error': 'The name of the work cannot contain spaces. Use "_" or "-" instead.'}
    
    work = validate_space(**args)
    
    print()
    
    return work

def start_rename_folders(language:str):
    if language == 'PT-BR':
        print('Renomeando as pastas:\n')
    else:
        print('Renaming the folders:\n')

def finish_rename_folders(language:str):
    if language == 'PT-BR':
        print('A renomeação das pastas foi finalizada.\n')
    else:
        print('The renomeation of the folders was finished.\n')

def finish_program(language:str):
    if language == 'PT-BR':
        input('Pressione ENTER para finalizar o programa...')
    else:
        input('Press ENTER to exit the program...')
