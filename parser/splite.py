import re

def split_line(line):               
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