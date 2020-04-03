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
        self.pieza = Pieza()
        self.clock = pygame.time.Clock()
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
        self.mascara_piezas = [Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook]+8*[Pawn]
        self.pos_blancas = list(zip(list(range(8))+list(range(8)),[0]*8+[1]*8))
        self.pos_negras = list(zip(list(range(8))+list(range(8)),[6]*8+[7]*8))
        self.pixel_blancas = self.pieza.cuadro_pixel(self.pos_blancas)
        self.pixel_negras = self.pieza.cuadro_pixel (self.pos_negras)
        self.seq_surfaces = list (zip (self.pieza.W + self.pieza.B, self.pixel_blancas + self.pixel_negras))
        self.click_pos = ()

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
                self.dibujarpiezas()
                #self.iniciar()

            elif aprob == "n":
                self.elegirtab()
            else:
                try:
                    raise InvalidOption()
                except InvalidOption:
                    print("Opcion Inválida")
                    break

    def dibujarpiezas(self):
        """ Crea las fichas del tablero de juego """
         #col,fila
        self.screen.blits(self.seq_surfaces)
        self.actualizartab()
        self.seleccionar()

    def contartiempo(self):
        """Crea un reloj para controlar el tiempo de cada turno,
        imprime un contador los últimos 10 segundos"""
        self.text = 10, '10'.rjust(3)
        self.font = pygame.font.SysFont("Arial", 60)
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        while True:
            self.counter -= 1
            self.text = str(self.counter).rjust(3) if self.counter > 0 else 'boom!'
            self.screen.blit(self.font.render(self.text, True, (0, 0, 0)), (320- 60 // 2, 320 - 60 // 2))
            pygame.display.flip()

    def ValidSeleccion (self):
        if self.jugador.turno == 'blanc@':   # Blancas
            self.ix_seleccion = [ix for ix,val in enumerate(self.pos_blancas) if val==self.click_pos]
            if self.ix_seleccion != []:
                self.ix_seleccion = self.ix_seleccion[0]
                self.mascara_piezas[self.ix_seleccion]().seleccionada()
            else:
                print ('Selecciona una ficha valida')
        else:       #Negras
            self.ix_seleccion = [ix for ix,val in enumerate(self.pos_negras) if val==self.click_pos]
            if self.ix_seleccion != []:
                self.ix_seleccion = self.ix_seleccion[0]
                self.mascara_piezas[self.ix_seleccion]().seleccionada()
            else:
                print ('Selecciona una ficha valida')



    def seleccionar(self):
        """Con este método puedes elegir piezas del tablero"""
        self.counter, text = 10, '10'.rjust(3)
        self.jugador.nombrar()
        self.orig= 34#580/16
        self.inc = 580/8
        run = True
        seleccion = False     #indica si han seleccionado una ficha
        mousey,mousex = 0, 0  #coordenadas rectangulares del mouse
        while run:
            mouseclick = False   #indica si se ha hecho click
            #pygame.time.delay(100)#?? things is just dont happen super quick, this is kind of like the clock in the game ??
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):## hasta que check mate sea verdadero
                    run = False #sys.exit()
                elif not mouseclick and event.type == MOUSEMOTION:
                    mousey, mousex = event.pos
                elif not mouseclick and event.type == MOUSEBUTTONUP:
                    mousey, mousex = event.pos
                    mousex = math.floor((mousex-self.orig)/self.inc)
                    mousey = math.floor((mousey-self.orig)/self.inc)
                    mouseclick = True
                    if mousey >= 0 and mousey < 8:
                        if mousex >= 0 and mousex < 8:
                            #print('presionaddooo0 en {}'.format(event.pos))
                            #print('presionaddooo0 en {},{}'.format((mousex-self.orig)/self.inc, (mousey-self.orig)/self.inc))
                            self.click_pos = mousey, mousex
                            self.ValidSeleccion()
                            #if click_pos ==

            #self.contartiempo()



            #self.clock.tick(0.3)
            #pygame.draw.rect(self.screen, (0,0,255), (self.Pieza.seleccionar()), (216, 191, 216))
            #self.clock.tick(5)

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
