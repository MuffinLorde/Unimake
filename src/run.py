import json
import os

def run():
    with open('cpii.json', 'r') as f:
        data = json.load(f)

        progarm_name = data['name']
        program_lang = data['language']
        program_main_file = data['main-file']

        if program_lang == 'python' or 'py':
            os.system(f'python {program_main_file}')
        
        if program_lang == 'c':
            os.system(f'gcc {program_main_file} -o {progarm_name}')

        if program_lang == 'cpp' or 'c++':
            os.system(f'g++ {program_main_file} -o {progarm_name}')

        if program_lang == 'rs':
            os.system(f'rustc {program_main_file}')
