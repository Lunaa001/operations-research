"""TP1 - Problema 1: produccion de dos productos."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog


def main() -> None:
    # x1 y x2 son las cantidades de los productos 1 y 2.
    utilidad = np.array([15, 18], dtype=float)
    consumo = np.array([[4, 2], [2, 6], [20, 28]], dtype=float)
    capacidad = np.array([2000, 2400, 14000], dtype=float)

    resultado = linprog(
        c=-utilidad,
        A_ub=consumo,
        b_ub=capacidad,
        bounds=[(0, None), (0, None)],
        method="highs-ds",
    )

    if not resultado.success:
        raise RuntimeError(resultado.message)

    x1, x2 = resultado.x
    print("PROBLEMA 1")
    print(f"Producto 1: {x1:.2f} unidades")
    print(f"Producto 2: {x2:.2f} unidades")
    print(f"Utilidad maxima: ${-resultado.fun:.2f}")
    print("Uso de recursos:")
    for nombre, usado, limite in zip(("A", "B", "C"), consumo @ resultado.x, capacidad):
        print(f"  Departamento {nombre}: {usado:.2f} / {limite:.2f}")

    x = np.linspace(0, 1000, 500)
    limites = {
        "A": (2000 - 4 * x) / 2,
        "B": (2400 - 2 * x) / 6,
        "C": (14000 - 20 * x) / 28,
    }
    fig, ax = plt.subplots(figsize=(8, 6))
    for nombre, y in limites.items():
        ax.plot(x, y, label=f"Departamento {nombre}")
    ax.fill_between(x, 0, np.minimum.reduce(list(limites.values())), where=np.minimum.reduce(list(limites.values())) >= 0, alpha=0.2)
    ax.scatter([x1], [x2], color="red", s=70, zorder=5, label="Optimo")
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 1000)
    ax.set_xlabel("Producto 1 (x1)")
    ax.set_ylabel("Producto 2 (x2)")
    ax.set_title("Problema 1: region factible y solucion optima")
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
