from utils.instructions import *
from utils.folder_manipulation import *

language = language_selection()

program_title(language)

program_explanation(language)

explain_create_chapters_folder(language)

create_chapters_folder()

test()

confirm_chapters_folder_insertion(language)

start_fix_chapter_numeration(language)

fix_chapter_numeration()

finish_fix_chapter_numeration(language)

work = define_work(language)

start_rename_folders(language)

rename_folders(work)

finish_rename_folders(language)

finish_program(language)
