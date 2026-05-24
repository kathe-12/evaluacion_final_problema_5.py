#matriz para  guardar los datos de los recursos
matriz_recursos =[]

#calcular total de horas

def calcular_horas(horas):
    total = sum(horas)

    if total >40:
        clasificacion = "sobretiempo"
    else:
        clasificacion ="horario estandar"
    return total, clasificacion

# registrar recursos
def registrar_recursos():
    global matriz_recursos

# limpiar datos anteriores
matriz_recursos = []
dias =["lunes","martes","miercoles","jueves","viernes"]

print("\n=== REGISTRO DE HORAS ===")

for i in range(4):
    print( f"\nRecurso {i + 1}")
    nombre = input("ingrese el nombre del recurso: ")
    horas = []
    for dia in dias:
            while True:
                try:
                    hora = float(input(f"Ingrese horas trabajadas el {dia}: "))
                    if hora < 0:
                        print(" no se permiten numeros negativos.")
                    else:
                        horas.append(hora)
                        break
                except ValueError:
                    print(" ingrese un número valido.")
    #guardar datos en la matriz
    matriz_recursos.append([nombre] + horas)
    print("\nDatos registrados correctamente.")

    # mostrar reporte
def mostrar_reporte():
    if len(matriz_recursos) == 0:
        print("\nNo hay recursos registrados.")
        return
    print("\n=== REPORTE SEMANAL ===")
    for recurso in matriz_recursos:
        nombre = recurso[0]
        horas = recurso[1:]

        total, clasificacion = calcular_horas(horas)
        print("\nNombre:", nombre)
        print("Horas trabajadas:", horas)
        print("Total semanal:", total)
        print("Clasificación:", clasificacion)
#menu principal
def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Registrar horas de trabajadas")
        print("2. Mostrar reporte semanal")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_recursos()
        elif opcion == "2":
            mostrar_reporte()
        elif opcion == "3":
            print("\nPrograma finalizado.")
            break
        else:
            print("\nOpción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()
