from parser.register import register_command
import re


@register_command("yazı")
def ast_declaration_string(tokens):    
    if len(tokens)>2:
        get=" ".join(tokens[1:])
    else:
        get=tokens[1]
    get=get.split("=")
    if len(get)>1:
        value=get[1]
    else:
        value='""'
    return {
            "type":"declaration_string",
            "name":get[0],
            "value": value
    }

@register_command("sayı")
def ast_declaration_int(tokens):    
    if len(tokens)>2:
        get=" ".join(tokens[1:])
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

@register_command("ondalık")
def ast_declaration_float(tokens):    
    if len(tokens)>2:
        get=" ".join(tokens[1:])
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

@register_command("değiştir")
def ast_assignment_declaration(tokens):
    try:
        value=(" ".join(tokens[0:])).split("=")[1]
        if value.startswith("'") or value.startswith('"'):
            return {
                "type":"assignment_declaration_string",
                "name": (" ".join(tokens[0:])).split("=")[0],
                "value": value
            }
        else:
            return {
                "type":"assignment_declaration_number",
                "name":(" ".join(tokens[0:])).split("=")[0],
                "value": (" ".join(tokens[0:])).split("=")[1]
            }
    except:
        return None