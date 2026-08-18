# ============================================================
# PARTE 1: Diccionario de items
# ------------------------------------------------------------
# Cada item de la lista original se guarda como clave de un
# diccionario, con un numero de indice como valor. Sirve para
# tener un identificador unico por objeto (0, 1, 2, ...).
# ============================================================
items = [
    "cubo rubik",
    "peluche",
    "hexagono",
    "libro",
    "cable",
    "lapicera",
    "caja plastica",
    "tapa plastico",
    "lentes",
]

diccionario_items = {item: indice for indice, item in enumerate(items)}


# ============================================================
# PARTE 2: Caracteristicas por item
# ------------------------------------------------------------
# Diccionario donde cada item tiene asociada una lista con sus
# caracteristicas (las variables que describiste: forma,
# textura, dureza, etc). Esta es la fuente de datos que despues
# se usa para armar la tabla de la Parte 3.
# ============================================================
caracteristicas_por_item = {
    "cubo rubik": ["movimiento", "cuadrado", "liso"],
    "peluche": ["liso", "blando"],
    "hexagono": ["liso", "duro"],
    "libro": ["liso", "rectangular"],
    "cable": ["cilindrico", "rigido"],
    "lapicera": ["cilindrico", "rigido"],
    "caja plastica": ["blando", "movil", "ruidoso"],
    "tapa plastico": ["rigido", "cilindrico"],
    "lentes": ["plastico", "liso", "elastico"],
}


# ============================================================
# PARTE 3: Tabla de codificacion 1/0
# ------------------------------------------------------------
# 3.1) Se junta la lista de todas las variables (columnas) sin
#      repetirlas, respetando el orden en el que aparecen.
# 3.2) Se arma "tabla": un diccionario de diccionarios donde
#      tabla[item][variable] vale 1 si ese item tiene esa
#      caracteristica, y 0 si no la tiene.
# ============================================================
variables = list(
    dict.fromkeys(
        variable
        for lista_caracteristicas in caracteristicas_por_item.values()
        for variable in lista_caracteristicas
    )
)

tabla = {
    item: {
        variable: (1 if variable in lista_caracteristicas else 0)
        for variable in variables
    }
    for item, lista_caracteristicas in caracteristicas_por_item.items()
}


# ============================================================
# PARTE 4: Mostrar los resultados
# ------------------------------------------------------------
# Solo se ejecuta si corres este archivo directamente (no si lo
# importas desde otro script). Imprime primero el diccionario
# de items con su indice, y despues la tabla de 1/0 en formato
# de columnas alineadas.
# ============================================================
if __name__ == "__main__":
    print("Diccionario de items (item: indice)")
    for item, indice in diccionario_items.items():
        print(f"  {item}: {indice}")

    print("\nTabla de caracteristicas (1 = tiene, 0 = no tiene)")
    ancho_item = max(len(item) for item in caracteristicas_por_item)
    encabezado = f"{'item':<{ancho_item}} | " + " | ".join(variables)
    print(encabezado)
    print("-" * len(encabezado))
    for item, fila in tabla.items():
        valores = " | ".join(str(fila[variable]).rjust(len(variable)) for variable in variables)
        print(f"{item:<{ancho_item}} | {valores}")
