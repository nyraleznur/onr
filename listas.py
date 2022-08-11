nombre=[]


for i in range(2):

    datos=[]
    nom=input("Digite un nombre ")
    edad=int(input("Digite edad "))
    correo=input("Digite correo ")
    datos.append(edad)
    datos.append(correo)
    nombre.append(nom)
    nombre.append(datos)
print(nombre)
nombuscar=input("Digite el nombre a buscar ")

if nombuscar in nombre:
    ind=nombre.index(nombuscar)
    print(nombre[ind:ind+2])
else:
    print ("Dato no encontrado")
