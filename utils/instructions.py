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
    uploader_link = 'https://github.com/OneDefauter/mupl'
    pyneko_link = 'https://github.com/Lyem/pyneko'
    if language == 'PT-BR':
        print('-> Esse programa renomeia as pastas para estarem dentro do padrão de upload do programa do One.')
        print('-> Utilize o nome da obra e os nomes dos grupos igual a como está no Mapa de IDs do uploader.')
        print('-> Use o seguinte padrão para que o programa renomeie as pastas com os volumes certos = volume | volume:capitulo-capitulo;volume:capitulo-capitulo')
        print('-> Exemplos = 1 | 1:1-10;2:11-20')
        print('-> Para os grupos, é o mesmo padrão, mas se for só um grupo para todos os capítulos, digite somente o nome do grupo. E, para mais de um grupo, coloque + entre os nomes = grupo:capitulo-capitulo;grupo+grupo:capitulo-capitulo')
        print('-> Exemplos = Scan_A:1-10;Scan_A+Scan_B:11-20;Scan_B:21-30')
        print(f'-> Baixe o uploader em = {uploader_link}')
        print(f'-> Utilize o Pyneko para baixar as obras = {pyneko_link}\n')
    else:
        print('-> This program renames the folders to conform the upload standard of One\'s program.')
        print('-> Use the name of the work and the names of the groups exactly as they are in the uploader\'s ID Map.')
        print('-> Use the following format for the program to rename the folders with the correct volumes: volume | volume:chapter-chapter;volume:chapter-chapter')
        print('-> Examples = 1 | 1:1-10;2:11-20')
        print('-> For the groups, it\'s the same format, but if there is only one group for all the chapters, enter just the name of the group. And, for multiple groups, place a + between the names = group:chapter-chapter;group+group:chapter-chapter')
        print('-> Examples = Scan_A:1-10;Scan_A+Scan_B:11-20;Scan_B:21-30')
        print(f'-> Download the uploader on = {uploader_link}')
        print(f'-> Use the Pyneko to download the manga/manhwa/manhua = {pyneko_link}\n')

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
        print('Padronizando os números dos capítulos:\n')
    else:
        print('Standardizing the chapter numbers:\n')

def finish_fix_chapter_numeration(language:str):
    if language == 'PT-BR':
        print('A padronização dos números dos capítulos foi finalizada.\n')
    else:
        print('The standardization of chapter numbers was finished.\n')

def define_work(language:str):
    if language == 'PT-BR':
        args = {'msg_input': 'Digite o nome da obra: ',
                'msg_error': 'O nome da obra não pode conter espaços. Utilize "_" ao invés disso.'}
    else:
        args = {'msg_input': 'Type the name of the work: ',
                'msg_error': 'The name of the work cannot contain spaces. Use "_" instead.'}
    
    work = validate_space(**args)
    
    print()
    
    return work

def get_volumes_division(language:str):
    if language == 'PT-BR':
        args = {'msg_input': 'Digite os volumes e os capítulos em cada volume: ',
                'msg_error': 'Siga o padrão explicado nas instruções.'}
    else:
        args = {'msg_input': 'Type the volumes and the chapter in each volume: ',
                'msg_error': 'Follow the pattern explained in the instructions.'}
    
    volumes = validate_space(**args)
    
    return volumes

def define_volumes(language:str):
    if language == 'PT-BR':
        args = {'msg_input': 'A obra tem número do volume [S | N]: ',
                'msg_error': 'Digite somente "S" ou "N".',
                'options': ['S', 'SIM', 'N', 'NÃO', 'NAO']}
    else:
        args = {'msg_input': 'The work has volume number [Y | N]: ',
                'msg_error': 'Type only "Y" or "N".',
                'options': ['Y', 'YES', 'N', 'NO']}
    
    if validate_option(**args) in ['S', 'SIM', 'Y', 'YES']:
        print()
        volumes = get_volumes_division(language)
    else:
        volumes = ''

    print()
    
    return volumes

def define_chapter_title(language:str):
    if language == 'PT-BR':
        args = {'msg_input': 'Os capítulos tem título [S | N]: ',
                'msg_error': 'Digite somente "S" ou "N".',
                'options': ['S', 'SIM', 'N', 'NÃO', 'NAO']}
    else:
        args = {'msg_input': 'The chapters have title [Y | N]: ',
                'msg_error': 'Type only "Y" or "N".',
                'options': ['Y', 'YES', 'N', 'NO']}
    
    if validate_option(**args) in ['S', 'SIM', 'Y', 'YES']:
        chapter_title = ' ()'
    else:
        chapter_title = ''
    
    print()
    
    return chapter_title

def define_groups(language:str):
    if language == 'PT-BR':
        args = {'msg_input': 'Digite o(s) grupo(s): ',
                'msg_error': 'Siga o padrão explicado nas instruções.'}
    else:
        args = {'msg_input': 'Type the group(s): ',
                'msg_error': 'Follow the pattern explained in the instructions.'}
    
    groups = validate_space(**args)
    
    print()
    
    return groups
        
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
