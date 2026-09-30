"""TP1 - Problema 2: mezcla de vitaminas al minimo costo."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog


def main() -> None:
    # x1 y x2 son los frascos de P1 y P2.
    resultado = linprog(
        c=[50, 80],
        A_ub=-np.array([[4, 1], [1, 6], [4, 6]], dtype=float),
        b_ub=-np.array([4, 6, 12], dtype=float),
        bounds=[(0, None), (0, None)],
        method="highs-ds",
    )
    if not resultado.success:
        raise RuntimeError(resultado.message)
    x1, x2 = resultado.x
    print("PROBLEMA 2")
    print(f"Frascos de P1: {x1:.2f}")
    print(f"Frascos de P2: {x2:.2f}")
    print(f"Costo minimo: ${resultado.fun:.2f}")
    print(f"Vitaminas obtenidas (A, B, C): {4*x1+x2:.2f}, {x1+6*x2:.2f}, {4*x1+6*x2:.2f}")

    x = np.linspace(0, 12, 500)
    restricciones = [(4 - 4*x, "Vitamina A"), ((6 - x) / 6, "Vitamina B"), ((12 - 4*x) / 6, "Vitamina C")]
    limite = np.maximum.reduce([np.maximum(y, 0) for y, _ in restricciones])
    fig, ax = plt.subplots(figsize=(8, 6))
    for y, nombre in restricciones:
        ax.plot(x, y, label=f"{nombre}: frontera")
    ax.fill_between(x, limite, 12, alpha=0.2, label="Region factible")
    ax.scatter([x1], [x2], color="red", s=70, zorder=5, label="Optimo")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.set_xlabel("Frascos P1")
    ax.set_ylabel("Frascos P2")
    ax.set_title("Problema 2: mezcla de vitaminas")
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
