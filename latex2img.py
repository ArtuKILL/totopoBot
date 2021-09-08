from sympy import preview
from random import randint
# from datetime import time, date
pt = 11
pixels = pt*4/3

options = ["-z","0","--truecolor","-D 100", "bg", "Transparent"]

def main():
    op = 1

    i = 1
    while (op == 1):
        latexCode = input("Latex code: ")
        randomName = randint(0,100_000_000)
        #timestamp = f'{op}-{date.day}{date.month}{date.year}{time.hour}{time.minute}{time.second}'
        preview(f'$${latexCode}$$',viewer='file', filename = f".\\output\\{i} {randomName}.png", euler = False, dvioptions = options)
        op = int(input("Para seguir oprima 1.\n \tSalir cualquier tecla."))
        i = i+1

if __name__ == '__main__':
    main()


        


