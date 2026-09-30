"""TP1 - Problema 3: mezcla de fertilizantes."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog


def main() -> None:
    resultado = linprog(
        c=-np.array([40, 50, 60], dtype=float),
        A_ub=np.array([[4, 4, 5], [200, 300, 300], [600, 400, 500]], dtype=float),
        b_ub=[80, 6000, 5000],
        bounds=[(0, None)] * 3,
        method="highs-ds",
    )
    if not resultado.success:
        raise RuntimeError(resultado.message)
    a, b, c = resultado.x
    print("PROBLEMA 3")
    print(f"Sulfato A: {a:.2f} toneladas")
    print(f"Nitrato B: {b:.2f} toneladas")
    print(f"Urea C: {c:.2f} toneladas")
    print(f"Utilidad maxima: ${-resultado.fun:.2f}")
    print("Uso de recursos:", np.round(np.array([[4, 4, 5], [200, 300, 300], [600, 400, 500]]) @ resultado.x, 2))

    # Como hay tres variables, la visualizacion es una proyeccion 3D de puntos factibles.
    rng = np.random.default_rng(1)
    puntos = rng.uniform(0, [20, 20, 20], size=(100000, 3))
    recursos = puntos @ np.array([[4, 200, 600], [4, 300, 400], [5, 300, 500]])
    factibles = puntos[(recursos[:, 0] <= 80) & (recursos[:, 1] <= 6000) & (recursos[:, 2] <= 5000)]
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(factibles[:, 0], factibles[:, 1], factibles[:, 2], s=2, alpha=0.15, label="Factibles")
    ax.scatter([a], [b], [c], color="red", s=90, label="Optimo")
    ax.set_xlabel("A: sulfato")
    ax.set_ylabel("B: nitrato")
    ax.set_zlabel("C: urea")
    ax.set_title("Problema 3: region factible 3D")
    ax.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
