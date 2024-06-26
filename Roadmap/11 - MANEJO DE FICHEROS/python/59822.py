import os 

file_name = "59822.txt"

with open(file_name, "w") as file:
    file.write("Katherinne\n")
    file.write("18\n")
    file.write("Python\n")
    
with open(file_name, "r") as file:
    contenido = file.read()
    print(contenido)

os.remove(file_name)

''' EXTRA '''
venta = "ventas.txt"

open(venta, "a")

print("Select an option:\n1. Añadir producto\n2. Consultar producto\n3. Borrar producto\n4. Mostrar productos\n5. Calcular venta total\n6. Calcular venta por producto\n7. Salir")

option = int(input("Select an option: "))

match option:
    case 1:
        product = input("Enter product name: ")
        quantity = int(input("Enter product quantity: "))
        price = float(input("Enter product price: "))
        
        with open(venta, "a") as file:
            file.write(f"{product}, {quantity}, {price}\n")
    case 2:
        product = input("Enter product name: ")
        with open(venta, "r") as file:
            for i in file.readlines():  #devuelve en lista por lineas
                if i.split(", ")[0] == product: #separa por coma y espacio
                    print(i)
                    break
    case 3:
        product = input("Enter product name: ")
        with open(venta, "r") as file:
            lines = file.readlines()
            for i in lines:
                if i.split(",")[0] != product:
                    file.write(i)
    case 4:
        with open(venta, "r") as file:
            print(file.read())
    case 5:
        with open(venta, "r") as file:
            total = 0
            for i in file.readlines():
                total += float(i.split(", ")[1]) * float(i.split(", ")[2])
        print(total)
    case 6:
        product = input("Enter product name: ")
        total_product = 0
        with open(venta, "r") as file:
            for i in file.readlines():
                if i.split(",")[0] == product:
                    total_product += float(i.split(",")[1]) * float(i.split(",")[2])
        print(total_product)
    case 7:
        os.remove(venta)
    case _:
        print("Invalid option")