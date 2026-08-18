import pandas as pd
import numpy as np

# ============================================================
# PARTE 1: Diccionario crudo con listas paralelas
# ------------------------------------------------------------
# Cada clave es un atributo (una futura columna) y cada valor es
# una lista con un dato por objeto, en el MISMO ORDEN que la
# lista "objeto". np.nan se usa cuando no se relevo ese dato
# para ese objeto en particular.
# ============================================================
datos_objetos = {
    "objeto_id": [0, 1, 2, 3, 4, 5, 6, 7, 8],
    "objeto": [
        "cubo rubik", "peluche", "hexagono", "libro", "cable",
        "lapicera", "caja plastica", "tapa plastico", "lentes",
    ],
    "forma": [
        "cuadrado", np.nan, "hexagonal", "rectangular", "cilindrico",
        "cilindrico", np.nan, "cilindrico", np.nan,
    ],
    "textura": [
        "liso", "liso", "liso", "liso", np.nan,
        np.nan, np.nan, np.nan, "liso",
    ],
    "rigidez": [
        np.nan, "blando", "rigido", np.nan, "rigido",
        "rigido", "blando", "rigido", np.nan,
    ],
    "movimiento": [True, False, False, False, False, False, False, False, False],
    "movil": [False, False, False, False, False, False, True, False, False],
    "ruidoso": [False, False, False, False, False, False, True, False, False],
    "elastico": [False, False, False, False, False, False, False, False, True],
}

# ============================================================
# PARTE 2: Transformacion a DataFrame
# ------------------------------------------------------------
# pd.DataFrame junta todas las listas del diccionario en una
# tabla: cada clave del diccionario pasa a ser una columna, y
# cada posicion de las listas pasa a ser una fila (un objeto).
# ============================================================
df_objetos = pd.DataFrame(datos_objetos)

# ============================================================
# PARTE 3: Convertir tipos categoricos y ordinales
# ------------------------------------------------------------
# "forma" y "textura" son categorias SIN orden entre si.
# "rigidez" es ordinal: blando < medio < rigido (por eso se usa
# pd.Categorical con "categories" en ese orden y ordered=True,
# lo que permite despues comparar con < y > entre objetos).
# ============================================================
df_objetos["forma"] = df_objetos["forma"].astype("category")
df_objetos["textura"] = df_objetos["textura"].astype("category")
df_objetos["rigidez"] = pd.Categorical(
    df_objetos["rigidez"],
    categories=["blando", "medio", "rigido"],
    ordered=True,
)

# ============================================================
# PARTE 4: Mostrar resultados
# ------------------------------------------------------------
# Solo se ejecuta si corres este archivo directamente.
# ============================================================
if __name__ == "__main__":
    print(df_objetos)
    print("\nTipos de dato por columna:")
    print(df_objetos.dtypes)
