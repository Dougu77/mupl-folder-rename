from utils.instructions import *
from utils.folder_manipulation import *

language = language_selection()

program_title(language)

program_explanation(language)

explain_create_chapters_folder(language)

create_chapters_folder()

confirm_chapters_folder_insertion(language)

start_fix_chapter_numeration(language)

fix_chapter_numeration()

finish_fix_chapter_numeration(language)

work = define_work(language)

volumes = define_volumes(language)

chapter_title = define_chapter_title(language)

groups = define_groups(language)

start_rename_folders(language)

rename_folders(work, volumes, chapter_title, groups)

finish_rename_folders(language)

finish_program(language)
