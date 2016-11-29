#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Programa Servidor
# Fuente original de este codigo: www.pythondiario.com
# Utilizado para fines academicos en el curso CI-1320 

import socket
import sys
from Tkinter import *
from threading import Thread
from time import sleep
from ctypes import *

respuestas =""
exitThread = False
def iniciarServidor():
	listaRespuestas=[]
	tamano = 0
	respuestasAlCliente = open('asciiRespuesta.txt', 'r')
	for line in respuestasAlCliente:
		listaRespuestas.append(line)

	tamano=len(listaRespuestas)
	print(listaRespuestas[0])
	# Creando el socket TCP/IP
	global sock
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Enlace de socket y puerto
	server_address = ('localhost', int(ContentPuerto.get()))
	global respuestas
	respuestas = respuestas + "Levantando puerto "+str(server_address)+"\n\n"
	sock.bind(server_address)

	# Escuchando conexiones entrantes
	sock.listen(1)
	#root.destroy()
	global exitThread
	contador=0
	while 1:
	    # Esperando conexion
	    respuestas = respuestas+"esperando para conectarse\n"
	    #EntryRespuestaServer.insert(END,"Emepezando")
	    connection, client_address = sock.accept()
	 
	    try:
	    	respuestas+="Conexion entrante"+str(client_address)+"\n"
	        # Recibe los datos en trozos y reetransmite
	        respuestas+="recibido:\n"
	        while 1:
	            data = connection.recv(1000)
	            respuestas =respuestas + data+"\n"
	            if data:
	            	respuestas = respuestas+"Enviando mensaje de vuelta al cliente:\n "+listaRespuestas[contador]+"\n"
	                connection.sendall(listaRespuestas[contador])
	                contador=(contador+1)%tamano
	            else:
	            	respuestas = respuestas+"No hay más datos\n---------------------------------------\n\n"
	                break
	             
	    finally:
	        # Cerrando conexion
	        connection.close()

def iniciarThread():
	if __name__ == "__main__":
	    global thread 
	    thread = Thread(target = iniciarServidor, args = ( ))
	    thread.start()
	    EntryPuerto.config(state=DISABLED)
    	btnSubmit1.config(state=DISABLED)



def actualizarMensajes():	
	EntryRespuestaServer.config(state=NORMAL)
	EntryRespuestaServer.delete(1.0, END)
	EntryRespuestaServer.insert(END, respuestas)
	EntryRespuestaServer.see(END)
	EntryRespuestaServer.config(state=DISABLED)	
	root.after(1000,actualizarMensajes)

def cerrar():
	#global exitThread
	global respuestas
	global sock
	global thread
	#exitThread = True
	sock.close()
	respuestas=""
	EntryRespuestaServer.config(state=NORMAL)
	EntryRespuestaServer.delete(1.0, END)
	EntryRespuestaServer.insert(END, "")
	EntryRespuestaServer.config(state=DISABLED)	
	if thread.isAlive():
	    try:
	    	print("detenido")
	        thread._Thread__stop()
	        root.quit()
	    except:
	        print("imposible to terminate")


#inicio de la interfaz grafica
root = Tk()#indica en inicio de loop
ContentPuerto=StringVar()

root.title("Socket Cliente-Servidor Python")#titulo de la ventana
root.geometry("500x450")#tamaño de la ventana
root.config(bg = "#000066")#color azul de background

separador1 = LabelFrame(root,height=30, bg="#16EE67", text="SERVIDOR - TP2 - Johan Durán & Kenneth Calvo - Universidad De Costa Rica")#crea un espacio - separador
separador1.pack(fill="both")

LabelPuerto = Label(root, text="Puerto")
LabelPuerto.pack(side=TOP,fill="both")

EntryPuerto = Entry(root, bd =5,textvariable=ContentPuerto)
EntryPuerto.pack(fill="both",side=TOP)

separador2 = LabelFrame(root,height=10, bg="#16EE67")#crea un espacio - separador
separador2.pack(fill="both")

btnSubmit1 = Button(root,text="Iniciar Servidor", bg="#B2B3E8", command=iniciarThread)
btnSubmit1.pack(fill="both",side=TOP)

separador4 = LabelFrame(root,height=30, bg="#16EE67")#crea un espacio - separador
separador4.pack(fill="both")

btnSubmit2 = Button(root,text="Desconectar", bg="#B2B3E8", command=cerrar)
btnSubmit2.pack(fill="both",side=TOP)

LabelRespuesta = Label(root, text="Conexiones")
LabelRespuesta.pack(side=TOP,fill="both")


scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

EntryRespuestaServer = Text(root)
EntryRespuestaServer.pack(fill="both",side=TOP)
EntryRespuestaServer.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=EntryRespuestaServer.yview)
EntryRespuestaServer.config(state=DISABLED)

actualizarMensajes()

root.mainloop()#llama el loop