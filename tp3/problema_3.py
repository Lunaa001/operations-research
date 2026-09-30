"""TP3 - Problema 3: hectareas enteras de maiz y trigo."""

import matplotlib.pyplot as plt
from scipy.optimize import linprog
from entera import resolver_entera


def main() -> None:
    print("PROBLEMA 3 - RELAJACION LINEAL Y CORTE")
    relajacion = linprog(
        c=[-5, -3],
        A_ub=[[1, 1], [3, 2], [-1, 1]],
        b_ub=[17, 14, 0],
        bounds=[(0, None), (0, None)],
        method="highs-ds",
    )
    if not relajacion.success:
        raise RuntimeError(relajacion.message)
    print(f"Relajacion PL: maiz = {relajacion.x[0]:.4f}, trigo = {relajacion.x[1]:.4f}")
    print(f"Ganancia de la relajacion: ${-relajacion.fun:.4f}")
    print("La solucion es fraccionaria. Se agrega el corte valido maiz <= 4,")
    print("porque 3 maiz <= 14 y maiz debe ser entero.")

    con_corte = linprog(
        c=[-5, -3],
        A_ub=[[1, 1], [3, 2], [-1, 1], [1, 0]],
        b_ub=[17, 14, 0, 4],
        bounds=[(0, None), (0, None)],
        method="highs-ds",
    )
    if not con_corte.success:
        raise RuntimeError(con_corte.message)
    print(f"Despues del corte: maiz = {con_corte.x[0]:.4f}, trigo = {con_corte.x[1]:.4f}")
    print(f"Ganancia despues del corte: ${-con_corte.fun:.4f}")

    def objetivo(v: tuple[int, int]) -> float:
        maiz, trigo = v
        return 5 * maiz + 3 * trigo

    def factible(v: tuple[int, int]) -> bool:
        maiz, trigo = v
        return maiz + trigo <= 17 and 3 * maiz + 2 * trigo <= 14 and trigo <= maiz

    solucion, _, soluciones = resolver_entera(["maiz", "trigo"], [4, 7], objetivo, factible)
    maiz, trigo = solucion
    print("\nComprobacion por enumeracion entera")
    print("Maximizar: 5 maiz + 3 trigo")
    print("Restricciones: M + T <= 17; 3M + 2T <= 14; T <= M; M,T enteras no negativas")
    print(f"Conclusion: dedicar {maiz} ha a maiz y {trigo} ha a trigo produce la mayor ganancia entera: ${objetivo((maiz, trigo)):.2f}.")
    print(f"Tierra usada: {maiz + trigo}/17 ha; fertilizante usado: {3*maiz + 2*trigo}/14 toneladas.")

    x = [v[0][0] for v in soluciones]
    y = [v[0][1] for v in soluciones]
    z = [v[1] for v in soluciones]
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(x, y, c=z, cmap="cividis", s=90)
    ax.scatter(relajacion.x[0], relajacion.x[1], color="orange", marker="x", s=100, label="Relajacion PL")
    ax.scatter([maiz], [trigo], color="red", s=100, label="Optimo")
    ax.set_xlabel("Hectareas de maiz")
    ax.set_ylabel("Hectareas de trigo")
    ax.set_title("TP3 - Problema 3: asignacion entera")
    ax.grid(True, alpha=0.3)
    ax.legend()
    plt.colorbar(ax.collections[0], ax=ax, label="Ganancia")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
