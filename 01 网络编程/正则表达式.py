import re

names = ['name123', '1name222', '_adskfj22', '__na!me__']
for name in names:
    if re.match(r"^[a-zA-Z_][a-z0-pA-Z]*$", name):
        print("变量名{}符合要求".format(name))
    else:
        print("变量名{}不符合要求".format(name))
