# TP3 - Programacion entera

Cada problema esta en un archivo independiente. Los tres problemas resuelven primero la relajacion lineal, agregan un corte valido cuando aparece una solucion fraccionaria y luego verifican el resultado enumerando las combinaciones enteras.

## Ejecucion

Desde la carpeta principal:

```bash
python tp3/problema_1.py
python tp3/problema_2.py
python tp3/problema_3.py
```

La salida muestra el modelo, la cantidad de soluciones enteras evaluadas, la solucion optima y una grafica de los puntos factibles. Para instalar la libreria grafica:

```bash
python -m pip install matplotlib
```

En el Problema 3 se interpreta que las hectareas tambien deben ser unidades enteras, porque el trabajo corresponde a programacion entera.

En el Problema 3, la relajacion produce maiz = 14/3 y trigo = 0. Como el maiz debe ser entero, se agrega el corte valido `maiz <= 4`; la nueva solucion es maiz = 4 y trigo = 1.
