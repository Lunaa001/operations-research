"""TP2 - Problema 1: artefactos A y B con simplex."""

import numpy as np
import matplotlib.pyplot as plt
from simplex import simplex


def main() -> None:
    # Se sigue la convencion de la resolucion entregada: se toman los LD tal como aparecen.
    A = np.array([[4, 8], [5, 6], [12, 8]], dtype=float)
    b = np.array([480, 600, 540], dtype=float)
    resultado = simplex(np.array([100, 120], dtype=float), A, b, ["A", "B"])
    cantidades = resultado["solution"]
    uso = A @ cantidades
    print("\nConclusion final:")
    print(f"Se fabrican {cantidades[0]:.4f} artefactos A y {cantidades[1]:.4f} artefactos B.")
    print(f"Beneficio maximo: ${resultado['objective']:.2f}.")
    print(f"Holguras en maquinado, armado y montaje: {np.round(b - uso, 4)} horas.")

    x = np.linspace(0, 2.5, 500)
    limites = [(b[i] - A[i, 0] * x) / A[i, 1] for i in range(3)]
    fig, ax = plt.subplots(figsize=(8, 6))
    for limite, nombre in zip(limites, ("Maquinado", "Armado", "Montaje")):
        ax.plot(x, limite, label=nombre)
    factible = np.minimum.reduce(limites)
    ax.fill_between(x, 0, factible, where=factible >= 0, alpha=0.2, label="Region factible")
    ax.scatter(*cantidades, color="red", s=75, zorder=5, label="Optimo")
    ax.set_xlim(0, 2.5)
    ax.set_ylim(0, 2.5)
    ax.set_xlabel("Artefactos A")
    ax.set_ylabel("Artefactos B")
    ax.set_title("TP2 - Problema 1: solucion simplex")
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
