def create():
    author = input('author: ')
    program_name = input('program name: ')
    program_lang = input('programming language: ')
    program_main_file = input('main file: ')

    with open('cpii.json', 'w') as f:
        f.write('')

    with open('cpii.json', 'a') as f:
        f.write('{')
        f.write(f'\n\t"author": "{author}",')
        f.write(f'\n\t"name": "{program_name}",')
        f.write(f'\n\t"language": "{program_lang}",')
        f.write(f'\n\t"main-file": "{program_main_file}"')
        f.write(f'\n\t"additional-files": ')
        f.write('\n}')
