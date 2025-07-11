from parser.register import register_command
import os
import platform
import compiler.state as state

@register_command("yazı")
def ast_declaration_string(tokens):    
    try:
        if len(tokens)>2:
            get="".join(tokens[1:])
        else:
            get=tokens[1]
        get=get.split("=")
        
        if len(get)>1:
            value=get[1]
        elif len(get)>2:
            value=get[1:]
        else:
            value='""'
        return {
            "type":"declaration_string",
            "name":get[0],
            "value": value
        }
    except Exception as e:
        return{
            "type":"error",
            "code":"yazı",
            "event":"değişken oluşturulurken hata meydana geldi;"
        }
    

@register_command("değiştir")
def ast_assignment_declaration(tokens):
    try:
        if len(tokens)>3:
            value="".join(tokens[2:])
        else:
            value=tokens[2]
        
        return{
                "type":"assignment_declaration",
                "name":tokens[0],
                "value":value
            }
    except:
        return{
            "type":"error",
            "code":"değişken veri ataması",
            "event":"değişken veri atamasında hata meydana geldi;"
        }



@register_command("sayı")
def ast_declaration_int(tokens):
    try:
        if len(tokens)>2:
            get="".join(tokens[1:])
        else:
            get=tokens[1]
        get=get.split("=")
        if len(get)>1:
            value=get[1]
        else:
            value=""
    
        return {
            "type":"declaration_int",
            "name":get[0],
            "value": value
        }
    except:
       return{
            "type":"error",
            "code":"sayı",
            "event":"değişken oluşturulurken hata meydana geldi;"
        }    


@register_command("ondalık")
def ast_declaration_float(tokens):    
    if len(tokens)>2:
        get="".join(tokens[1:])
    else:
        get=tokens[1]
    get=get.split("=")
    if len(get)>1:
        value=get[1]
    else:
        value=""
    
    return {
            "type":"declaration_float",
            "name":get[0],
            "value": value
    }




@register_command("işlev")
def ast_function(tokens):
    return {
            "type":"function",
            "name":tokens[1],
            "parameters": tokens[2:]
        }
@register_command("yaz")
def ast_print(tokens):
    return {
            "type":"print",
            "text":"".join(tokens[1:]),
        }
@register_command("eğer")
def ast_if(tokens):
    return {
            "type":"if",
            "func":tokens[1:]
        }
@register_command("sürekli")
def ast_while(tokens):
    return {
            "type":"while",
            "func":tokens[1]
        }
@register_command("değilse")
def ast_else(tokens):
    return {
            "type":"else",
        }
@register_command(".")
def ast_full(tokens):
    return {
            "type":"full",
        }
@register_command("çağır")
def ast_call_function(tokens):
    if tokens[0]=="çağır":
        return {
            "type":"call_function",
            "func":"".join(tokens[1:])
        }
    return {
            "type":"call_function",
            "func":"".join(tokens[0:])
        }
@register_command("satır")
def ast_n(tokens):
    return {
            "type":"n",
            "func":"\\n"
        }


@register_command("dosya_işlemi")
def ast_FILE(tokens):
    return {
            "type":"FILE",
            "name":tokens[1]
        }

@register_command("dosya_kapa")
def ast_FILE_CLOSE(tokens):
    return {
            "type":"FILE_CLOSE",
            "name":tokens[1]
        }



@register_command("dönüt")
def ast_return(tokens):
    return {
            "type":"return",
            "value":" ".join(tokens[1:])
        }


def ast_include(tokens):
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