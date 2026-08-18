# Cada item mapeado a una descripcion/categoria (material u origen).
# Ajusta los valores segun lo que necesites.
diccionario_items = {
    "cubo rubik": "plastico rigido",
    "peluche": "tela con relleno blando",
    "hexagono": "plastico rigido",
    "libro": "papel/carton",
    "cable": "plastico y metal flexible",
    "lapicera": "plastico rigido",
    "caja plastico blando": "plastico blando",
    "tapa plastico": "plastico rigido",
    "lentes": "plastico/vidrio rigido",
}

if __name__ == "__main__":
    for item, descripcion in diccionario_items.items():
        print(f"{item}: {descripcion}")
