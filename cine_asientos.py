filas = int(input("Ingrese el numero de filas del cine: "))
columnas = int(input("Ingresae el numero de columnas: "))

while filas <= 0 or columnas <= 0:
    print("Error: las filas y columnas deben ser mayor que 0")
    filas = int(input("Ingrese el numero de filas: "))
    columnas = int(input("Ingrese el numero de columnas: "))

asientos = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append("L")
    asientos.append(fila)



def mostrar_sala():
    print("========== SALA DE CINE ==========")
    print("       ", end="")

    for j in range(columnas):
        print(f"{j + 1:^5}", end="")

    print()

    for i in range(filas):
        print(f"Fila {i + 1}: ", end="")

        for j in range(columnas):
            print(f"{asientos[i][j]:^5}", end="")

        print()

    print("L = Libre")
    print("X = Ocupado")



def reservar_asiento():
    print("========== RESERVAR ASIENTO ==========")

    fila = int(input("Ingrese el numero de fila: "))
    columna = int(input("Ingrese el numero de asiento: "))

    if fila < 1 or fila > filas or columna < 1 or columna > columnas:
        print("Error: el asiento seleccionado no existe")

    else:
        fila = fila - 1
        columna = columna - 1

        if asientos[fila][columna] == "L":
            asientos[fila][columna] = "X"
            print("El asiento fue reservado correctamente")

        else:
            print("Este asiento ya esta ocupado")



def liberar_asiento():
    print("========== LIBERAR ASIENTO ==========")

    fila = int(input("Ingrese el numero de fila: "))
    columna = int(input("Ingrese el numero de asiento: "))

    if fila < 1 or fila > filas or columna < 1 or columna > columnas:
        print("Error: el asiento seleccionado no existe")

    else:
        fila = fila - 1
        columna = columna - 1

        if asientos[fila][columna] == "X":
            asientos[fila][columna] = "L"
            print("El asiento se libero correctamente")

        else:
            print("Este asiento esta libre")


def contar_asientos():
    ocupados = 0
    libres = 0

    for i in range(filas):
        for j in range(columnas):

            if asientos[i][j] == "X":
                ocupados += 1

            else:
                libres += 1

    print("========== ESTADISTICAS ==========")
    print("Total de asientos:", filas * columnas)
    print("Asientos ocupados:", ocupados)
    print("Asientos libres:", libres)


while True:

    print("================================")
    print("       SISTEMA DE CINE")
    print("================================")
    print("1. Mostrar sala")
    print("2. Reservar asiento")
    print("3. Liberar asiento")
    print("4. Contar asientos ocupados y libres")
    print("5. Salir")
    print("================================")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        mostrar_sala()

    elif opcion == "2":
        reservar_asiento()

    elif opcion == "3":
        liberar_asiento()

    elif opcion == "4":
        contar_asientos()

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opcion no valida")
