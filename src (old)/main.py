import sys
import init
import run
import intro

def main_program():
    command_num = len(sys.argv)

    if command_num == 1:
        intro.help()
    elif command_num == 2:
        command = sys.argv[1]

        if command == "init":
            init.init()
        elif command == "run":
            run.run()
        elif command == "help":
            intro.help()
        else:
            print('Imprper syntax, type help to referance commands')

main_program()
