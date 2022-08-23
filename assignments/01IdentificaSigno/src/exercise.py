import math
def main():
    #escribe tu código abajo de esta línea
    numero = int(input('Dame un numero: '))
    def mensaje(numero):
        if numero <0:
            return 'Es negativo'
        if numero == 0:
            return 'Es cero'
        if numero >0:
            return 'Es positivo'
    resultado = mensaje(numero)
    print(resultado)
if __name__ == '__main__':
    main()
