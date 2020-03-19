#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 09:30:19 2020

@author: bridget
"""
import sys

from tablero import Tablero
from jugador import Jugador


class InvalidOption(Exception):
    def __init__(self):
        super().__init__("No es una opción válida")


class Ajedrez: #Ajedrez
    """Despliega el menu de inicio para el usuario en la terminal, y espera entrada de teclado"""
    def __init__(self):
        self.tablero  = Tablero() # Composición
        #self.jugador  = Jugador() # Asociación
        self.opciones = {
            "1" : self.iniciarpartida,
            "2" : self.elegirtablero,
            "3" : self.salir_app,
            #"4" : self.inicializarjugadores
        }

    def desplegar1(self):
        print("""
        Inicia una partida de AJEDREZ
        Selecciona la opcion deseada:
            1. Iniciar nuevo juego.
            2. Seleccionar color del tablero.
            3. Salir del juego.
            """)# 4. Ingresa el nombre de los jugadores.)
        #self.tablero.generartab()

    def run(self):
        """Desplegar el menu y esperar la seleccion del usuario"""
        while(True):
            self.desplegar1()
            opcion = input("""\nIntroduce la opcion deseada: """)
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                try:
                    raise InvalidOption()
                except InvalidOption:
                    print("Opcion Inválida")

#No funciona bien la excepción para salir si se agrega try y except se necesita reiniciar el kernel para volver  a comenzar, no sale del menú, además no marca el error solo impime lo que hay en el except, no se puede quitar el while o no permanece el menú, se se queda así sale el error pero tambien sale del menú

    def elegirtablero(self):
        """Elegir el tablero"""
        self.tablero.elegirtab()
        #self.tablero.iniciar()


    def iniciarpartida(self):
        """Inicia un nuevo Juego"""
        self.tablero.generartab()
        self.tablero.inicializartab()
        #self.tablero.seleccionar()


    def salir_app(self):
        print("""Gracias por jugar Ajedrez, regresa pronto dude!""")
        sys.exit()

if __name__ == '__main__':
    Ajedrez().run()



#%%

#python3 -m http.server 8080
        #Jugador.playerA
