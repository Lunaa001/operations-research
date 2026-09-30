"""Utilidades para resolver modelos pequenos de programacion entera."""

from itertools import product
from typing import Callable


def resolver_entera(
    nombres: list[str],
    maximos: list[int],
    objetivo: Callable[[tuple[int, ...]], float],
    factible: Callable[[tuple[int, ...]], bool],
) -> tuple[tuple[int, ...], float, list[tuple[tuple[int, ...], float]]]:
    evaluadas = []
    for candidato in product(*(range(maximo + 1) for maximo in maximos)):
        if factible(candidato):
            evaluadas.append((candidato, objetivo(candidato)))
    if not evaluadas:
        raise ValueError("El modelo no tiene soluciones factibles")
    optimo, valor = max(evaluadas, key=lambda item: item[1])
    print("Soluciones enteras factibles evaluadas:", len(evaluadas))
    print("Variables:", dict(zip(nombres, optimo)))
    print(f"Valor optimo: ${valor:.2f}")
    return optimo, valor, evaluadas
