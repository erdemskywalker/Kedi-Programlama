import os
import platform
import argparse
import subprocess
from parser.creat_ast import creat_ast
from compiler.code import c_code
import compiler.state as state
from lib.global_code import global_code_one
import sys
import re
import shutil







def expand_file(file_path, file_name, visited_files=None):
    if visited_files is None:
        visited_files = set()

    expanded_lines = []

    if file_path in visited_files:
        return []

    visited_files.add(file_path)

    if not os.path.exists(file_path):
        print(f"❌ Hata: Dosya bulunamadı: {file_path}")
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("kullan"):
            x = ast_one(stripped.split(" "))
            nested_path = os.path.join(os.path.dirname(file_path), x["file_path"])
            nested_name = x["file_name"]

            print(f"📂 Dosya içe aktarılıyor: {nested_path}")
            expanded_lines.extend(expand_file(nested_path, nested_name, visited_files))
            i += 1
            continue

        control = creat_ast(line)
        if control is None:
            i += 1
            continue

        if control["type"] == "function":
            depth = 1
            new_func_name = f"{file_name}_{control['name']}"
            modified_line = line.replace(f"işlev {control['name']}(", f"işlev {new_func_name}(")
            function_lines = [modified_line]

            i += 1
            while i < len(lines) and depth > 0:
                inner_line = lines[i]
                inner_control = creat_ast(inner_line)

                if not inner_control:
                    function_lines.append(inner_line)
                    i += 1
                    continue

                if inner_control["type"] in ["if", "else", "while"]:
                    depth += 1
                elif inner_control["type"] == "full":
                    depth -= 1

                function_lines.append(inner_line)
                i += 1

            expanded_lines.extend(function_lines)
            continue

        elif control["type"] == "include":
            included_path = os.path.join(os.path.dirname(file_path), control["file_path"])
            included_name = os.path.splitext(os.path.basename(control["file_path"]))[0]
            expanded_lines.extend(expand_file(included_path, included_name, visited_files))
            i += 1
            continue

        i += 1

    return expanded_lines
















ErrorMessage="""❌ HATA: Derleyici kontrolü sırasında bir sorun oluştu. Lütfen sisteminize GCC kurunuz.
                GCC kurmak için sisteminize uygun aşağıdaki komutu kullanabilirsiniz:

                🔹 Debian / Ubuntu:
                    $ sudo apt update && sudo apt install build-essential

                🔹 Arch Linux / Manjaro:
                    $ sudo pacman -S base-devel

                🔹 Fedora:
                    $ sudo dnf groupinstall "Development Tools"

                🔹 openSUSE:
                    $ sudo zypper install -t pattern devel_C_C++

                🔹 Alpine:
                    $ sudo apk add build-base
                  """

#NORMAL ÇALIŞTIRMA 

def normal():
    try:
        if platform.system() == "Windows":
            if platform.architecture()[0] == "64bit":
                path = "C:\\Program Files\\Kedi\\mingw64\\bin\\gcc.exe"
            else:
                path = "C:\\Program Files\\Kedi\\mingw32\\bin\\gcc.exe"

            os.system("chcp 65001 >nul 2>&1")
            result = subprocess.run([path, "tmp\\program.c", "-o", "uygulama.exe"],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            if result.returncode != 0:
                print("❌ Derleme hatası")
                return

            shutil.rmtree("tmp", ignore_errors=True)
            exe_path = os.path.abspath("uygulama.exe")
            subprocess.run([exe_path])

        elif platform.system() == "Darwin":
            result = subprocess.run(["gcc", "tmp/program.c", "-o", "uygulama.out"],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            if result.returncode != 0:
                result2 = subprocess.run(["clang", "tmp/program.c", "-o", "uygulama.out"],
                                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if result2.returncode != 0:
                    print("❌ HATA: Derleyici kontrolü sırasında sorun oluştu.\n➡ Lütfen Xcode kurun: xcode-select --install")
                    return

            shutil.rmtree("tmp", ignore_errors=True)
            subprocess.run(["./uygulama.out"])

        else:
            result = subprocess.run(["gcc", "tmp/program.c", "-o", "uygulama.out"],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            if result.returncode != 0:
                print("❌ Derleme hatası (Linux)")
                return

            shutil.rmtree("tmp", ignore_errors=True)
            subprocess.run(["./uygulama.out"])

    except Exception as e:
        print("⛔ Sistemsel hata oluştu:", str(e))





#DEBUGLI ÇALIŞTIRMA 


def debug():
    if platform.system() == "Windows":
        if platform.architecture()[0]=="64bit":
            path='"C:\\Program Files\\Kedi\\mingw64\\bin\\gcc.exe"'
        else:
            path='"C:\\Program Files\\Kedi\\mingw32\\bin\\gcc.exe"'
        os.system("chcp 65001 >nul 2>&1")
        os.system(f"{path} tmp\\program.c -o tmp\\uygulama.exe")
        exe_path = os.path.abspath("tmp\\uygulama.exe")
        os.system(f'"{exe_path}"')
    elif platform.system()=="Darwin":
        compile_s=os.system("gcc tmp/program.c -o tmp/uygulama.out")
        if compile_s!=0:
            compile_s2=os.system("clang tmp/program.c -o tmp/uygulama.out")
            if compile_s2!=0:
                print("❌ HATA: Derleyici kontrolü sırasında bir sorun oluştu. Lütfen Xcode Command Line Tools'u kurunuz: xcode-select --install")
                exit(1)
        os.system("./tmp/a.out")
    else:
        try:
            os.system("gcc tmp/program.c -o tmp/uygulama.out")
            os.system("./tmp/uygulama.out")
        except:
            print(ErrorMessage)

def ast_one(tokens):
    if platform.system() == "Windows":
        x=os.getcwd()+"\\"+"\\".join(tokens[1].split("."))
    else:
        x=os.getcwd()+"/"+"/".join(tokens[1].split("."))
    x=x+".kedi"
    return{
        "type":"include",
        "file_path":x,
        "file_name":tokens[1]
    }

#COMPILE İŞLEMLERİ

def compile(read_file,write_file,mode):
    with open(read_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()


    global_code = [global_code_one + '\n']
    main_code = ['\n\nint main() {\n', '   SetConsoleOutputCP(CP_UTF8);\n']

    expanded_lines = []

    for line in lines:
        if line.strip().startswith("kullan"):
            x = ast_one(line.strip().split(" "))
            file_path = os.path.join(os.path.dirname(read_file), x["file_path"])
        
            expanded_lines.extend(expand_file(file_path,"_".join(x["file_name"].split("."))))
        else:
            expanded_lines.append(line)


    for index, line in enumerate(expanded_lines):
        event=creat_ast(line)
        if event is not None:
            if event["type"]=="declaration_string" or event["type"]=="declaration_int" or event["type"]=="declaration_float":
                value=c_code(event)
                value=value.split("=")
                global_code.append(value[0]+";")
                expanded_lines[index]=event["name"]+"="+event["value"]

    for line in expanded_lines:
        event=creat_ast(line)

        if(event is not None and event["type"]=="error"):
            print("Hata: "+event["code"]+"; "+ event["event"])
            continue
        event=c_code(event)


        #ekstralar
        for strx in state.strs:
            if strx in event:
                if strx+"=" in event:
                    pass
                else:
                    pattern = r'\b' + re.escape(strx) + r'\b'
                    event = re.sub(pattern, strx + '.veri', event)
        if event is not None and "girdi()" in event:
            if not re.search(r"\w+\s*=\s*girdi\(\)",event):
                event=event.replace("girdi()","girdi().veri")
        #ekstralar bitti

        
        if event is not None:
            if state.function == False:
                main_code.append(event)
                
            else:
                if(event[0:10]=="----------"):
                    state.function = False
                    state.depth = 0
                    event=event[10:]
                global_code.append(event)
        if event == "}":
            if state.depth > 0:
                state.depth -= 1
            else:
                state.function = False

    if not os.path.exists("tmp"):
        os.makedirs("tmp")
    main_code.append('\n}')
    with open("tmp/"+write_file, 'w', encoding='utf-8') as out:
        out.write("\n".join(global_code)+"\n")
        out.write("\n".join(main_code))

    print("✅ Program Çalıştırılıyor")

    if (mode):
        debug()
    else:
        normal()




#ANA ÇALIŞTIRMA

def main():
    if len(sys.argv) < 2:
        print("Kullanım: <dosya.kedi>")
        sys.exit(1)

    kedi_file = sys.argv[1]
    if not kedi_file.endswith(".kedi"):
        print("Lütfen bir .kedi dosyası girin!")
        sys.exit(1)
    
    c_dursun="-c" in sys.argv
    
    compile(kedi_file,"program.c",c_dursun)
    

if __name__ == "__main__":
    main()








