"""TP2 - Problema 3: análisis de sensibilidad con simplex."""

import numpy as np
import matplotlib.pyplot as plt
from simplex import simplex


def main() -> None:
    A = np.array([[4, 4, 5], [200, 300, 300], [600, 400, 500]], dtype=float)
    b = np.array([80, 6000, 5000], dtype=float)
    resultado = simplex(np.array([40, 50, 60], dtype=float), A, b, ["A", "B", "C"])
    cantidades = resultado["solution"]
    uso = A @ cantidades
    print("\nAnalisis solicitado:")
    for i, (usado, disponible, precio) in enumerate(zip(uso, b, resultado["shadow_prices"]), 1):
        estado = "escaso (activo)" if np.isclose(usado, disponible) else "abundante (con holgura)"
        print(f"  Recurso {i}: {estado}; holgura = {disponible - usado:.2f}; precio sombra = {precio:.4f}")
    print("Los costos reducidos muestran cuánto debería mejorar la utilidad un producto no fabricado para entrar en la solución.")

    rng = np.random.default_rng(7)
    puntos = rng.uniform(0, [25, 25, 25], size=(100000, 3))
    usados = puntos @ A.T
    factibles = puntos[np.all(usados <= b, axis=1)]
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(factibles[:, 0], factibles[:, 1], factibles[:, 2], s=2, alpha=0.15, label="Factibles")
    ax.scatter(*cantidades, color="red", s=90, label="Optimo")
    ax.set_xlabel("A")
    ax.set_ylabel("B")
    ax.set_zlabel("C")
    ax.set_title("TP2 - Problema 3: región factible 3D")
    ax.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
