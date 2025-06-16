#!/usr/bin/env python

import os
import platform
import argparse
import shlex
import re



function=False
depth=0

def split_line(line):
    if "boyut(" in line:
        line = re.sub(r'boyut\((.*?)\)', r'sizeof(\1)', line)
    if line.startswith("işlev") and "(" in line and ")" in line:
        match = re.match(r"işlev\s+(\w+)\((.*?)\)", line)
        if match:
            func_name = match.group(1)
            param_string = match.group(2)
            param_list = []
            for param in param_string.split(","):
                parts = param.strip().split()
                if len(parts) == 2:
                    param_list.append([parts[0], parts[1]])
            return ["işlev", func_name] + param_list

    tokens = re.findall(r'"[^"]*"|\S+', line)

    return tokens




def token_to_ast(tokens):
    tokens=split_line(tokens)
    if not tokens:
        return None
    
    if tokens[0]=="değişken":
        return {
            "type":"declaration",
            "var_type":tokens[1],
            "name":tokens[2],
            "value": tokens[4] if len(tokens)>4 and tokens[3]=="=" else None
        }
    elif tokens[0]=="işlev":
        return {
            "type":"function",
            "name":tokens[1],
            "parameters": tokens[2:] 
        }

    elif tokens[0]=="yaz":
        return {
            "type":"print",
            "text":"".join(tokens[1:]),
        }

    elif tokens[0]=="eğer":
        return {
            "type":"if",
            "func":tokens[1:]
        }
    
    elif tokens[0]=="sürekli":
        return {
            "type":"while",
            "func":tokens[1]
        }
    
    elif tokens[0]=="değilse":
        return {
            "type":"else",
        }

    elif tokens[0]==".":
        return {
            "type":"full",
        }
    
    elif tokens[0]=="çağır":
        return {
            "type":"call_function",
            "func":"".join(tokens[1:])
        }
    elif tokens[0]=="alt":
        return {
            "type":"n",
            "func":"\\n"
        }
    
    else:
        return None

def c_code(ret):
    global function
    global depth
    if not isinstance(ret, dict):
        return ""
    if ret["type"]=="declaration":
        if ret["var_type"]=="yazı":
            if ret["value"]!=None:
                return f"char {ret['name']}[] = {ret['value']};"
            else:
                return f"char {ret['name']};"
        elif ret["var_type"]=="sayı":
            if ret["value"]!=None:
                return f"int {ret['name']} = {ret['value']};"
            else:
                return f"int {ret['name']};"
        elif ret["var_type"]=="ondalık":
            if ret["value"]!=None:
                return f"float {ret['name']} = {ret['value']};"
            else:
                return f"float {ret['name']};"
    
    elif ret["type"]=="function": 
        function=True
        param=""
        for i in range(len(ret["parameters"])):
            if(i>0):
                if ret["parameters"][i][0]=="yazı":
                    param+=", char "+ret["parameters"][i][1]+"[]"
                elif ret["parameters"][i][0]=="sayı":
                    param+=", int "+ret["parameters"][i][1]+"[]"
                elif ret["parameters"][i][0]=="ondalık":
                    param+=", float "+ret["parameters"][i][1]+"[]"
            else:
                if ret["parameters"][i][0]=="yazı":
                    param+="char "+ret["parameters"][i][1]+"[]"
                elif ret["parameters"][i][0]=="sayı":
                    param+="int "+ret["parameters"][i][1]+"[]"
                elif ret["parameters"][i][0]=="ondalık":
                    param+="float "+ret["parameters"][i][1]+"[]"


        return "void "+ret['name']+"("+param+")\n{\n"
    
    elif ret["type"]=="print":
        return f'printf({ret["text"]});'

    elif ret["type"]=="if":
        if(function):
            depth=depth+1
        return 'if('+"".join(ret["func"])+'){'

    elif ret["type"]=="while":
        if(function):
            depth=depth+1
        return 'while('+"".join(ret["func"])+'){'

    elif ret["type"]=="else":
        if(function):
            depth=depth+1
        return "else{"

    elif ret["type"]=="full":
        return "}"

    elif ret["type"]=="call_function":
        return ret['func']+";"
    elif ret["type"]=="n":
        return f'printf("{ret['func']}");'



def compile(read_file,write_file):
    with open(read_file, 'r') as line:
        lines = line.readlines()
    
    global function
    global depth


    global_code=[
        '#include <stdio.h>\n#include <string.h>\n',
        'void girdi(char x[], int size) {'+f'\n',
        '  fgets(x, size, stdin);'+f'\n',
        '  x[strcspn(x, "\\n")] = 0;'+f'\n',
        '}'+f'\n\n',
        'int yazikarsilastir(const char *str1, const char *str2) {\n    while (*str1 && *str2) {\n  if (*str1 != *str2) {\n return 0;  \n}\n str1++;\nstr2++;\n } return *str1 == *str2;\n}    \n\n'
    ]
    main_code=[
        '\n\nint main() \n{'
    ]

    for line in lines:
        event=c_code(token_to_ast(line))
        if(function==False):
            main_code.append(event)
        else:
            global_code.append(event)
            if event=="}":
                if(depth>0):
                    depth=depth-1
                else:
                    function=False

    main_code.append('\n}')
    with open(write_file, 'w') as out:
        out.write("\n".join(global_code)+"\n")
        out.write("\n".join(main_code))

    print("✅ Program Çalıştırılıyor")
    os.system("gcc program.c")
    if platform.system() == "Windows":
        os.system("a.exe")
    else:
        os.system("./a.out")

def main():
    parser = argparse.ArgumentParser(description="SCANNER...")
    parser.add_argument("-s", "--dosya", required=True, help="Dosya")
    args = parser.parse_args()
    compile(args.dosya, "program.c")


if __name__ == "__main__":
    main()