def create_unimake(app_name, author, root_folder, main_file, version, run_command):
    with open('.unimake', 'w') as f:
        f.write('[IMPORTANT]')
        f.write('\n{')
        f.write(f'\n\tapp_name: {app_name}')
        f.write(f'\n\tauthor: {author}')
        f.write(f'\n\troot_folder: {root_folder}')
        f.write(f'\n\tmain_file: {main_file}')
        f.write(f'\n\tversion: {version}')
        f.write(f'\n\trun_command: {run_command}')
        f.write('\n}')

def init():
    app_name = input("app name: ")
    author = input("author: ")
    root_folder = input("root folder: ")
    main_file = input("main file: ")
    version = input("version: ")
    run_command = input("run command: ")

    create_unimake(app_name, author, root_folder, main_file, version, run_command)

    print(f'\napp name: {app_name}')
    print(f'auhtor: {author}')
    print(f'root folder: {root_folder}')
    print(f'main file: {main_file}')
    print(f'version: {version}')
    print(f'run command: {run_command}')
