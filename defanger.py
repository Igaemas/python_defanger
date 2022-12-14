import sys

class colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'

def Defanger(str):
    defangedSTR = ""

    for c in str:
        if(c == '.'):
            defangedSTR += "[.]"
        elif(c == 't'):
            defangedSTR += "X"
        else:
            defangedSTR += c
    return defangedSTR

if len(sys.argv) != 2:
    raise ValueError('Entrer une IP / URL à defang.')

str = sys.argv[1]


print("\n")
print("Input : ")
print("    " + colors.RED + str + colors.RESET)
print("\n")
print("Information modifié : ")
print(colors.GREEN + "    " + Defanger(str) + colors.RESET)
print("\n")