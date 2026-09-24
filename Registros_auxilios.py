import json
import os
from datetime import datetime

# ============================================================
# REGISTRO DE AUXILIOS DE SEGURIDAD CIUDADANA
# Proyecto desarrollado en Python
# ============================================================

ARCHIVO_DATOS = "datos.json"

USUARIO = "policia"
CONTRASENA = "1234"


# ============================================================
# LISTA DE MOTIVOS DE ATENCIÓN
# ============================================================
# Los nombres se mantienen como categorías del ejercicio.
# Si tu fotografía contiene una denominación diferente,
# reemplaza únicamente esta lista por la transcripción exacta.

MOTIVOS = [
    "Abandono de persona",
    "Delitos sexuales",
    "Actos inmorales",
    "Agresión a la autoridad",
    "Agresiones a personas",
    "Amenaza de bomba",
    "Apoyo aduana",
    "Boleta / orden de autoridad",
    "Capturado por civiles",
    "Manejo de material pirotécnico",
    "Constatar persona sin vida",
    "Daño a propiedad pública o privada",
    "Delito hidrocarburos",
    "Desalojos",
    "Desaparición de persona",
    "Escándalo",
    "Fraude a persona",
    "Eventos ilegales",
    "Diversas formas de explotación",
    "Falsificación de documentos",
    "Falso funcionario",
    "Fuga detenidos",
    "Maltrato a animales",
    "Manifestaciones",
    "Moneda falsa",
    "Persona armada",
    "Presencia policial",
    "Otro"
]


# ============================================================
# DATOS INICIALES FICTICIOS
# ============================================================

REGISTROS_INICIALES = [
    {
        "codigo": "AT001",
        "alertante": "Carlos Mendoza Ruiz",
        "motivo": "Escándalo",
        "fecha_hora": "05/09/2026 - 08:15:20",
        "lugar": "Barrio Los Almendros"
    },
    {
        "codigo": "AT002",
        "alertante": "María Fernanda López",
        "motivo": "Agresiones a personas",
        "fecha_hora": "05/09/2026 - 09:40:12",
        "lugar": "Avenida Principal"
    },
    {
        "codigo": "AT003",
        "alertante": "Jorge Andrés Castillo",
        "motivo": "Daño a propiedad pública o privada",
        "fecha_hora": "05/09/2026 - 10:25:45",
        "lugar": "Sector El Mirador"
    },
    {
        "codigo": "AT004",
        "alertante": "Ana Patricia Torres",
        "motivo": "Presencia policial",
        "fecha_hora": "05/09/2026 - 11:10:30",
        "lugar": "Parque Central"
    },
    {
        "codigo": "AT005",
        "alertante": "Luis Alberto Zambrano",
        "motivo": "Persona armada",
        "fecha_hora": "05/09/2026 - 12:05:18",
        "lugar": "Calle Los Ceibos"
    },
    {
        "codigo": "AT006",
        "alertante": "Daniela Sofía Vera",
        "motivo": "Maltrato a animales",
        "fecha_hora": "05/09/2026 - 13:30:42",
        "lugar": "Urbanización Las Palmas"
    },
    {
        "codigo": "AT007",
        "alertante": "Miguel Ángel Paredes",
        "motivo": "Falso funcionario",
        "fecha_hora": "05/09/2026 - 14:20:10",
        "lugar": "Mercado Municipal"
    },
    {
        "codigo": "AT008",
        "alertante": "Sofía Valentina Cruz",
        "motivo": "Fraude a persona",
        "fecha_hora": "05/09/2026 - 15:45:27",
        "lugar": "Sector Las Flores"
    },
    {
        "codigo": "AT009",
        "alertante": "Roberto Javier Molina",
        "motivo": "Desaparición de persona",
        "fecha_hora": "05/09/2026 - 16:15:55",
        "lugar": "Barrio San José"
    },
    {
        "codigo": "AT010",
        "alertante": "Gabriela Isabel Cedeño",
        "motivo": "Desalojos",
        "fecha_hora": "05/09/2026 - 17:05:33",
        "lugar": "Calle 10 de Agosto"
    },
    {
        "codigo": "AT011",
        "alertante": "Fernando Esteban Reyes",
        "motivo": "Eventos ilegales",
        "fecha_hora": "05/09/2026 - 18:20:14",
        "lugar": "Sector La Esperanza"
    },
    {
        "codigo": "AT012",
        "alertante": "Valeria Nicole Ortiz",
        "motivo": "Amenaza de bomba",
        "fecha_hora": "05/09/2026 - 19:10:05",
        "lugar": "Zona Comercial"
    },
    {
        "codigo": "AT013",
        "alertante": "Pedro Xavier Andrade",
        "motivo": "Boleta / orden de autoridad",
        "fecha_hora": "05/09/2026 - 20:35:41",
        "lugar": "Sector Los Laureles"
    },
    {
        "codigo": "AT014",
        "alertante": "Camila Alejandra Ruiz",
        "motivo": "Actos inmorales",
        "fecha_hora": "05/09/2026 - 21:15:29",
        "lugar": "Parque La Unión"
    },
    {
        "codigo": "AT015",
        "alertante": "José Miguel Herrera",
        "motivo": "Apoyo aduana",
        "fecha_hora": "05/09/2026 - 22:05:16",
        "lugar": "Sector Industrial"
    }
]


# ============================================================
# FUNCIONES PARA GUARDAR Y CARGAR DATOS
# ============================================================

def guardar_datos(registros):
    """Guarda todos los registros en el archivo datos.json."""
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
            json.dump(registros, archivo, ensure_ascii=False, indent=4)

    except Exception as error:
        print(f"\nError al guardar los datos: {error}")


def cargar_datos():
    """
    Carga los registros desde datos.json.
    Si el archivo no existe, crea los 15 registros iniciales.
    """

    if not os.path.exists(ARCHIVO_DATOS):
        registros = REGISTROS_INICIALES.copy()
        guardar_datos(registros)
        return registros

    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            registros = json.load(archivo)

        return registros

    except (json.JSONDecodeError, OSError):
        print("\nNo se pudo leer datos.json.")
        print("Se crearán nuevamente los registros iniciales.")

        registros = REGISTROS_INICIALES.copy()
        guardar_datos(registros)

        return registros


# ============================================================
# FUNCIONES DE APOYO
# ============================================================

def mostrar_separador():
    print("\n" + "=" * 65)


def mostrar_encabezado():
    mostrar_separador()
    print("      REGISTRO DE AUXILIOS DE SEGURIDAD CIUDADANA")
    mostrar_separador()


def mostrar_registro(registro):
    """Muestra un registro como ficha individual."""

    print("-" * 65)
    print(f"Código de atención : {registro['codigo']}")
    print(f"Nombre del alertante: {registro['alertante']}")
    print(f"Motivo de atención : {registro['motivo']}")
    print(f"Fecha y hora       : {registro['fecha_hora']}")
    print(f"Lugar de atención  : {registro['lugar']}")
    print("-" * 65)


def mostrar_motivos():
    """Muestra la lista de motivos disponibles."""

    print("\nLISTA DE MOTIVOS DE ATENCIÓN")
    print("-" * 65)

    for i, motivo in enumerate(MOTIVOS, start=1):
        print(f"{i:2}. {motivo}")

    print("-" * 65)


def seleccionar_motivo():
    """
    Permite seleccionar un motivo de la lista.
    Devuelve el nombre del motivo seleccionado.
    """

    while True:
        mostrar_motivos()

        opcion = input("Seleccione el número del motivo: ").strip()

        if opcion.isdigit():
            numero = int(opcion)

            if 1 <= numero <= len(MOTIVOS):
                return MOTIVOS[numero - 1]

        print("\nOpción inválida. Seleccione un número de la lista.")


def generar_codigo(registros):
    """
    Genera automáticamente el siguiente código de atención.

    Ejemplo:
    AT001
    AT002
    AT003
    """

    mayor = 0

    for registro in registros:
        codigo = registro.get("codigo", "")

        if codigo.startswith("AT"):
            parte_numerica = codigo[2:]

            if parte_numerica.isdigit():
                numero = int(parte_numerica)

                if numero > mayor:
                    mayor = numero

    return f"AT{mayor + 1:03d}"


def buscar_registro_por_codigo(registros, codigo):
    """Busca un registro utilizando su código."""

    codigo = codigo.upper().strip()

    for registro in registros:
        if registro["codigo"].upper() == codigo:
            return registro

    return None


# ============================================================
# LOGIN
# ============================================================

def iniciar_sesion():
    """Controla el acceso al programa."""

    print("=" * 65)
    print("       SISTEMA DE REGISTRO DE AUXILIOS")
    print("              INICIO DE SESIÓN")
    print("=" * 65)

    intentos = 0

    while intentos < 3:
        usuario = input("\nUsuario: ").strip()
        contrasena = input("Contraseña: ").strip()

        if usuario == USUARIO and contrasena == CONTRASENA:
            print("\nAcceso autorizado.")
            return True

        intentos += 1
        restantes = 3 - intentos

        if restantes > 0:
            print("\nUsuario o contraseña incorrectos.")
            print(f"Intentos restantes: {restantes}")
        else:
            print("\nSe alcanzó el máximo de intentos.")
            print("El programa se cerrará.")

    return False


# ============================================================
# OPCIÓN 1: REGISTRAR PERSONA ATENDIDA
# ============================================================

def registrar_auxilio(registros):
    """Registra un nuevo auxilio."""

    mostrar_separador()
    print("          REGISTRAR PERSONA ATENDIDA")
    mostrar_separador()

    codigo = generar_codigo(registros)

    print(f"\nCódigo generado automáticamente: {codigo}")

    # Solicitar nombre del alertante
    while True:
        alertante = input("Nombre del alertante: ").strip()

        if alertante:
            break

        print("El nombre del alertante no puede quedar vacío.")

    # Seleccionar motivo
    motivo = seleccionar_motivo()

    # Fecha y hora automática del sistema
    fecha_hora = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")

    # Solicitar lugar
    while True:
        lugar = input("Lugar de atención: ").strip()

        if lugar:
            break

        print("El lugar de atención no puede quedar vacío.")

    # Crear el diccionario del nuevo registro
    nuevo_registro = {
        "codigo": codigo,
        "alertante": alertante,
        "motivo": motivo,
        "fecha_hora": fecha_hora,
        "lugar": lugar
    }

    # Mostrar resumen antes de guardar
    print("\nRESUMEN DEL NUEVO REGISTRO")
    mostrar_registro(nuevo_registro)

    confirmacion = input("¿Desea guardar este registro? (S/N): ").strip().upper()

    if confirmacion == "S":
        registros.append(nuevo_registro)
        guardar_datos(registros)

        print("\nRegistro guardado correctamente.")

    else:
        print("\nEl registro no fue guardado.")


# ============================================================
# OPCIÓN 2: MOSTRAR TODOS LOS REGISTROS
# ============================================================

def mostrar_todos(registros):
    """Muestra todos los registros como fichas individuales."""

    mostrar_separador()
    print("              TODOS LOS REGISTROS")
    mostrar_separador()

    if not registros:
        print("\nNo existen registros actualmente.")
        return

    print(f"\nTotal de registros: {len(registros)}\n")

    for registro in registros:
        mostrar_registro(registro)


# ============================================================
# OPCIÓN 3: BUSCAR POR CÓDIGO
# ============================================================

def buscar_por_codigo(registros):
    """Busca y muestra un registro mediante su código."""

    mostrar_separador()
    print("                BUSCAR POR CÓDIGO")
    mostrar_separador()

    codigo = input("\nIngrese el código de atención: ").strip()

    registro = buscar_registro_por_codigo(registros, codigo)

    if registro:
        print("\nRegistro encontrado:")
        mostrar_registro(registro)
    else:
        print(f"\nNo se encontró ningún registro con el código {codigo.upper()}.")

    input("\nPresione ENTER para regresar al menú principal...")


# ============================================================
# OPCIÓN 4: BUSCAR POR LUGAR
# ============================================================

def buscar_por_lugar(registros):
    """Busca registros cuyo lugar coincida con la búsqueda."""

    mostrar_separador()
    print("                 BUSCAR POR LUGAR")
    mostrar_separador()

    lugar_buscado = input("\nIngrese el lugar a buscar: ").strip().lower()

    if not lugar_buscado:
        print("\nDebe ingresar un lugar.")
        return

    encontrados = []

    for registro in registros:
        lugar = registro["lugar"].lower()

        if lugar_buscado in lugar:
            encontrados.append(registro)

    if encontrados:
        print(f"\nCantidad de registros encontrados: {len(encontrados)}")

        for registro in encontrados:
            mostrar_registro(registro)

    else:
        print("\nNo se encontraron registros para ese lugar.")

    input("\nPresione ENTER para regresar al menú principal...")


# ============================================================
# OPCIÓN 5: ELIMINAR REGISTRO
# ============================================================

def eliminar_registro(registros):
    """Elimina un registro después de pedir confirmación."""

    mostrar_separador()
    print("                 ELIMINAR REGISTRO")
    mostrar_separador()

    codigo = input("\nIngrese el código del registro: ").strip()

    registro = buscar_registro_por_codigo(registros, codigo)

    if not registro:
        print(f"\nNo se encontró ningún registro con el código {codigo.upper()}.")
        input("\nPresione ENTER para continuar...")
        return

    print("\nRegistro que será eliminado:")
    mostrar_registro(registro)

    confirmacion = input(
        "¿Está seguro de eliminar este registro? (S/N): "
    ).strip().upper()

    if confirmacion == "S":
        registros.remove(registro)
        guardar_datos(registros)

        print("\nRegistro eliminado correctamente.")

    else:
        print("\nEl registro no fue eliminado.")

    input("\nPresione ENTER para continuar...")


# ============================================================
# OPCIÓN 7: MODIFICAR MOTIVO
# ============================================================

def modificar_motivo(registros):
    """Permite modificar únicamente el motivo de un registro."""

    mostrar_separador()
    print("                 MODIFICAR MOTIVO")
    mostrar_separador()

    codigo = input("\nIngrese el código de atención: ").strip()

    registro = buscar_registro_por_codigo(registros, codigo)

    if not registro:
        print(f"\nNo se encontró ningún registro con el código {codigo.upper()}.")
        input("\nPresione ENTER para continuar...")
        return

    print("\nREGISTRO ACTUAL")
    mostrar_registro(registro)

    print(f"\nMotivo actual: {registro['motivo']}")

    nuevo_motivo = seleccionar_motivo()

    print("\nNUEVO REGISTRO")
    registro_temporal = registro.copy()
    registro_temporal["motivo"] = nuevo_motivo

    mostrar_registro(registro_temporal)

    confirmacion = input(
        "¿Desea confirmar el cambio de motivo? (S/N): "
    ).strip().upper()

    if confirmacion == "S":
        registro["motivo"] = nuevo_motivo
        guardar_datos(registros)

        print("\nMotivo modificado correctamente.")

    else:
        print("\nNo se realizaron cambios.")

    input("\nPresione ENTER para continuar...")


# ============================================================
# OPCIÓN 8: ESTADÍSTICAS
# ============================================================

def mostrar_estadisticas(registros):
    """Muestra estadísticas dinámicas de los registros."""

    mostrar_separador()
    print("                    ESTADÍSTICAS")
    mostrar_separador()

    total = len(registros)

    print(f"\nTotal de auxilios registrados: {total}")

    if total == 0:
        print("\nNo existen datos para generar estadísticas.")
        input("\nPresione ENTER para continuar...")
        return

    # ----------------------------------------
    # Contar registros por motivo
    # ----------------------------------------

    conteo_motivos = {}

    for registro in registros:
        motivo = registro["motivo"]

        if motivo not in conteo_motivos:
            conteo_motivos[motivo] = 0

        conteo_motivos[motivo] += 1

    print("\n--- AUXILIOS POR MOTIVO ---")

    for motivo, cantidad in sorted(conteo_motivos.items()):
        print(f"{motivo}: {cantidad}")

    # ----------------------------------------
    # Contar registros por lugar
    # ----------------------------------------

    conteo_lugares = {}

    for registro in registros:
        lugar = registro["lugar"]

        if lugar not in conteo_lugares:
            conteo_lugares[lugar] = 0

        conteo_lugares[lugar] += 1

    print("\n--- AUXILIOS POR LUGAR ---")

    for lugar, cantidad in sorted(conteo_lugares.items()):
        print(f"{lugar}: {cantidad}")

    # ----------------------------------------
    # Motivo con mayor cantidad de registros
    # ----------------------------------------

    motivo_mayor = max(conteo_motivos, key=conteo_motivos.get)

    print("\n--- RESUMEN ---")
    print(f"Motivo con mayor cantidad de registros: {motivo_mayor}")
    print(f"Cantidad: {conteo_motivos[motivo_mayor]}")

    input("\nPresione ENTER para continuar...")


# ============================================================
# MENÚ PRINCIPAL
# ============================================================

def mostrar_menu():
    """Muestra las opciones principales del sistema."""

    mostrar_separador()
    print("                   MENÚ PRINCIPAL")
    mostrar_separador()

    print("1. Registrar persona atendida")
    print("2. Mostrar todos los registros")
    print("3. Buscar por código")
    print("4. Buscar por lugar")
    print("5. Eliminar registro")
    print("6. Salir")
    print("7. Modificar motivo")
    print("8. Estadísticas")

    mostrar_separador()


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():
    """Función principal que ejecuta el sistema."""

    if not iniciar_sesion():
        return

    # Cargar registros desde datos.json
    registros = cargar_datos()

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción (1-8): ").strip()

        if opcion == "1":
            registrar_auxilio(registros)

        elif opcion == "2":
            mostrar_todos(registros)

            input("\nPresione ENTER para regresar al menú principal...")

        elif opcion == "3":
            buscar_por_codigo(registros)

        elif opcion == "4":
            buscar_por_lugar(registros)

        elif opcion == "5":
            eliminar_registro(registros)

        elif opcion == "6":
            print("\nSesión finalizada.")
            print(
                "Gracias por utilizar el Registro de Auxilios "
                "de Seguridad Ciudadana."
            )
            break

        elif opcion == "7":
            modificar_motivo(registros)

        elif opcion == "8":
            mostrar_estadisticas(registros)

        else:
            print("\nOpción inválida. Seleccione una opción del 1 al 8.")


# ============================================================
# INICIO DEL PROGRAMA
# ============================================================

if __name__ == "__main__":
    main()