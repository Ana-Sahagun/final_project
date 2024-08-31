README:
# Estudio de la sostenibilidad de las finanzas públicas en España

## Descripción
El objeto de estudio es la determinación de la sostenibilidad financiera en España desde una perspectiva temporal. Para ello, se analizará la evolución de las principales variables determinantes, así como otros determinantes indirectos. 

## Características Principales
- Análisis de datos con Python (pandas, numpy, etc.)
- Visualización interactiva con Power BI

## Requisitos Previos
- Python 3.x
- Power BI Desktop

## Fuente
-INE
-Datos Macro

## Requisitos Previos
-Base de datos inicial: “BD para estudio de sostenibilidad de la deuda”
-Datos tratados para analizar en Power BI: “01_exploratory_analysis”

## Tratamiento de datos en Python
1.	Transformación de Datos: Se ajustaron los tipos de datos de las columnas clave, convirtiendo variables como "tasa de natalidad" a tipo float, "año" a tipo integer, y otras fechas a tipo date según lo requerido para el análisis.
2.	Análisis de Valores Nulos: Se realizó un estudio exhaustivo de los valores NaN y null presentes en cada columna. Se identificó que faltaban 22 datos correspondientes a los intereses de la deuda, lo que llevó a la decisión de limitar el análisis al período comprendido entre el año 2002 y la actualidad.
3.	Estudio de Outliers: Aunque se detectaron outliers en los datos, estos fueron conservados. Se consideró que estos puntos atípicos, posiblemente relacionados con eventos extraordinarios como la crisis del COVID-19, proporcionan una visión más completa del análisis y explican fenómenos importantes, como la recuperación en forma de "V".
4.	Análisis de Correlaciones: Se llevó a cabo un estudio de correlaciones entre las variables, observándose altos niveles de correlación. Sin embargo, estos resultados no fueron sorprendentes dado que las variables están estrechamente relacionadas entre sí.
5.	Visualización Preliminar: Se realizó una previsualización de la evolución de las principales variables del conjunto de datos, facilitando una primera comprensión de las tendencias y patrones.
6.	Creación de Variable de Sostenibilidad: Finalmente, se generó una nueva variable que calcula la sostenibilidad de la deuda de manera simplificada, aportando un indicador adicional para el análisis.
Este conjunto de pasos asegura un análisis robusto y fundamentado en la preparación y transformación de los datos, garantizando la fiabilidad de los resultados obtenidos.

## Visualización de datos en Power BI
1.	Se introduce la importancia del estudio
2.	Se ofrece una visión general de la situación actual de los principales determinantes de la sostenibilidad de las finanzas públicas en España
3.	Estudio del tono de política Fiscal y le impacto en el stock de deuda
4.	Estudio de la relación del déficit con el ciclo económico
5.	Estudio de la ecuación de sostenibilidad y análisis gráfico de sus principales determinantes 
6.	Estudio del efecto inflacionario (derivado de la política monetaria) sobre la sostenibilidad financiera	
7.	Consideración de otros elementos indirectos de la sostenibilidad financiera. Especial referencia a la comparativa gasto vs. Inversión y a la tendencia de la tasa de natalidad.
8.	Elaboración de recomendaciones de política económica.


