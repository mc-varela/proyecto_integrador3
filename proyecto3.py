import os
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    tecla = 0
    while tecla <= 50:
        limpiar()
        print(tecla)
        try:
            t = input("Presiona una tecla ")
            if t != '':
                tecla += 1
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
