#Curso introduccion a la programacion en Python
#Paula Nevado
#Simulador de dados

import random   #libreria para generar números aleatorios

def main():
    #Observar como se debe dar la respuesta, solo es valido 1 o 0, no es valido si, no, S, N, si, No
    instruccion = input("¿Desea lanzar los dados? Esccribe 1 para Si o cualquier tecla para salir: ")  
    print("")     #Se imprime un espacio por organizacion
    while(instruccion == '1'):    #ciclo para que se lance el dado
        d1 = random.randint(1,6)   #dado 1
        d2 = random.randint(1,6)   #dado 2
        print(("El dado uno cayó en: ") + str(d1) + " y el dado dos en:" + str(d2) + "\n")  #imprime la salida de cada dado
        print("La suma de los dos dados es:" + str(d1 + d2) + "\n")  #imprime la suma de los dados

        #Pregunta al usuario si desea volver a lanzar los dados
        instruccion = input("¿Desea lanzar los dados de nuevo? Esccribe 1 para Si, o cualquier tecla para salir: ")

if __name__ == "__main__":
  main()