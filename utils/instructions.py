from utils.data_validation import *

def language_selection():
    language = validate_option('Escolha o idioma | Select the language: [PT-BR | ENG] ',
                               'Digite somente "PT-BR" ou "ENG" | Type only "PT-BR" or "ENG".',
                               ['PT-BR', 'PTBR', 'ENG'])
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

    print()
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
        print('Coloque as pastas dos capítulos dentro da recém criada pasta "chapters".')
    else:
        print('Place the chapter folders inside the newly created folder "chapters".')

def confirm_chapters_folder_insertion(language:str):
    if language == 'PT-BR':
        args = {'msg_input': 'Digite "OK" depois de colocar as pastas no local indicado: ',
                'msg_error': 'Digite somente "OK".'}
    else:
        args = {'msg_input': 'Type "OK" after putting the folders in the indicated place: ',
                'msg_error': 'Type only "OK".'}
    args['options'] = ['OK']
    validate_option(**args)
    

def start_fix_chapter_numeration(language:str):
    if language == 'PT-BR':
        print('Começando a padronização dos números dos capítulos:\n')
    else:
        print('Starting the standardization of chapter numbers:\n')
        