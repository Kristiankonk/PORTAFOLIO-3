
import math

# Funciones de utilidades


def mostrar_titulo(titulo: str) -> None:
    """Muestra un título formateado en consola."""
    print("\n" + "=" * 60)
    print(titulo)
    print("=" * 60)


# 1) Conversor de unidades (variables, operadores, tipos básicos)
def conversor_unidades() -> None:
    """Permite convertir unidades simples de temperatura y longitud."""
    while True:
        mostrar_titulo("Conversor de unidades")
        print("1) Celsius a Fahrenheit")
        print("2) Fahrenheit a Celsius")
        print("3) Metros a centímetros")
        print("4) Centímetros a metros")
        print("0) Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "0":
            break

        if opcion not in ("1", "2", "3", "4" ):
            print("Opción no válida. Intenta nuevamente.")
            continue

        try:
            valor = float(input("Ingresa el valor a convertir: "))
        except ValueError:
            print("Debes ingresar un número válido.")
            continue

        if opcion == "1":
            # Celsius a Fahrenheit
            resultado = (valor * 9 / 5) + 32
            print(f"{valor} °C equivalen a {resultado:.2f} °F")
        elif opcion == "2":
            # Fahrenheit a Celsius
            resultado = (valor - 32) * 5 / 9
            print(f"{valor} °F equivalen a {resultado:.2f} °C")
        elif opcion == "3":
            # Metros a centímetros
            resultado = valor * 100
            print(f"{valor} m equivalen a {resultado:.2f} cm")
        elif opcion == "4":
            # Centímetros a metros
            resultado = valor / 100
            print(f"{valor} cm equivalen a {resultado:.2f} m")

        input("\nPresiona Enter para continuar...")


# 2) Formulario en consola (tipos de datos: str, int, float, bool)
def formulario_usuario() -> None:
    """Solicita información al usuario y la almacena en variables adecuadas."""
    mostrar_titulo("Formulario de datos de usuario")

    nombre = input("Ingresa tu nombre: ")
    edad_str = input("Ingresa tu edad: ")
    estatura_str = input("Ingresa tu estatura en metros (ej: 1.75): ")
    estudiante_str = input("¿Eres estudiante? (s/n): ")

    # Conversión de tipos
    try:
        edad = int(edad_str)
    except ValueError:
        edad = 0

    try:
        estatura = float(estatura_str)
    except ValueError:
        estatura = 0.0

    estudiante = estudiante_str.lower() == "s"

    print("\nResumen de los datos ingresados:")
    print(f"Nombre: {nombre} (tipo: {type(nombre).__name__})")
    print(f"Edad: {edad} (tipo: {type(edad).__name__})")
    print(f"Estatura: {estatura} m (tipo: {type(estatura).__name__})")
    print(f"¿Es estudiante?: {estudiante} (tipo: {type(estudiante).__name__})")

    input("\nPresiona Enter para continuar...")


# 3) Condicionales: determinar si un número es positivo, negativo o cero
def analizar_numero() -> None:
    """Determina si un número es positivo, negativo o cero."""
    mostrar_titulo("Análisis de número")

    try:
        numero = float(input("Ingresa un número: "))
    except ValueError:
        print("No ingresaste un número válido.")
        input("\nPresiona Enter para continuar...")
        return

    if numero > 0:
        mensaje = "El número es positivo."
    elif numero < 0:
        mensaje = "El número es negativo."
    else:
        mensaje = "El número es cero."

    print(mensaje)
    input("\nPresiona Enter para continuar...")


# 4) Bucles for/while: tablas de multiplicar y cálculo de factorial
def generar_tablas_multiplicar() -> None:
    """Genera tablas de multiplicar usando un bucle for."""
    mostrar_titulo("Generador de tablas de multiplicar")

    try:
        numero = int(input("Ingresa el número base de la tabla: "))
    except ValueError:
        print("Debes ingresar un número entero.")
        input("\nPresiona Enter para continuar...")
        return

    try:
        limite = int(input("¿Hasta qué número quieres la tabla? "))
    except ValueError:
        print("Debes ingresar un número entero.")
        input("\nPresiona Enter para continuar...")
        return

    print(f"\nTabla de multiplicar del {numero} hasta el {limite}:")
    for i in range(1, limite + 1):
        print(f"{numero} x {i} = {numero * i}")

    input("\nPresiona Enter para continuar...")


def calcular_factorial() -> None:
    """Calcula el factorial de un número usando un bucle while."""
    mostrar_titulo("Calculadora de factorial")

    try:
        n = int(input("Ingresa un número entero no negativo: "))
    except ValueError:
        print("Debes ingresar un número entero.")
        input("\nPresiona Enter para continuar...")
        return

    if n < 0:
        print("El factorial no está definido para números negativos.")
        input("\nPresiona Enter para continuar...")
        return

    resultado = 1
    contador = 1

    while contador <= n:
        resultado *= contador
        contador += 1

    print(f"El factorial de {n} es {resultado}.")
    input("\nPresiona Enter para continuar...")


# 5) Agenda de contactos con diccionario
def agenda_contactos() -> None:
    """Sistema simple de agenda de contactos usando un diccionario."""
    contactos = {}  # nombre -> teléfono

    while True:
        mostrar_titulo("Agenda de contactos")
        print("1) Agregar contacto")
        print("2) Ver contactos")
        print("3) Buscar contacto")
        print("4) Eliminar contacto")
        print("0) Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "0":
            break

        if opcion == "1":
            nombre = input("Nombre del contacto: ").strip()
            telefono = input("Teléfono del contacto: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.")
            else:
                contactos[nombre] = telefono
                print("Contacto agregado correctamente.")

        elif opcion == "2":
            if not contactos:
                print("No hay contactos registrados.")
            else:
                print("\nContactos registrados:")
                for nombre, telefono in contactos.items():
                    print(f"- {nombre}: {telefono}")

        elif opcion == "3":
            nombre = input("Ingresa el nombre a buscar: ").strip()
            if nombre in contactos:
                print(f"{nombre}: {contactos[nombre]}")
            else:
                print("Contacto no encontrado.")

        elif opcion == "4":
            nombre = input("Ingresa el nombre del contacto a eliminar: ").strip()
            if nombre in contactos:
                del contactos[nombre]
                print("Contacto eliminado.")
            else:
                print("No se encontró un contacto con ese nombre.")

        else:
            print("Opción no válida. Intenta nuevamente.")

        input("\nPresiona Enter para continuar...")


# 6) Cálculo de áreas usando funciones
def area_circulo(radio: float) -> float:
    """Calcula el área de un círculo."""
    return math.pi * radio ** 2


def area_rectangulo(base: float, altura: float) -> float:
    """Calcula el área de un rectángulo."""
    return base * altura


def area_triangulo(base: float, altura: float) -> float:
    """Calcula el área de un triángulo."""
    return (base * altura) / 2


def calculadora_areas() -> None:
    """Permite calcular el área de distintas figuras geométricas."""
    while True:
        mostrar_titulo("Calculadora de áreas geométricas")
        print("1) Círculo")
        print("2) Rectángulo")
        print("3) Triángulo")
        print("0) Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "0":
            break

        try:
            if opcion == "1":
                radio = float(input("Ingresa el radio del círculo: "))
                resultado = area_circulo(radio)
                print(f"El área del círculo es {resultado:.2f}.")
            elif opcion == "2":
                base = float(input("Ingresa la base del rectángulo: "))
                altura = float(input("Ingresa la altura del rectángulo: "))
                resultado = area_rectangulo(base, altura)
                print(f"El área del rectángulo es {resultado:.2f}.")
            elif opcion == "3":
                base = float(input("Ingresa la base del triángulo: "))
                altura = float(input("Ingresa la altura del triángulo: "))
                resultado = area_triangulo(base, altura)
                print(f"El área del triángulo es {resultado:.2f}.")
            else:
                print("Opción no válida.")
        except ValueError:
            print("Debes ingresar valores numéricos válidos.")

        input("\nPresiona Enter para continuar...")



# Menú principal


def mostrar_menu() -> None:
    print("\n" + "-" * 60)
    print("MENÚ PRINCIPAL - PROYECTO PYTHON PORTAFOLIO")
    print("-" * 60)
    print("1) Conversor de unidades")
    print("2) Formulario de usuario (tipos de datos)")
    print("3) Analizar número (positivo, negativo o cero)")
    print("4) Generar tabla de multiplicar")
    print("5) Calcular factorial")
    print("6) Agenda de contactos (diccionario)")
    print("7) Calculadora de áreas (funciones)")
    print("0) Salir")


def main() -> None:
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ").strip()

        if opcion == "0":
            print("\nGracias por utilizar el programa. ¡Hasta luego!")
            break
        elif opcion == "1":
            conversor_unidades()
        elif opcion == "2":
            formulario_usuario()
        elif opcion == "3":
            analizar_numero()
        elif opcion == "4":
            generar_tablas_multiplicar()
        elif opcion == "5":
            calcular_factorial()
        elif opcion == "6":
            agenda_contactos()
        elif opcion == "7":
            calculadora_areas()
        else:
            print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    main()
