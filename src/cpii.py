import create
import run
import sys

command = sys.argv[1]

def main_program():

    if command == 'create':
        create.create()

    if command == 'run':
        run.run()

main_program()
