import os
import getfiles

def run():
    with open('.unimake', 'r') as f:
        lines = f.readlines()

        app_name = ''
        author = ''
        root_folder = ''
        main_file = ''
        version = ''
        run_command =''

        for line in lines:
            main_line = line.strip()

            line_split = main_line.split(':')
            
            if 'app_name' in line_split[0]:
                app_name = line_split[1]
            
            if 'author' in line_split[0]:
                author = line_split[1]

            if 'root_folder' in line_split[0]:
                root_folder = line_split[1]

            if 'main_file' in line_split[0]:
                main_file = line_split[1]

            if 'version' in line_split[0]:
                version = line_split[1]
            
            if 'run_command' in line_split[0]:
                files = getfiles.get_files(root_folder)
                

                replacemnt = line_split[1].replace('<f>', main_file)
                replacemnt = replacemnt.replace('<n>', app_name)
                run_command = replacemnt
        
        run_command = run_command.replace('<>')
        print(files)

        os.system(run_command)
