"""TP1 - Problema 6: produccion de automoviles."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog


def main() -> None:
    utilidad = np.array([10000 - 10 - 70, 8000 - 10 - 70], dtype=float)
    recursos = np.array([[200, 150], [18, 20]], dtype=float)
    disponibles = np.array([80000, 9000], dtype=float)
    resultado = linprog(c=-utilidad, A_ub=recursos, b_ub=disponibles, bounds=[(0, None)] * 2, method="highs-ds")
    if not resultado.success:
        raise RuntimeError(resultado.message)
    compactos, subcompactos = resultado.x
    print("PROBLEMA 6")
    print(f"Compactos: {compactos:.2f}")
    print(f"Subcompactos: {subcompactos:.2f}")
    print(f"Ganancia maxima: ${-resultado.fun:,.2f}")
    uso = recursos @ resultado.x
    print(f"Recursos usados: {uso[0]:.2f} lb de materia prima y {uso[1]:.2f} h de mano de obra.")
    print(f"Holguras: {disponibles[0] - uso[0]:.2f} lb y {disponibles[1] - uso[1]:.2f} h.")
    print("Conclusion: la mezcla usa completamente los recursos que limitan la ganancia.")
    print("Precios sombra aproximados:", np.round(-resultado.ineqlin.marginals, 4))

    x = np.linspace(0, 500, 500)
    materia = (80000 - 200*x) / 150
    mano_obra = (9000 - 18*x) / 20
    limite = np.minimum.reduce([np.maximum(materia, 0), np.maximum(mano_obra, 0)])
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, materia, label="Materia prima")
    ax.plot(x, mano_obra, label="Mano de obra")
    ax.fill_between(x, 0, limite, where=limite >= 0, alpha=0.2, label="Region factible")
    ax.scatter([compactos], [subcompactos], color="red", s=70, zorder=5, label="Optimo")
    ax.set_xlim(0, 500)
    ax.set_ylim(0, 500)
    ax.set_xlabel("Compactos")
    ax.set_ylabel("Subcompactos")
    ax.set_title("Problema 6: produccion optima")
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
