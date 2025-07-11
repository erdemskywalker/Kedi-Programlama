from lexer.lexer import lexer
from parser.commands import *
from parser.register import command_map

def creat_ast(tokens):
    tokens=lexer(tokens)
    if not tokens:
        return None
    if tokens[0]=="//" or tokens[0].startswith("//"):
        return None
    if tokens[0] in command_map:
        return command_map[tokens[0]](tokens)
    else:
        if len((" ".join(tokens[0:])).split("="))>1:
            return command_map["değiştir"](tokens)
        if len((" ".join(tokens[0:])).split("("))>1:
            return command_map["çağır"](tokens)
    return None
    