"""TP3 - Problema 1: mesas y sillas enteras."""

import matplotlib.pyplot as plt
from scipy.optimize import linprog
from entera import resolver_entera


def main() -> None:
    def objetivo(v: tuple[int, int]) -> float:
        mesas, sillas = v
        return 5 * mesas + 3 * sillas

    def factible(v: tuple[int, int]) -> bool:
        mesas, sillas = v
        return 3 * mesas + 2 * sillas <= 17 and 2 * mesas + sillas <= 14 and sillas <= 4

    solucion, _, soluciones = resolver_entera(["mesas", "sillas"], [5, 8], objetivo, factible)
    mesas, sillas = solucion
    print("\nPROBLEMA 1")
    relajacion = linprog(c=[-5, -3], A_ub=[[3, 2], [2, 1], [0, 1]], b_ub=[17, 14, 4], bounds=[(0, None)] * 2, method="highs-ds")
    print(f"Relajacion PL: mesas = {relajacion.x[0]:.4f}, sillas = {relajacion.x[1]:.4f}")
    con_corte = linprog(c=[-5, -3], A_ub=[[3, 2], [2, 1], [0, 1], [1, 0]], b_ub=[17, 14, 4, 5], bounds=[(0, None)] * 2, method="highs-ds")
    print("Se agrega el corte valido mesas <= 5 porque 3 mesas <= 17 y mesas debe ser entera.")
    print(f"Despues del corte: mesas = {con_corte.x[0]:.4f}, sillas = {con_corte.x[1]:.4f}")
    print("Maximizar: 5 mesas + 3 sillas")
    print("Restricciones: 3M + 2S <= 17; 2M + S <= 14; S <= 4; M,S enteras no negativas")
    print(f"Conclusion: fabricar {mesas} mesas y {sillas} sillas produce la mayor ganancia entera: ${objetivo((mesas, sillas)):.2f}.")
    print(f"Uso de madera: {3*mesas + 2*sillas}/17 m2; mano de obra: {2*mesas + sillas}/14 h.")

    x = [v[0][0] for v in soluciones]
    y = [v[0][1] for v in soluciones]
    z = [v[1] for v in soluciones]
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(x, y, c=z, cmap="viridis", s=80)
    ax.scatter([mesas], [sillas], color="red", s=100, label="Optimo")
    ax.set_xlabel("Mesas")
    ax.set_ylabel("Sillas")
    ax.set_title("TP3 - Problema 1: soluciones enteras factibles")
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.colorbar(ax.collections[0], ax=ax, label="Ganancia")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
