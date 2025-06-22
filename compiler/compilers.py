from compiler.register import register_compile
import compiler.state as state

@register_compile("declaration_string")
def compile_declaration_string(ret):
    return f"kedi_default_typedef_string {ret["name"]}=kedi_default_add_typedef_string("+ret["value"]+");"

@register_compile("assignment_declaration_string")
def compile_declaration_string(ret):
    return f"kedi_default_assignment_typedef_string(&{ret["name"]},{ret["value"]});"


@register_compile("declaration_int")
def compile_declaration_string(ret):
    return f"int {ret["name"]}="+ret["value"]+";"

@register_compile("assignment_declaration_number")
def compile_declaration_number(ret):
    return f"{ret["name"]} = {ret["value"]};"

@register_compile("declaration_float")
def compile_declaration_string(ret):
    return f"float {ret["name"]}="+ret["value"]+";"

@register_compile("function")
def compile_function(ret):
    state.function=True
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


@register_compile("print")
def compile_print(ret):
    return f'printf({ret["text"]});'


@register_compile("if")
def compile_if(ret):
    if(state.function):
        state.depth=state.depth+1
    return 'if('+"".join(ret["func"])+'){'


@register_compile("while")
def compile_while(ret):
    if(state.function):
        state.depth=state.depth+1
    return 'while('+"".join(ret["func"])+'){'


@register_compile("else")
def compile_else(ret):
    if(state.function):
        state.depth=state.depth+1
    return "else{"


@register_compile("full")
def compile_full(ret):
    return "}"

@register_compile("call_function")
def compile_call_function(ret):
    return ret['func']+";"


@register_compile("n")
def compile_n(ret):
    return f'printf("{ret['func']}");'