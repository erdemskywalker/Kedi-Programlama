from compiler.register import compile_map
from compiler.compilers import *

def c_code(ret):
    if not isinstance(ret, dict):
        return ""
    if ret["type"] in compile_map:
        return compile_map[ret["type"]](ret)
    return None