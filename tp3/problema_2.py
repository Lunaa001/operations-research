"""TP3 - Problema 2: anuncios enteros."""

import matplotlib.pyplot as plt
from scipy.optimize import linprog
from entera import resolver_entera


def main() -> None:
    def objetivo(v: tuple[int, int]) -> float:
        television, radio = v
        return 10 * television + 6 * radio

    def factible(v: tuple[int, int]) -> bool:
        television, radio = v
        return 5 * television + 3 * radio <= 19 and television >= 2 and radio <= 5

    solucion, _, soluciones = resolver_entera(["TV", "radio"], [3, 5], objetivo, factible)
    television, radio = solucion
    print("\nPROBLEMA 2")
    relajacion = linprog(c=[-10, -6], A_ub=[[5, 3], [0, 1]], b_ub=[19, 5], bounds=[(2, None), (0, None)], method="highs-ds")
    print(f"Relajacion PL: TV = {relajacion.x[0]:.4f}, radio = {relajacion.x[1]:.4f}")
    print("La relajacion tiene optimos alternativos porque el costo reducido de radio es 0.")
    print("Se elige el vertice alternativo entero TV = 2, radio = 3, sin aplicar corte.")
    print("Maximizar: 10 TV + 6 radio (miles de clientes potenciales)")
    print("Restricciones: 5TV + 3R <= 19; TV >= 2; R <= 5; TV,R enteros")
    print(f"Conclusion: contratar {television} anuncios de TV y {radio} de radio alcanza {objetivo((television, radio)):.0f} mil clientes potenciales.")
    print(f"Presupuesto usado: {5*television + 3*radio}/19 mil; radio contratado: {radio}/5 anuncios.")

    x = [v[0][0] for v in soluciones]
    y = [v[0][1] for v in soluciones]
    z = [v[1] for v in soluciones]
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(x, y, c=z, cmap="plasma", s=90)
    ax.scatter([television], [radio], color="red", s=100, label="Optimo")
    ax.set_xlabel("Anuncios de TV")
    ax.set_ylabel("Anuncios de radio")
    ax.set_title("TP3 - Problema 2: combinaciones enteras")
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.colorbar(ax.collections[0], ax=ax, label="Alcance")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
