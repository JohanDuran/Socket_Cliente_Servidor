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
respuestas =""
exitThread = False
def iniciarServidor():
	# Creando el socket TCP/IP
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Enlace de socket y puerto
	server_address = ('localhost', int(ContentPuerto.get()))
	global respuestas
	respuestas = respuestas + "\nLevantando puerto "+str(server_address)
	sock.bind(server_address)

	# Escuchando conexiones entrantes
	sock.listen(1)
	#root.destroy()
	global exitThread
	while exitThread == False:
	    # Esperando conexion
	    respuestas = respuestas+"\nesperando para conectarse"
	    #EntryRespuestaServer.insert(END,"Emepezando")
	    connection, client_address = sock.accept()
	 
	    try:
	    	respuestas+="\nConexion entrante"+str(client_address)
	        # Recibe los datos en trozos y reetransmite
	        while exitThread == False:
	            data = connection.recv(1000)
	            respuestas = respuestas+"\nrecibido: "+data
	            if data:
	            	respuestas = respuestas+"\nEnviando mensaje de vuelta al cliente"
	                connection.sendall(data)
	            else:
	            	respuestas = respuestas+"\nNo hay más datos\n\n\n"
	                break
	             
	    finally:
	        # Cerrando conexion
	        connection.close()

def iniciarThread():
	if __name__ == "__main__":
	    global thread 
	    thread = Thread(target = iniciarServidor, args = ( ))
	    thread.start()
	    print "thread finished...exiting"


def actualizarMensajes():	
	EntryRespuestaServer.config(state=NORMAL)
	EntryRespuestaServer.delete(1.0, END)
	EntryRespuestaServer.insert(END, respuestas)
	EntryRespuestaServer.config(state=DISABLED)	
	root.after(1000,actualizarMensajes)

def cerrar():
	global exitThread
	global respuestas
	exitThread = True
	respuestas=""
	EntryRespuestaServer.config(state=NORMAL)
	EntryRespuestaServer.delete(1.0, END)
	EntryRespuestaServer.insert(END, "")
	EntryRespuestaServer.config(state=DISABLED)	


#inicio de la interfaz grafica
root = Tk()#indica en inicio de loop
ContentPuerto=StringVar()

root.title("Socket Cliente-Servidor Python")#titulo de la ventana
root.geometry("500x450")#tamaño de la ventana
root.config(bg = "#000066")#color azul de background

separador1 = LabelFrame(root,height=30, bg="#16EE67", text="TP2 - Johan Durán & Kenneth Calvo - Universidad De Costa Rica")#crea un espacio - separador
separador1.pack(fill="both")

LabelPuerto = Label(root, text="Puerto")
LabelPuerto.pack(side=TOP,fill="both")

EntryPuerto = Entry(root, bd =5,textvariable=ContentPuerto)
EntryPuerto.pack(fill="both",side=TOP)

separador2 = LabelFrame(root,height=10, bg="#16EE67")#crea un espacio - separador
separador2.pack(fill="both")

btnSubmit = Button(root,text="Iniciar", bg="#B2B3E8", command=iniciarThread)
btnSubmit.pack(fill="both",side=TOP)

separador4 = LabelFrame(root,height=30, bg="#16EE67")#crea un espacio - separador
separador4.pack(fill="both")

btnSubmit = Button(root,text="Desconectar", bg="#B2B3E8", command=cerrar)
btnSubmit.pack(fill="both",side=TOP)

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