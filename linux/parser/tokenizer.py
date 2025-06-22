from parser.splite import split_line
from parser.commands import *
from parser.register import command_map

def token_to_ast(tokens):
    tokens=split_line(tokens)
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
        print("d")
    return None

