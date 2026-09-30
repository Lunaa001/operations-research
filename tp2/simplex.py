"""Implementacion educativa del simplex para maximizacion con restricciones <=."""

from __future__ import annotations

import numpy as np


def imprimir_tabla(tabla: np.ndarray, nombres: list[str], base: list[str], iteracion: int) -> None:
    print(f"\nTabla {iteracion}")
    encabezado = [*nombres, "RHS"]
    print("Base | " + " | ".join(f"{nombre:>10}" for nombre in encabezado))
    for nombre_base, fila in zip(base, tabla[:-1]):
        print(f"{nombre_base:>4} | " + " | ".join(f"{valor:10.3f}" for valor in fila))
    print("  Z  | " + " | ".join(f"{valor:10.3f}" for valor in tabla[-1]))


def simplex(c: np.ndarray, A: np.ndarray, b: np.ndarray, nombres: list[str]) -> dict[str, object]:
    filas, columnas = A.shape
    tabla = np.zeros((filas + 1, columnas + filas + 1), dtype=float)
    tabla[:filas, :columnas] = A
    tabla[:filas, columnas:columnas + filas] = np.eye(filas)
    tabla[:filas, -1] = b
    tabla[-1, :columnas] = -c
    nombres_completos = [*nombres, *(f"s{i + 1}" for i in range(filas))]
    base = [f"s{i + 1}" for i in range(filas)]
    imprimir_tabla(tabla, nombres_completos, base, 0)

    iteracion = 0
    while np.min(tabla[-1, :-1]) < -1e-9:
        columna_entrada = int(np.argmin(tabla[-1, :-1]))
        candidatos = [
            (tabla[fila, -1] / tabla[fila, columna_entrada], fila)
            for fila in range(filas)
            if tabla[fila, columna_entrada] > 1e-9
        ]
        if not candidatos:
            raise ValueError("El problema es ilimitado")
        _, fila_salida = min(candidatos)
        pivote = tabla[fila_salida, columna_entrada]
        tabla[fila_salida] /= pivote
        for fila in range(filas + 1):
            if fila != fila_salida:
                tabla[fila] -= tabla[fila, columna_entrada] * tabla[fila_salida]
        base[fila_salida] = nombres_completos[columna_entrada]
        iteracion += 1
        imprimir_tabla(tabla, nombres_completos, base, iteracion)

    valores = {nombre: 0.0 for nombre in nombres_completos}
    for fila, nombre_base in enumerate(base):
        valores[nombre_base] = tabla[fila, -1]
    solucion = np.array([valores[nombre] for nombre in nombres])
    valor_objetivo = tabla[-1, -1]
    matriz_completa = np.hstack((A, np.eye(filas)))
    costos_completos = np.concatenate((c, np.zeros(filas)))
    base_completa = [nombres_completos.index(nombre) for nombre in base]
    precios_sombra = np.linalg.solve(matriz_completa[:, base_completa].T, costos_completos[base_completa])
    costos_reducidos = c - precios_sombra @ A

    print("\nTabla final del simplex")
    print(f"Solucion: {dict(zip(nombres, np.round(solucion, 4)))}")
    print(f"Valor optimo: ${valor_objetivo:.4f}")
    print(f"Precios sombra: {dict(zip(range(1, filas + 1), np.round(precios_sombra, 4)))}")
    print(f"Costos reducidos: {dict(zip(nombres, np.round(costos_reducidos, 4)))}")
    return {"solution": solucion, "objective": valor_objetivo, "tableau": tabla, "shadow_prices": precios_sombra, "reduced_costs": costos_reducidos}
