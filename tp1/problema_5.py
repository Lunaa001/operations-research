"""TP1 - Problema 5: dieta de costo minimo."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog


def main() -> None:
    resultado = linprog(c=[60, 80], A_ub=-np.array([[120, 100], [2, 5]], dtype=float), b_ub=[-1000, -30], bounds=[(0, None)] * 2, method="highs-ds")
    if not resultado.success:
        raise RuntimeError(resultado.message)
    a, b = resultado.x
    print("PROBLEMA 5")
    print(f"Alimento A: {a:.2f} unidades")
    print(f"Alimento B: {b:.2f} unidades")
    print(f"Costo minimo: ${resultado.fun:.2f}")
    print(f"Aporte final: {120*a + 100*b:.2f} calorias y {2*a + 5*b:.2f} gramos de proteina.")
    print("Conclusion: esta combinacion cumple los minimos requeridos con el menor costo.")

    x = np.linspace(0, 20, 500)
    calorias = (1000 - 120*x) / 100
    proteinas = (30 - 2*x) / 5
    limite = np.maximum.reduce([np.maximum(calorias, 0), np.maximum(proteinas, 0)])
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, calorias, label="Calorias")
    ax.plot(x, proteinas, label="Proteinas")
    ax.fill_between(x, limite, 20, alpha=0.2, label="Region factible")
    ax.scatter([a], [b], color="red", s=70, zorder=5, label="Optimo")
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 20)
    ax.set_xlabel("Unidades de A")
    ax.set_ylabel("Unidades de B")
    ax.set_title("Problema 5: dieta de costo minimo")
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
