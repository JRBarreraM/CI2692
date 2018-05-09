# Proyecto01.py
#
# DESCRIPCION: Programa que permite a un usuario resolver el problema del recorrido \
# del caballo, a traves de 3 modalidades: Manual: donde es el usuario, quien intenta \
# resolver el acertijo, "Fuerza Bruta" y "Divide y conquistarás": donde un algoritmo \
# de backtracking o basandose en las soluciones de Penberry, busca la solucion o determina \
# el tablero como irresoluble.
#
# Autores: 
#	Br. Jose Barrera y Br. Alfredo Cruz.
#
# Ultima modificacion: 17/05/2018.

"""
   CONSTANTES Logicas	#informacion proporcionada por el usuriario que el programa no modifica:
  
   VARIABLES Logicas

"""	
import random
# Lista de subprogramas (funciones) que usa el esqueleto principal:

def crearPosibles(tabl=list,Anterior_Jugada=list) -> list:
	# VAR:
		# Posibles : list 
		# Candidatos : list
		# hay_fila : bool
		# hay_columna						#Candidatos: Se incializa con -1, porque no existe\
	Candidatos=[[-1,-1]*8]					#dicha fila o comuna en una matriz. Posibles: Se inicia\
	hay_fila,hay_columna=False,False		#vacia para llenarse con aquellas opciones que cumplan las \
	Posibles=[]								#condiciones del caballo y que sean una posicion libre del tablero.
	anteriorfila=Anterior_Jugada[0]
	anteriorcolumna=Anterior_Jugada[1]
	if 0<=anteriorfila-2<Tam:				#-----------------------------------------------------------------
		Candidatos[0][0]=(anteriorfila-2)	
		Candidatos[1][0]=(anteriorfila-2)
		Candidatos[2][0]=(anteriorfila-1)
		Candidatos[3][0]=(anteriorfila-1)
		hay_fila=True
	elif 0<=anteriorfila-1<Tam:
		Candidatos[2][0]=(anteriorfila-1)
		Candidatos[3][0]=(anteriorfila-1)
		hay_fila=True

	if 0<=anteriorfila+2<Tam:
		Candidatos[4][0]=(anteriorfila+1)
		Candidatos[5][0]=(anteriorfila+1)
		Candidatos[6][0]=(anteriorfila+2)
		Candidatos[7][0]=(anteriorfila+2)
		hay_fila=True
	elif 0<=anteriorfila+1<Tam:
		Candidatos[4][0]=(anteriorfila+1)	#					"""CONDICIONES DEL CABALLO"""
		Candidatos[5][0]=(anteriorfila+1)		
		d=(anteriorfila+1)
		hay_fila=True
	
	if hay_fila:
		if 0<=anteriorcolumna-2<Tam:
		Candidatos[0][1]=(anteriorcolumna-2)
		Candidatos[1][1]=(anteriorcolumna-2)
		Candidatos[2][1]=(anteriorcolumna-1)
		Candidatos[3][1]=(anteriorcolumna-1)
		hay_fila=True
	elif 0<=anteriorcolumna-1<Tam:
		Candidatos[2][1]=(anteriorcolumna-1)
		Candidatos[3][1]=(anteriorcolumna-1)
		hay_fila=True

	if 0<=anteriorcolumna+2<Tam:
		Candidatos[4][1]=(anteriorcolumna+1)
		Candidatos[5][1]=(anteriorcolumna+1)
		Candidatos[6][1]=(anteriorcolumna+2)
		Candidatos[7][1]=(anteriorcolumna+2)
		hay_fila=True
	elif 0<=anteriorcolumna+1<Tam:
		Candidatos[4][1]=(anteriorcolumna+1)
		Candidatos[5][1]=(anteriorcolumna+1)		
		d=(anteriorcolumna+1)
		hay_fila=True						#-----------------------------------------------------------------

	if hay_columna and hay_fila:
		for i in range(8):
			if Candidatos[i][0]>-1 and Candidatos[i][1]>-1:
					if tabl[Candidatos[i][0]][Candidatos[i][1]]==0:		#Casilla libre
						Posibles.append(Candidatos[i])				#Es una posible jugada valida, se agrega

	return Posibles

#Descripcion: Pide al usuario la columna donde desea jugar, toma el tabl y lo devuelve mas las coordenadas de la jugada
# Parametros:
def jugadaUser( tabl = list, turno = int, Posibles=list ) -> (list,int,int) :
	# VAR:
		# jugada_seleccionada : int
		# opciones : int
		# Intentos : int
	Intentos=0
	opciones=len(Posibles)
	while Intentos<8:
		try:
			jugada_seleccionada=int(input("Escoja la jugada deseada: "))
			Intentos+=1
			assert(0<=jugada_seleccionada<opciones)
			break		
		except:
			print "Parece que no has escojido una jugada valida"
	if Intentos=7:
		print "Demasiados intentos, tendras que empezar de nuevo"

	anteriorfila=Posibles[jugada_seleccionada][0]
	actualcolumna=Posibles[jugada_seleccionada][1]	
	tabl[actualfila][actualcolumna]=turno
	
	return tabl,actualfila,actualcolumna

def jugadaBruta( tabl = list, turno = int, Posibles=list ) -> (list,int,int) :
	# VAR:
		# jugada_seleccionada : int
		# opciones : int
		# Intentos : int
	jugada_seleccionada=random.randint(0,len(Posibles))
	anteriorfila=Posibles[jugada_seleccionada][0]
	actualcolumna=Posibles[jugada_seleccionada][1]	
	tabl[actualfila][actualcolumna]=turno

def mostrar_tablero(tabl=list, Tam=int)->:
	mostrar_columnas=[0]*Tam
	for i in range(Tam):
		print i,"",|,"",tabl[i]


def back_in_time(tabl=list,anteriorfila=int,anteriorcolumna=int,turno=int)->(list,int,int,list):
	# VAR:
		# Posibles : list
		# Fila_Del_Pasado : int
		# Columna_Del_Pasado : int
		# Malas_Jugadas : list

	tabl[anteriorfila][anteriorcolumna]=0
	Posibles=crearPosibles(tabl,anteriorfila,anteriorcolumna)
	Malas_Jugadas=[anteriorfila,anteriorcolumna]

	for i in len(Posibles):
		Fila_Del_Pasado=Posibles[i][0]
		Columna_Del_Pasado=Posibles[i][1]
		if tabl[Fila_Del_Pasado][Columna_Del_Pasado]==turno-2:
			anteriorfila=Fila_Del_Pasado
			anteriorcolumna=Columna_Del_Pasado
			Anterior_Jugada=[Fila_Del_Pasado,Columna_Del_Pasado]
			return tabl,Anterior_Jugada,Malas_Jugadas


# Incializacion de las variables del juego:
dentro=True							# Para entrar en el loop del juego
jugando=False						# Para entra primero al menu
anteriorfila,anteriorcolumna=0,0	# Jugada Predeterminada de la IA en su primer turno
tabl=[[0]*Tam for i in range(Tam)]	# Crear tablero de juego logico.

#Loop del juego

while dentro :							# Dentro del juego
	if not(jugando):					# en menu
		while True: 					# Se permite al usuario introducir nuevos datos correctos
			try: 
				Tam=int(input("Indique el tamaño del tablero (Debe ser un natural mayor o igual que 3)"))
				assert( Tam>=3 )
				break
			except:
				print "Ingrese un natural mayor o igual que 3"			
			try: 
				eleccion_algoritmo=int(input("Que algorimo desea usar?(0=Manual,1=Fuerza_Bruta,2=Divide_y_conquistaras,3=Terminar)"))
				assert( eleccion_algoritmo==0 or eleccion_algoritmo==2 or eleccion_algoritmo==1 or eleccion_algoritmo==3 )
				break
			except:
				print "Seleccione 0,1,2,3 o 4"
		
		tabl=[[0]*Tam for i in range(Tam)]		# Crear tablero de juego lleno de ceros.
		jugando=True
		tabl[0][0]=1
		turno=2
		Jugada_Inicial=[0][0]
		Anterior_Jugada=[0,0]
		Malas_Jugadas=[]
		mostrar_columnas=[0]*Tam

		for i in range(Tam):
			mostrar_columnas[i]=i

	elif jugando and eleccion_algoritmo==3:		# El usuario decide que quiere salir del juego
			dentro=False						# Salimos del loop del juego
			print "Hasta luego!"				# Nos depedimos del usuario
	
	elif jugando and eleccion_algoritmo==2:		# Modo divide y conquistaras


	elif jugando and eleccion_algoritmo==1: 	# Modo fuerza bruta activado

		Posibles=crearPosibles(tabl,Anterior_Jugada)
		for i in range(len(Posibles)):
			Posibles.remove(Malas_Jugadas[i])

		if Anterior_Jugada==Jugada_Inicial and len(Posibles)==0:
			dentro=False						# Salimos del loop del juego
			print "Se intentaron todas las posibles rutas, no hay solucion"

		elif len(Posibles)==0:
			if Turno==(Tam*Tam)+1
				print "Felicidades, lo has conseguido"
				jugando=False
			else:
				Rback_in_time=back_in_time(tabl,Anterior_Jugada,turno)
				tabl=Rback_in_time[0]
				Anterior_Jugada=Rback_in_time[1]
				Malas_Jugadas.append(Rback_in_time[2])
				turno=turno-2
		elif len(Posibles)==1:
			tabl[Posibles[0][0]][Posibles[0][1]]=turno
			Anterior_Jugada=[Posibles[0][0],Posibles[0][1]]

		elif len(Posibles)>=2:
			Rbruta=jugadaBruta(tabl,turno,Posibles)
			tabl=Rbruta[0]
			Anterior_Jugada=[Rbruta[1],Rbruta[2]]

	
	elif jugando and eleccion_algoritmo==1:		# Modo manual activado

		seguir=bool(input("Desea seguir en esta partida?(Si=Enter)(No=Else)")) # en cada turno
		step_back=bool(input("Desea anular su jugada anterior?(Si=Enter)(No=Else)")) # en cada turno
		if seguir:
			jugando=False
			print "Nos vemos"

		elif not(seguir):
			Posibles=crearPosibles(tabl,Anterior_Jugada)
			for i in range(len(Posibles)):
				Posibles.remove(Malas_Jugadas[i])
			
			if step_back:
				if Anterior_Jugada==Jugada_Inicial:
					print "No es posible volver mas atras"
				else:
					Rback_in_time=back_in_time(tabl,Anterior_Jugada,turno)
					tabl=Rback_in_time[0]
					Anterior_Jugada=Rback_in_time[1]

			elif Anterior_Jugada==Jugada_Inicial and len(Posibles)==0:
				dentro=False						# Salimos del loop del juego
				print "Se intentaron todas las posibles rutas, no hay solucion"

			elif len(Posibles)==0:
				if Turno==(Tam*Tam)+1
					print "Felicidades, lo has conseguido"
					jugando=False
				else:
					print "Se agotaron las opciones, volviendo un paso atras"
					Rback_in_time=back_in_time(tabl,Anterior_Jugada,turno)
					tabl=Rback_in_time[0]
					Anterior_Jugada=Rback_in_time[1]
					Malas_Jugadas.append(Rback_in_time[2])
					turno=turno-2
			elif len(Posibles)==1:
				tabl[Posibles[0][0]][Posibles[0][1]]=turno
				Anterior_Jugada=[Posibles[0][0],Posibles[0][1]]

			elif len(Posibles)>=2:
				print "Veamos el tablero"
				print "\n"
				mostrar_tablero(tabl, Tam)
				print mostrar_columnas
				print "Estas son tus Posibles jugadas"
				print Posibles	
				Ruser=jugadaUser(tabl, turno, Posibles)	# Almacenamos los cambios tras la jugada del usuario.
				tabl=Ruser[0]							# Reescribimos el tablero con la jugada
				Anterior_Jugada=[Ruser[1],Ruser[2]]		# Guardamos la jugada

			turno = turno + 1		# contamos el siguiente turno

assert( dentro==False )

# Aqui termina el el loop del juego.