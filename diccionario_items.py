items = [
    "cubo rubik",
    "peluche",
    "hexagono",
    "libro",
    "cable",
    "lapicera",
    "caja plastico blando",
    "tapa plastico",
    "lentes",
]

diccionario_items = {indice: item for indice, item in enumerate(items)}

if __name__ == "__main__":
    for indice, item in diccionario_items.items():
        print(f"{indice}: {item}")
