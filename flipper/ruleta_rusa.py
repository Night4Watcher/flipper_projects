import random
import os
from time import sleep

def main():
    numero_final = random.randint(0, 10)
    segundos = 9
    os.system("clear")
    for c in range(segundos):
        sleep(1)
        if c == numero_final:
            print("Bye Bye")
            os.system("shutdown now")
        print(c)
    print("Time Out....")
    print("You survived for now...")

if (__name__ == "__main__"):
    main()

