"""TP2 - Problema 2: mesas, sillas y sillones con simplex."""

import numpy as np
import matplotlib.pyplot as plt
from simplex import simplex


def main() -> None:
    A = np.array([[4, 4, 5], [15, 10, 25], [40, 60, 50]], dtype=float)
    b = np.array([80, 600, 500], dtype=float)
    resultado = simplex(np.array([40, 50, 60], dtype=float), A, b, ["mesa", "silla", "sillon"])
    cantidades = resultado["solution"]
    uso = A @ cantidades
    print("\nRecursos usados y sobrantes:")
    for nombre, usado, disponible in zip(("Produccion", "Madera", "Remaches"), uso, b):
        print(f"  {nombre}: {usado:.2f} / {disponible:.2f}; holgura = {disponible - usado:.2f}")
    print("Conclusión: un precio sombra positivo identifica un recurso cuyo aumento mejora la ganancia, dentro de su rango de sensibilidad.")

    fig, ax = plt.subplots(figsize=(8, 6))
    nombres = ["Produccion", "Madera", "Remaches"]
    ax.bar(nombres, b, label="Disponible", alpha=0.45)
    ax.bar(nombres, uso, label="Usado")
    ax.set_ylabel("Cantidad de recurso")
    ax.set_title("TP2 - Problema 2: recursos disponibles y utilizados")
    ax.legend()
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
