import random

def main():
  print("TIRADA DE DADOS")
  tirar= input("para tirar pulse enter: ")
  numero= int(input("numero de dados: "))
  
  while tirar == "":
    DADO1 = random.randint(1,7)
    DADO2 = random.randint(1,7)

    print(f"dado 1 igual a: {DADO1}, y el dado 2 es igual a: {DADO2}") 
    
    suma= DADO1 + DADO2

    print(f"el valor de la suma es igual a: {suma}.")

    seguir = input("si quieres volver a tirar presiona enter, si quieres terminar presiona otra tecla ")


    print("JUEGO TERMIANDO")
    
 
    

if __name__ == "__main__":
  main()