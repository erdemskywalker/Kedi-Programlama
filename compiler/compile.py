from parser.tokenizer import token_to_ast
from compiler.global_code_c import global_code_one
from compiler.register import compile_map
from compiler.compilers import *
import os , platform
import compiler.state as state


def c_code(ret):
    if not isinstance(ret, dict):
        return ""
    if ret["type"] in compile_map:
        return compile_map[ret["type"]](ret)
    return None


def compile(read_file,write_file):
    with open(read_file, 'r') as line:
        lines = line.readlines()
    


    global_code=[
        global_code_one+'\n',
    ]
    main_code=[
        '\n\nint main() \n{'
    ]

    for line in lines:
        event=c_code(token_to_ast(line))
        if event is not None:
            if state.function == False:
                main_code.append(event)
                
            else:
                global_code.append(event)
        if event == "}":
            if state.depth > 0:
                state.depth -= 1
            else:
                state.function = False


    main_code.append('\n}')
    with open(write_file, 'w') as out:
        out.write("\n".join(global_code)+"\n")
        out.write("\n".join(main_code))

    print("✅ Program Çalıştırılıyor")
    os.system("gcc program.c -lSDL2 -lSDL2_ttf")
    if platform.system() == "Windows":
        os.system("a.exe")
    else:
        os.system("./a.out")