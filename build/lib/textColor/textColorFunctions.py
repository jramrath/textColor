def green(colorText, whiteText="", space=True):
    if space:
        return "\033[1;32;40m" + str(colorText) + " \033[0;37;40m" + str(whiteText)
    else:
        return "\033[2;32;40m" + str(colorText) + "\033[0;37;40m" + str(whiteText)

def red(colorText, whiteText="", space=True):
    if space:
        return "\033[1;31;40m" + str(colorText) + " \033[0;37;40m" + str(whiteText)
    else:
        return "\033[1;31;40m" + str(colorText) + "\033[0;37;40m" + str(whiteText)

def blue(colorText, whiteText="", space=True):
    if space:
        return "\033[1;34;40m" + str(colorText) + " \033[0;37;40m" + str(whiteText)
    else:
        return "\033[1;34;40m" + str(colorText) + "\033[0;37;40m" + str(whiteText)

def yellow(colorText, whiteText="", space=True):
    if space:
        return "\033[1;33;40m" + str(colorText) + " \033[0;37;40m" + str(whiteText)
    else:
        return "\033[1;33;40m" + str(colorText) + "\033[0;37;40m" + str(whiteText)


def input(text):
    return "\033[1;33;40m" + "[?]" + " \033[0;37;40m" + str(text)

def info(text):
    return "\033[1;34;40m" + "[-]" + " \033[0;37;40m" + str(text)

def error(text):
    return "\033[1;31;40m" + "[!]" + " \033[0;37;40m" + str(text)

def output(text):
    return "\033[1;32;40m" + "[>]" + " \033[0;37;40m" + str(text)