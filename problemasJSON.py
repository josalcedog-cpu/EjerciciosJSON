#Autor: José Daniel Salcedo Gutiérrez

import json 

with open("docu.json", "r") as read_file:
    data = json.load(read_file)

#primer ejercicio
def uno(): 
    d=input("Inserta un deporte: ")
    for p in data.values():
        if d in p["deportes"]: 
            print(f"Nombre:{p["nombres"]}\nApellidos:{p["apellidos"]} ")

def dos(): 
    b0 = int(input("Inserta una edad minima: "))
    b1 = int(input("Inserta una edad máxima: "))
    for p in data.values():
        n = p["edad"]
        if b0 <= n <= b1:
            print(f"Nombre:{p["nombres"]}\nApellidos:{p["apellidos"]} ")
def main(): 
    while True:
        x = input("Usuario desea realizar la busqueda por deportes o por edad?:\t")
        if x.lower() == "deportes":
            uno()
            y = input("Desea realizar otra busqueda?\n")
            if y.lower() == "no":
                break
        if x.lower() == "edad": 
            dos()
            z = input("Desea realizar otra busqueda?")
            if z.lower() == "no":
                break


if __name__ =="__main__":
    main()