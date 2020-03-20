#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 04:57:08 2020

@author: bridget
"""

import sys
from pieza import *

from jugador import Jugador

import pygame
import os
from pygame import image
from pygame.transform import scale
from pygame.locals import *

import random
from random import randrange, choice
 #importa todas las clases
import math


class InvalidColor(Exception):
    pass
class InvalidOption(Exception):
    pass

class Tablero:
    def __init__(self):
        """Aquí se inicializan los atributos del tablero y de la pantalla de pygame que lo contiene"""
        self.jugador  = Jugador()
        self.SCREEN_WIDTH= 640
        self.widthtab = 640
        self.SCREEN_HEIGHT= 640
        self.heighttab = 640
        self.xposition = 0
        self.yposition = 0
        self.tableros = ['tableros/tablero-azul-notacion.png'   ,
                         'tableros/tablero-gris-notacion.png'   ,
                         'tableros/tablero-marron-notacion.png' ,
                         'tableros/tablero-naranja-notacion.png',
                         'tableros/tablero-negro-notacion.png'  ,
                         'tableros/tablero-rojo-notacion.png'   ,
                         'tableros/tablero-verde-notacion.png'  ,
                         'tableros/tablero-violeta-notacion.png']
        #pygame.init()
        self.opciones = {
            "1" : 0,#self.tableros[0],
            "2" : 1,#self.tableros[1],
            "3" : 2,#self.tableros[2],
            "4" : 3,#self.tableros[3],
            "5" : 4,#self.tableros[4],
            "6" : 5,#self.tableros[5],
            "7" : 6,#self.tableros[6],
            "8" : 7#self.tableros[7]
        }
    def desplegar(self):
        """Despliega el menú de opciones para los colores del tablero"""
        print(self.opciones)
        print("""\n Elige el color de tu tablero:
            1. Azul
            2. Gris
            3. Marrón
            4. Naranja
            5. Negro
            6. Rojo
            7. Verde
            8. Violeta""")
    def elegirtab(self):
        while(True):
            self.desplegar()
            opcion1 = input("\nIntroduce la opcion deseada: ")
            opcion = self.opciones.get(opcion1)
            if opcion:
                self.generartab(opcion)
                self.aprobartab()
            else:
                try:
                    raise InvalidColor()
                except InvalidColor:
                    print("Opcion Inválida")#print("{} no es una opcion valida".format(opcion))#
                    y = False

    def generartab(self, fondo = random.randint(0,7)):



        pygame.init()
        self.fondo = pygame.image.load((self.tableros[fondo]))######
        #print(self.fondo)
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Ajedrez")
        self.tab = pygame.transform.scale(self.fondo, (self.widthtab, self.heighttab))
        self.screen.blit(self.tab, (self.xposition, self.yposition))
        #print("hola")
        self.actualizartab()
        #self.quitar()


    def aprobartab(self):

        y = True
        while y:
            aprob = input("\n ¿Te gustó el color? [y/n]")
            if aprob == "y":
                self.inicializartab()
                #self.iniciar()

            elif aprob == "n":
                self.elegirtab()
            else:
                try:
                    raise InvalidOption()
                except InvalidOption:
                    print("Opcion Inválida")
                    break

    def inicializartab(self):
        """ Crea las fichas del tablero de juego """

         #col fila
        #self.generartab(self.fondo)
        self.screen.blit (Rook((0,0), "w").dibujar()[0],
                    Rook((0,0), "w").dibujar()[1])
        self.screen.blit (Knight((1,0), "w").dibujar()[0],
                    Knight((1,0), "w").dibujar()[1])
        self.screen.blit (Bishop((2,0), "w").dibujar()[0],
                    Bishop((2,0), "w").dibujar()[1])
        self.screen.blit (King((3,0), "w").dibujar()[0],
                    King((3,0), "w").dibujar()[1])
        self.screen.blit (Queen((4,0), "w").dibujar()[0],
                    Queen((4,0), "w").dibujar()[1])
        self.screen.blit (Bishop((5,0), "w").dibujar()[0],
                    Bishop((5,0), "w").dibujar()[1])
        self.screen.blit (Knight((6,0), "w").dibujar()[0],
                    Knight((6,0), "w").dibujar()[1])
        self.screen.blit (Rook((7,0), "w").dibujar()[0],
                    Rook((7,0), "w").dibujar()[1])

        self.screen.blit (Pawn((0,1), "w").dibujar()[0],
                    Pawn((0,1), "w").dibujar()[1])
        self.screen.blit (Pawn((1,1), "w").dibujar()[0],
                    Pawn((1,1), "w").dibujar()[1])
        self.screen.blit (Pawn((2,1), "w").dibujar()[0],
                    Pawn((2,1), "w").dibujar()[1])
        self.screen.blit (Pawn((3,1), "w").dibujar()[0],
                    Pawn((3,1), "w").dibujar()[1])
        self.screen.blit (Pawn((4,1), "w").dibujar()[0],
                    Pawn((4,1), "w").dibujar()[1])
        self.screen.blit (Pawn((5,1), "w").dibujar()[0],
                    Pawn((5,1), "w").dibujar()[1])
        self.screen.blit (Pawn((6,1), "w").dibujar()[0],
                    Pawn((6,1), "w").dibujar()[1])
        self.screen.blit (Pawn((7,1), "w").dibujar()[0],
                    Pawn((7,1), "w").dibujar()[1])

        self.screen.blit (Pawn((0,6), "b").dibujar()[0],
                    Pawn((0,6), "b").dibujar()[1])
        self.screen.blit (Pawn((1,6), "b").dibujar()[0],
                    Pawn((1,6), "b").dibujar()[1])
        self.screen.blit (Pawn((2,6), "b").dibujar()[0],
                    Pawn((2,6), "b").dibujar()[1])
        self.screen.blit (Pawn((3,6), "b").dibujar()[0],
                    Pawn((3,6), "b").dibujar()[1])
        self.screen.blit (Pawn((4,6), "b").dibujar()[0],
                    Pawn((4,6), "b").dibujar()[1])
        self.screen.blit (Pawn((5,6), "b").dibujar()[0],
                    Pawn((5,6), "b").dibujar()[1])
        self.screen.blit (Pawn((6,6), "b").dibujar()[0],
                    Pawn((6,6), "b").dibujar()[1])
        self.screen.blit (Pawn((7,6), "b").dibujar()[0],
                    Pawn((7,6), "b").dibujar()[1])


        self.screen.blit (Rook((0,7), "b").dibujar()[0],
                    Rook((0,7), "b").dibujar()[1])
        self.screen.blit (Knight((1,7), "b").dibujar()[0],
                    Knight((1,7), "b").dibujar()[1])
        self.screen.blit (Bishop((2,7), "b").dibujar()[0],
                    Bishop((2,7), "b").dibujar()[1])
        self.screen.blit (King((3,7), "b").dibujar()[0],
                    King((3,7), "b").dibujar()[1])
        self.screen.blit (Queen((4,7), "b").dibujar()[0],
                    Queen((4,7), "b").dibujar()[1])
        self.screen.blit (Bishop((5,7), "b").dibujar()[0],
                    Bishop((5,7), "b").dibujar()[1])
        self.screen.blit (Knight((6,7), "b").dibujar()[0],
                    Knight((6,7), "b").dibujar()[1])
        self.screen.blit (Rook((7,7), "b").dibujar()[0],
                    Rook((7,7), "b").dibujar()[1])

        self.actualizartab()
        self.seleccionar()


        #self.quitar()
        #funciona raro, si viene de el menu normal se sale al menú del ajedrez on el x o con n en la pregunta si quiere jugar, si viene de elegir tablero con n marca error, exit regresa a preguntar error: display Surface quit si quiere iniciar un nuevo juego

    def seleccionar(self):
        self.jugador.nombrar()
        self.orig= 34#580/16
        self.inc = 580/8
        run = True
        seleccion = False       #indica si han seleccionado una ficha
        mousex,mousey = 0, 0        #coordenadas rectangulares del mouse
        while run:
            mouseclick = False   #indica si se ha hecho click
            pygame.time.delay(100)#?? things is just dont happen super quick, this is kind of like the clock in the game ??
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):## hasta que check mate sea verdadero
                    run = False #sys.exit()
                elif not mouseclick and event.type == MOUSEMOTION:
                    mousex, mousey = event.pos
                elif not mouseclick and event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    mouseclick = True
                    print('presionaddooo0 en {}'.format(event.pos))
                    print('presionaddooo0 en {},{}'.format((mousex-self.orig)/self.inc, (mousey-self.orig)/self.inc))
                    print('presionaddooo0 en {},{}'.format(math.floor((mousex-self.orig)/self.inc), math.floor((mousey-self.orig)/self.inc)))

                #pygame.draw.rect(self.screen, (0,0,255), (self.Pieza.seleccionar()), (216, 191, 216))
                self.actualizartab()
        self.quitar()

    def actualizartab(self):
        pygame.display.update()

    def quitar(self):
        pygame.quit()
        sys.exit()
#%%
#tablero = Tablero()
#tablero.elegirtab()

#%%
