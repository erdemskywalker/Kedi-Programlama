compile_map = {}

def register_compile(name):
    def load(f):
        compile_map[name] = f
        return f
    return load