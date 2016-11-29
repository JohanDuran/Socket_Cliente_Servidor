#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Programa Cliente
# Fuente original de este codigo: www.pythondiario.com
# Utilizado para fines academicos en el curso CI-1320 

import socket
import sys
from Tkinter import *
def conectarServidor(): 
	# Creando un socket TCP/IP
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	 
	# Conecta el socket en el puerto cuando el servidor esté escuchando
	server_address = ('localhost', int(ContentPuerto.get()))
	print >>sys.stderr, 'conectando a %s puerto %s' % server_address
	sock.connect(server_address)

	try: 
	     
	    # Enviando datos
	    message = ContentMensaje.get()
	    print >>sys.stderr, 'enviando "%s"' % message
	    sock.sendall(message)
	 
	    # Buscando respuesta
	    amount_received = 0
	    amount_expected = len(message)
	    data="" 
	    while amount_received < amount_expected:
	        data = data+sock.recv(19)
	        amount_received += len(data)
	        print >>sys.stderr, 'recibiendo "%s"' % data
	 	ContentRespuestaServidor.set(data)
	 	ContentMensaje.set("")
	finally:
	    print >>sys.stderr, 'cerrando socket'
	    sock.close()

#inicio de la interfaz grafica
root = Tk()#indica en inicio de loop
ContentRespuestaServidor=StringVar()
ContentPuerto=StringVar()
ContentMensaje=StringVar()


ContentRespuestaServidor.set("Esperando respuesta del servidor")
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

LabelMensajeEnviar = Label(root, text="Mensaje")
LabelMensajeEnviar.pack(side=TOP,fill="both")

EntryMensajeEnviar = Entry(root, bd =5,textvariable=ContentMensaje)
EntryMensajeEnviar.pack(fill="both",side=TOP)

separador3 = LabelFrame(root,height=10, bg="#16EE67")#crea un espacio - separador
separador3.pack(fill="both")

btnSubmit = Button(root,text="Conectar", bg="#B2B3E8", command=conectarServidor)
btnSubmit.pack(fill="both",side=TOP)

separador4 = LabelFrame(root,height=30, bg="#16EE67")#crea un espacio - separador
separador4.pack(fill="both")

LabelRespuesta = Label(root, text="Respuesta del servidor")
LabelRespuesta.pack(side=TOP,fill="both")

EntryRespuestaServer = Entry(root, bd =5,textvariable=ContentRespuestaServidor)
EntryRespuestaServer.pack(fill="both",side=TOP)
EntryRespuestaServer.config(state="readonly")

root.mainloop()#llama el loop