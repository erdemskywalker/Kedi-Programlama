command_map={}

def register_command(name):
    def load(f):
        command_map[name] = f
        return f
    return load