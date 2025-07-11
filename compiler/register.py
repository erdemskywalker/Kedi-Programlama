compile_map = {}

def register_compile(name):
    def load(f):
        compile_map[name] = f
        return f
    return load




def split_outside_quotes_and_parens(s, delimiter='+'):
    result = []
    current = ""
    in_quote = False
    quote_char = ''
    paren_depth = 0
    s=s.strip()
    for c in s:
        if c in ('"', "'"):
            if not in_quote:
                in_quote = True
                quote_char = c
            elif quote_char == c:
                in_quote = False
            current += c
        elif c == '(':
            paren_depth += 1
            current += c
        elif c == ')':
            paren_depth -= 1
            current += c
        elif c == delimiter and not in_quote and paren_depth == 0:
            result.append(current.strip())
            current = ""
        else:
            current += c

    if current.strip():
        result.append(current.strip())
    return result



