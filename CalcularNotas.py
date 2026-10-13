
#Primer programa Mell

def ingresar_calificaciones():
    asignaturas = []
    notas = []

    while True:
        nombre = input("\nIngresa la materia (Enter para terminar): ").strip()

        if nombre == "":
            break

        while True:
            try:
                nota = float(input("Ingresa la nota de 0 a 10: "))

                if 0 <= nota <= 10:
                    break
                else:
                    print("La nota debe estar entre 0 y 10.")

            except ValueError:
                print("Debes ingresar un número. Ejemplo: 7.5.")

        asignaturas.append(nombre)
        notas.append(nota)

        respuesta = input("¿Quieres agregar otra materia? (s/n): ").strip().lower()

        while respuesta not in ("s", "n"):
            respuesta = input("Escribe s o n: ").strip().lower()

        if respuesta == "n":
            break

    return asignaturas, notas

#--------------------------------------------------------------

def calcular_promedio(calificaciones):
    if not calificaciones:
        return None

    suma = sum(calificaciones)
    cantidad = len(calificaciones)
    return suma / cantidad

#----------------------------------------------------------------

def determinar_estado(calificaciones, umbral=5.0):
    aprobadas = []
    reprobadas = []

    for posicion in range(len(calificaciones)):
        if calificaciones[posicion] >= umbral:
            aprobadas.append(posicion)
        else:
            reprobadas.append(posicion)

    return aprobadas, reprobadas

#----------------------------------------------------------------

def encontrar_extremos(calificaciones):
    if not calificaciones:
        return None, None

    mayor = 0
    menor = 0

    for posicion in range(len(calificaciones)):
        if calificaciones[posicion] > calificaciones[mayor]:
            mayor = posicion

        if calificaciones[posicion] < calificaciones[menor]:
            menor = posicion

    return mayor, menor

#----------------------------------------------------------------

def main():
    print("CALCULADORA DE PROMEDIOS ESCOLARES")

    asignaturas, notas = ingresar_calificaciones()

    if not notas:
        print("\nNo se ingresaron materias.")
    else:
        promedio = calcular_promedio(notas)
        aprobadas, reprobadas = determinar_estado(notas)
        mayor, menor = encontrar_extremos(notas)

        print("\n----- RESUMEN -----")

        for posicion in range(len(asignaturas)):
            print(f"{asignaturas[posicion]}: {notas[posicion]:.2f}")

        print(f"\nPromedio general: {promedio:.2f}")

        print("\nMaterias aprobadas:")
        if aprobadas:
            for posicion in aprobadas:
                print(f"- {asignaturas[posicion]}: {notas[posicion]:.2f}")
        else:
            print("Ninguna.")

        print("\nMaterias reprobadas:")
        if reprobadas:
            for posicion in reprobadas:
                print(f"- {asignaturas[posicion]}: {notas[posicion]:.2f}")
        else:
            print("Ninguna.")

        print(f"\nMejor nota: {asignaturas[mayor]} ({notas[mayor]:.2f})")
        print(f"Peor nota: {asignaturas[menor]} ({notas[menor]:.2f})")

    print("\nGracias por usar el programa. ¡Hasta pronto!")


if __name__ == "__main__":
    main()