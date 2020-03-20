#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:35:33 2020

@author: bridget
"""


import pygame
import os
from pygame import image
from pygame.transform import scale
from pygame.locals import *
import numpy as np

class Imagen():
    """"Clase que incluye las imgágenes de las piezas que se usarán al programa"""
    def __init__(self):
        self.width = 65
        self.height= 65
        self.B = []
        self.W = []

    def importar(self):
        """Aquí se cargan las imágenes que representarán las piezas utilizando pygame"""
        b_alfil   = pygame.image.load(os.path.join('img1/blackb.png'))
        b_rey     = pygame.image.load(os.path.join('img1/blackk.png'))
        b_caballo = pygame.image.load(os.path.join('img1/blackn.png'))
        b_peon    = pygame.image.load(os.path.join('img1/blackp.png'))
        b_reina   = pygame.image.load(os.path.join('img1/blackq.png'))
        b_torre   = pygame.image.load(os.path.join('img1/blackr.png'))

        w_alfil   = pygame.image.load(os.path.join('img1/whiteb.png'))
        w_rey     = pygame.image.load(os.path.join('img1/whitek.png'))
        w_caballo = pygame.image.load(os.path.join('img1/whiten.png'))
        w_peon    = pygame.image.load(os.path.join('img1/whitep.png'))
        w_reina   = pygame.image.load(os.path.join('img1/whiteq.png'))
        w_torre   = pygame.image.load(os.path.join('img1/whiter.png'))

        """Se obtiene una lista de las imágenes"""
        #Surface objects
        b = [b_torre, b_caballo, b_alfil, b_rey, b_reina, b_alfil, b_caballo, b_torre]+8*[b_peon]
        w = [w_torre, w_caballo, w_alfil, w_reina, w_rey, w_alfil, w_caballo, w_torre]+8*[w_peon]
        #b = [b_torre, b_caballo, b_alfil, b_rey, b_reina, b_alfil, b_caballo, b_torre]+8*[b_peon]
        #w = [w_torre, w_caballo, w_alfil, w_reina, w_rey, w_alfil, w_caballo, w_torre]+8*[w_peon]

        """Se hace una comprehensionlist de las imágenes escaladas"""
        self.B = [pygame.transform.scale(img, (self.width, self.height)) for img in b]
        self.W = [pygame.transform.scale(img, (self.width, self.height)) for img in w]


        """Se hacen transparentes los bordes de las imágenes
        en una lista"""

        #self.B = [img.convert_alpha() for img in self.B]
        #self.W = [img.convert_alpha() for img in self.W]
        return self.B, self.W


"""Definición de las excepciones que se van a usar"""

class InvalidPiece(Exception):
    pass
class InvalidColor(Exception):
    pass
class InvalidMovement(Exception):
    pass

class Pieza:
    """Clase piezas"""
    def __init__(self):
        #self.sqr   = pos
        #self.row   = pos[1]
        #self.col   = pos[0]
        #self.color = color
        #self.img = self.img
        #self.selected = False
        self.B, self.W = Imagen().importar() #lista de imagenes
        self.movelist = []

        self.x = 34#(640-60) / 16
        self.y = 34#(640-60) / 16
        self.width =65
        self.height=65
        self.increment = (640-60) / 8

    def cuadro_pixel(self,pos): #color w y
        """Con este método se convierten los cuadros a pixeles en el tablero"""
        self.row= [x[1] for x in pos]
        self.col = [x[0] for x in pos]
        self.row= list( np.array(self.row)*self.increment + self.x)
        self.col = list(np.array(self.col)*self.increment + self.y)
        pos_pixel = list (zip(self.col,self.row))
        return pos_pixel

    def validarmovimientos(self):#lista de movimientos
        #self.movelist = self.valid_moves(tablero)
        return self.movelist





    def dibujar(self,img): #color w y
        """Con este método se dibujan las piezas en el tablero"""
        self.img = img
        if self.color == "w":
            self.forma = self.W[self.img] #self.img atributo por sobreescribir
        else:
            self.forma = self.B[self.img]

        self.row= self.row*self.increment + self.x
        self.col = self.col*self.increment + self.y
        return self.forma, (self.col,self.row)

    def seleccionar1(self):
        return self.selected

    def seleccionar(self):
        #Atributos del recuadro
        self.xpositioni = 33
        self.ypositioni = 33
        print("\nPresiona las flechas para mover el recuadro y colócalo en la posición de la pieza que deseas mover, cuando termines presiona la barra espaciadora\n")
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.xpositioni > 30 + self.width:
            self.xpositioni-=self.increment
        if keys[pygame.K_RIGHT] and self.xpositioni < 640 - self.width -self.increment:
            self.xpositioni+=self.increment
        if keys[pygame.K_UP] and self.ypositioni > self.increment:
            self.ypositioni-=self.increment
        if keys[pygame.K_DOWN] and self.ypositioni < 640 - self.height - self.increment:
            self.ypositioni+=self.increment

        # Dibuja la superficie con la posicion de las "Surface" sobre la ventana
        #return (self.xpositioni, self.ypositioni, self.increment, self.increment) #screen.fill((0,0,0))
        #screen.blit(fondo, (0, 0)) #col fila
        pygame.draw.rect(screen, (0,0,255), (self.xpositioni, self.ypositioni, self.increment, self.increment), (216, 191, 216))
        #pygame.draw.rect(screen, (255, 0,0 ), (33, 33, increment, increment)) #(x, y, width, height)) tamaño del rectángulo para la posición
        # pygame.draw.rect(screen, (255, 0,0 ), (30, 30, SCREEN_WIDTH-60, SCREEN_HEIGHT-60)) #(x, y, width, height)) tamaño del rectángulo central del ajedrez para limitar el mov de la pieza
        #screen.blit(tB, (x, y)) ## debe llamar a todas las piezas con su posición actual
        #pygame.display.update() # allows to update a portion of the screen, instead of the entire area of the screen. Passing no arguments, updates the entire display
        #if keys[pygame.K_SPACE]:
        #    pass
            #si es del color del jugador en turno seleccionar True                   self.mover()
            #self.posición = (row,col)
    def mover(self):
        p = True
        while p:
            if keys[pygame.K_LEFT] and x > 30 + width:
                x-=increment
            if keys[pygame.K_RIGHT] and x < 640 - width -increment:
                x+=increment
            if keys[pygame.K_UP] and y > increment:
                y-=increment
                if keys[pygame.K_DOWN] and y < 640 - height - increment:
                    y+=increment
                if keys[pygame.K_SPACE]:
                    try:
                        #if no hay nadie cambiarposicion, if hay alguien ver si puede comerse y luego cambair pos P False
                        p = False
                    except:
                        raise InvalidMovement
                # Dibuja la superficie con la posicion de las "Surface" sobre la ventana
                #screen.fill((0,0,0))
                screen.blit(fondo, (0, 0)) #col fila

                screen.blit(tB, (x, y)) ## debe llamar a todas las piezas con su posición actual tablero?

                pygame.display.update() # allows to update a portion of the screen, instead of the entire area of the screen. Passing no arguments, updates the entire display
                #pygame.display.flip() # will update the contents of the entire display



    def cambiarpos (self): #actualiza la posición
        self.row = posición[0]
        self.col = posición[1]


# Polimorfismo en cada pieza

class Bishop(Pieza):
    def __init__(self, pos, color):
        super().__init__(pos, color)
    def validarmovimientos(self):

        return super().dibujar(self.img)
class King (Pieza):
    def __init__(self, pos, color):
        super().__init__(pos, color)
    def validarmovimientos(self):
        return super().dibujar(self.img)
class Rook (Pieza):
    def __init__(self, pos, color):
        super().__init__(pos, color)
    def validarmovimientos(self):
        return super().dibujar(self.img)
class Pawn (Pieza):
    def __init__(self, pos, color):
        super().__init__(pos, color)
    def validar_espacio(self):
        pass
    def validarmovimientos(self):
        if self.color == "w":
            if self.row == 1: #Permite mover doble cuadro al frente si es el primer movimiento
                self.movelist.append(self.col, self.row+2)
                self.movelist.append(self.col, self.row+1)
            else:
                if validarespacio():
                    None


        else:
            if self.row == 6: #Permite mover doble cuadro al frente si es el primer movimiento
                self.movelist.append(self.col, self.row-1)
                self.movelist.append(self.col, self.row-2)
        return super().dibujar(self.img)
class Queen(Pieza):
    def __init__(self, pos, color):
        super().__init__(pos, color)
    def validarmovimientos(self):
        return super().dibujar(self.img)
class Knight(Pieza):
    def __init__(self, pos, color):
        super().__init__(pos, color)
    def validarmovimientosr(self):
        return super().dibujar(self.img)
#%%







# Polimorfismo en cada pieza

class Bishop(Pieza):
    def __init__(self, pos, color):
        self.img = 0
        super().__init__(pos, color)
    def dibujar(self):
        return super().dibujar(self.img)
class King (Pieza):
    def __init__(self, pos, color):
        self.img = 1
        super().__init__(pos, color)
    def dibujar(self):
        return super().dibujar(self.img)
class Rook (Pieza):
    def __init__(self, pos, color):
        self.img = 5
        super().__init__(pos, color)
    def dibujar(self):
        return super().dibujar(self.img)
class Pawn (Pieza):
    def __init__(self, pos, color):
        self.img = 3
        super().__init__(pos, color)
    def dibujar(self):
        return super().dibujar(self.img)
class Queen(Pieza):
    def __init__(self, pos, color):
        self.img = 4
        super().__init__(pos, color)
    def dibujar(self):
        return super().dibujar(self.img)
class Knight(Pieza):
    def __init__(self, pos, color):
        self.img = 2
        super().__init__(pos, color)
    def dibujar(self):
        return super().dibujar(self.img)
#%%
