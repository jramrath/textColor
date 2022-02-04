def green(text, whiteText="", space=True):
    if space:
        return "\033[1;32;49m" + str(text) + " \033[0;37;49m" + str(whiteText)
    else:
        return "\033[2;32;49m" + str(text) + "\033[0;37;49m" + str(whiteText)

def red(text, whiteText="", space=True):
    if space:
        return "\033[1;31;49m" + str(text) + " \033[0;37;49m" + str(whiteText)
    else:
        return "\033[1;31;49m" + str(text) + "\033[0;37;49m" + str(whiteText)

def blue(text, whiteText="", space=True):
    if space:
        return "\033[1;34;49m" + str(text) + " \033[0;37;49m" + str(whiteText)
    else:
        return "\033[1;34;49m" + str(text) + "\033[0;37;49m" + str(whiteText)

def yellow(text, whiteText="", space=True):
    if space:
        return "\033[1;33;49m" + str(text) + " \033[0;37;49m" + str(whiteText)
    else:
        return "\033[1;33;49m" + str(text) + "\033[0;37;49m" + str(whiteText)


def input(text):
    return "\033[1;33;49m" + "[?]" + " \033[0;37;49m" + str(text)

def info(text):
    return "\033[1;34;49m" + "[-]" + " \033[0;37;49m" + str(text)

def error(text):
    return "\033[1;31;49m" + "[!]" + " \033[0;37;49m" + str(text)

def output(text):
    return "\033[1;32;49m" + "[>]" + " \033[0;37;49m" + str(text)