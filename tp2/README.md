# TP2 - Metodo simplex

Cada problema esta separado en su propio archivo. La rutina `simplex.py` imprime la tabla inicial, cada pivote y la tabla final.

## Ejecutar

Desde la carpeta principal:

```bash
python tp2/problema_1.py
python tp2/problema_2.py
python tp2/problema_3.py
```

Dependencias:

```bash
python -m pip install numpy matplotlib
```

## Interpretacion

- La columna `RHS` de la tabla final contiene los valores de las variables basicas.
- Las variables `s1`, `s2`, etc. son holguras: recursos que quedan sin utilizar.
- Los precios sombra indican cuánto aumenta la ganancia si aumenta en una unidad el recurso correspondiente, mientras no se salga del rango de sensibilidad.
- Un costo reducido negativo indica que una variable no básica no conviene producir con los coeficientes actuales.
- En el Problema 1 se siguen los valores del lado derecho tal como aparecen en la resolución de clase: 480, 600 y 540. Así se obtiene A = 7,5, B = 56,25 y Z = 7.500.
