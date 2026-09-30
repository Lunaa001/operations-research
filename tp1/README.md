# TP1 - Investigacion operativa

Cada problema esta separado en un archivo Python. Todos imprimen el modelo resuelto y muestran la region factible con el punto optimo.

## Instalacion

```bash
python -m pip install numpy scipy matplotlib
```

## Ejecucion

Desde la carpeta principal del proyecto:

```bash
python tp1/problema_1.py
python tp1/problema_2.py
python tp1/problema_3.py
python tp1/problema_4.py
python tp1/problema_5.py
python tp1/problema_6.py
```

`linprog` minimiza por defecto, por eso en problemas de maximizar se usa el vector de utilidades cambiado de signo. Los scripts usan `method="highs-ds"`, el metodo dual simplex de HiGHS. En el Problema 3 la grafica es 3D porque hay tres variables. El Problema 4 imprime intervalos de sensibilidad, precios sombra y el impacto del aumento del precio del crudo pesado. La grafica aparece al ejecutar los archivos en un entorno con interfaz grafica.
