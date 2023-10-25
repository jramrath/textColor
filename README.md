This is an easy to use Python library which allows you to make your terminal outputs more colorful and therefore easier to read and understand.

It currently only works with Python3

The creator and maintainer is Jannik Ramrath (jramrath)

GitHub: https://github.com/jramrath/textColor

PyPi: https://pypi.org/project/textColor/


# Contributing

If you've found a bug or a typo, feel free to open an Issue on GitHub. Already have a solution? Make a Pull request and I'll take a look at your changes. Please make sure a similar Issue/Pull request doesn't already exist.


# Installation

This library is hosted on [pypi.org](https://pypi.org/project/textColor/). You can install it with **pip**:

`pip install textColor`


# Usage

To use this library, you first have to import it:
```
import textColor
```

To print colored text do the following:
```
print(textColor.green("GREEN"))           # 'GREEN' will be green
print(textColor.red("RED"))               # 'RED' will be red
print(textColor.blue("BLUE"))             # 'BLUE' will be blue
print(textColor.yellow("YELLOW"))         # 'YELLOW' will be yellow
```

You can also use special 'pre-fixes':
```
print(textColor.prompt("Name: "))         # will output '[?] Name: '  while '[?]' is yellow
print(textColor.info("Info"))             # will output '[-] Info'    while '[-]' is blue
print(textColor.error("ERROR"))           # will output '[!] ERROR'   while '[!]' is red
print(textColor.output("Success"))        # will output '[>] Success' while '[>]' is green
```

If those function names seem too long, you should use abbreviations:
```
green  ––> g
red    ––> r
blue   ––> b
yellow ––> y

error  ––> error
output ––> out
```


# License

This library was published under the **GNU General Public License**. For more information take a look at the **LICENSE** file.
