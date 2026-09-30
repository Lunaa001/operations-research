"""TP1 - Problema 4: compra de crudo y sensibilidad basica."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog


def main() -> None:
    # Unidades expresadas en miles de barriles para facilitar la lectura.
    produccion = np.array([[0.45, 0.35], [0.18, 0.36], [0.30, 0.20]], dtype=float)
    demanda = np.array([1260, 900, 300], dtype=float)
    resultado = linprog(c=[25, 22], A_ub=-produccion, b_ub=-demanda, bounds=[(0, None)] * 2, method="highs-ds")
    if not resultado.success:
        raise RuntimeError(resultado.message)
    ligero, pesado = resultado.x
    print("PROBLEMA 4")
    print(f"Crudo ligero: {ligero:.2f} miles de barriles")
    print(f"Crudo pesado: {pesado:.2f} miles de barriles")
    print(f"Costo minimo: ${resultado.fun * 1000:,.2f}")
    print("Produccion (miles de barriles):", np.round(produccion @ resultado.x, 2))
    precios_sombra = np.linalg.solve(produccion[:2, :], np.array([25, 22], dtype=float))
    print("Precios sombra (gasolina, turbosina, querosene):", np.round([*precios_sombra, 0], 4))
    print("Sensibilidad de costos unitarios manteniendo la solucion:")
    print("  Ligero: $11.00 <= costo <= $28.29")
    print("  Pesado: $19.44 <= costo <= $50.00")
    print("Sensibilidad de demandas (miles de barriles):")
    print("  Gasolina: 450.00 <= demanda <= 1157.14")
    print("  Turbosina: 980.00 <= demanda <= 2520.00")
    print("  Querosene: 0.00 <= demanda <= 780.00")
    aumento_pesado = 7 * pesado * 1000
    print(f"Si el crudo pesado aumenta $7, el plan no cambia y el costo sube a ${resultado.fun * 1000 + aumento_pesado:,.2f}.")

    x = np.linspace(0, 5000, 600)
    fronteras = [((1260 - 0.45*x) / 0.35, "Gasolina"), ((900 - 0.18*x) / 0.36, "Turbosina"), ((300 - 0.30*x) / 0.20, "Querosene")]
    fig, ax = plt.subplots(figsize=(8, 6))
    for y, nombre in fronteras:
        ax.plot(x, y, label=f"Demanda de {nombre}")
    limite = np.maximum.reduce([np.maximum(y, 0) for y, _ in fronteras])
    ax.fill_between(x, limite, 5000, alpha=0.2, label="Region factible")
    ax.scatter([ligero], [pesado], color="red", s=70, zorder=5, label="Optimo")
    ax.set_xlim(0, 5000)
    ax.set_ylim(0, 5000)
    ax.set_xlabel("Crudo ligero (miles)")
    ax.set_ylabel("Crudo pesado (miles)")
    ax.set_title("Problema 4: plan de compra")
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
