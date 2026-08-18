# Cada objeto con sus caracteristicas (variables).
objetos = {
    "cubo rubik": ["movimiento", "cuadrado", "liso"],
    "peluche": ["liso", "blando"],
    "hexagono": ["liso", "duro"],
    "cable": ["cilindrico", "rigido"],
    "lapicera": ["cilindrico", "rigido"],
    "caja plastica": ["blando", "movil", "ruidoso"],
    "tapa plastico": ["rigido", "cilindrico"],
    "lentes": ["plastico", "liso", "elastico"],
}

# Lista de variables (columnas), en orden de aparicion, sin repetir.
variables = list(dict.fromkeys(v for caracteristicas in objetos.values() for v in caracteristicas))

# Tabla: para cada objeto, 1 si tiene la variable, 0 si no.
tabla = {
    objeto: {variable: (1 if variable in caracteristicas else 0) for variable in variables}
    for objeto, caracteristicas in objetos.items()
}

if __name__ == "__main__":
    ancho_objeto = max(len(o) for o in objetos)
    encabezado = f"{'objeto':<{ancho_objeto}} | " + " | ".join(variables)
    print(encabezado)
    print("-" * len(encabezado))
    for objeto, fila in tabla.items():
        valores = " | ".join(str(fila[v]).rjust(len(v)) for v in variables)
        print(f"{objeto:<{ancho_objeto}} | {valores}")
