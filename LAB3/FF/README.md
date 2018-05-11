<table>
	<tr>
		<th colspan="2" style="text-align:center">
			<img src="http://www.usb.ve/conocer/corporativa/archivos/logos/logo/logo.gif" width="64" height="43"><br/>
			Universidad Sim&oacute;n Bol&iacute;var<br/>
			Departamento de Computaci&oacute;n y Tecnolog&iacute;a de la Informaci&oacute;n<br/>
			Laboratorio de Algoritmos y Estructuras de Datos II (CI 2692)
	</tr>
	<tr>
		<th scope="row">Asignaci&oacute;n:</th>
		<td style="text-align:right">Laboratorio 3</td>
	</tr>
	<tr>
		<th scope="row">Modalidad:</th>
		<td style="text-align:right">Individual</td>
	</tr>
	<tr>
		<th scope="row">Ponderación:</th>
		<td style="text-align:right">2%</td>
	</tr>
	<tr>
		<th scope="row">Asignado:</th>
		<td style="text-align:right">Jueves, 10 de mayo de 2018 (sem 3)</td>
	</tr>
	<tr>
		<th scope="row">Entrega:</th>
		<td style="text-align:right">Sábado, 12 de mayo de 2018 (sem 3)</td>
	</tr>
</table>

### Lab-03: Heapsort y quicksort

#### Objetivos:

1. Implementar los algoritmos de ordenamiento heapsort y quicksort (determin&iacute;stico y 
randomizado), y comparalos con mergesort y el algoritmo de ordenamiento nativo de Python.

Cada grupo debe entregar el c&oacute;digo implementado y un informe haciendo commit 
en el repositorio.

Todos los procedimientos se deben implementar dentro de la plantilla `lab_03.py` 
en la parte del archivo prevista para ello. Las *firmas* de los procedimientos
que deben implementar son las siguientes:

```
def heapsort_aux(A, p, r):
def quicksort_rec(A, p, r, partition_function):
def partition_with_pivot(A, p, r, pivot):
```
Con estos tres procedimientos se implementan heapsort y las dos versiones de 
quicksort:

```
def heapsort(A):
    heapsort_aux(A, 0, len(A) - 1)

def quicksort(A):
    quicksort_rec(A, 0, len(A) - 1, partition)

def quicksort_randomized(A):
    quicksort_rec(A, 0, len(A) - 1, partition_randomized)

def partition(A, p, r):
    pivot = A[r]
    return partition_with_pivot(A, p, r, pivot)

def partition_randomized(A, p, r):
    pivot_index = Random(p, r)
    pivot = A[pivot_index]
    A[pivot_index] = A[r]
    A[r] = pivot
    return partition_with_pivot(A, p, r, pivot)
```

El argumento ``partition_function`` es la *funci&oacute;n de partici&oacute;n*
en quicksort: para quicksort determin&iacute;stico se utiliza ```partition```
y para quicksort randomizado se utiliza ```partition_randomized```.

La funci&oacute;n de partici&oacute;n vista en clase s&oacute;lo retorna un &iacute;ndice
```q``` tal que ```A[q]``` contiene el pivote, los elementos ```A[i]``` para
r&le;i<q satisfacen ```A[i]<=A[q]```, y los elementos ```A[j]``` para q<j&le;r
satisfacen ```A[q]<A[j]```.
Sin embargo, usted debe implementar una funci&oacute;n de partici&oacute;n (i.e.
```partition_with_pivot```) que retorne *dos &iacute;ndices* ```l``` y ```m```
tales que: ```A[i]<A[l]``` para r&le;i<l, ```A[l]=A[l+1]=...=A[m]```igual al pivote,
y ```A[m]<A[j]``` para m<j&le;r.

Con est&aacute; funci&oacute;n, s&oacute;lo hace falta hacer recursi&oacute;n sobre
los subarreglos ```A[r,l-1]``` y ```A[m+1,r]``` lo que *garantiza* el desempe&ntilde;o
de quicksort a&uacute;n cuando existan elementos *repetidos*.


Todos los algoritmos se eval&uacute;an de forma *autom&aacute;tica* sobre fuentes
de datos provistas y se generan estad&iacute;sticos de tiempo de ejecuci&oacute;n.
Una vez que se hayan implementado los algoritmos, los experimentos se ejecutan desde
el *shell* de una de las siguiente formas:

```
python lab_03.py > data.csv
python lab_03.py | tee data.csv
```

La primera forma *redirecciona* la salida de la ejecuci&oacute;n al archivo ```data.csv```.
La segunda forma utiliza el programa ```tee``` de unix para mostrar por pantalla la salida y
redireccionarla al archivo ```data.csv```.

Luego usamos el programa estad&iacute;stico R para generar gr&aacute;ficas del tiempo 
de corrida y error:

```
R --no-save < ../common/plots/plot_lab_03.R
```

Se generan X gr&aacute;ficas que deben lucir de la siguiente forma:

![](../example/lab_03/plot_01.png)
![](../example/lab_03/plot_02.png)

#### Archivos de entrada:
Nuevamente se proporcionan archivos peque&ntilde;os para que puedan probar su programa:
* `carnets.txt`, el cual se encuentra ordenado, le permitirá probar el mejor caso
* `nombres.txt`, el cual se encuentra desordenado, le permitirá probar el caso promedio
* `stenrac.txt` (carnets invertido), el cual se encuentra en orden inverso, le permitirá probar el peor caso

El archivo para evaluar los tiempos de sus implementaciones es `web2`,

