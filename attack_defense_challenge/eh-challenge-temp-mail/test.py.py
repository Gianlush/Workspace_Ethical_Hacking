def esc(s: str):
    ret = ''
    for el in s:
        if el == '{' or el == '}':
            ret += 'NONE'
        else: ret += el
    return ret


s = esc("{{__input__.__malevolo__.}}")
print(s)