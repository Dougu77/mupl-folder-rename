import os

def create_chapters_folder():
    os.makedirs('chapters', exist_ok=True)

def fix_chapter_numeration():
    folders = os.listdir('chapters')
    print(folders)
    
def test():
    for c in range(1, 10):
        os.makedirs(f'chapters/Capítulo {c}', exist_ok=True)