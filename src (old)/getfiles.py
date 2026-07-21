import os

def get_files(root_folder):
    main_folder = root_folder.replace(' ', '')

    files = os.listdir(main_folder)
    files = [file for file in files if os.path.isfile(os.path.join(main_folder, file))]
    return files
