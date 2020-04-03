#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 07:22:41 2020

@author: alan
"""
from Jugador import jugador

"""
class Pieza:
    """Clase piezas"""
    def __init__(self):
        #self.sqr   = pos
        #self.row   = pos[1]
        #self.col   = pos[0]
        #self.color = color
        #self.img = self.img
        #self.selected = False
        self.x = 34#(640-60) / 16
        self.y = 34#(640-60) / 16
        self.width =65
        self.height=65
        self.increment = (640-60) / 8

class Bishop(Pieza):
    def __init__(self):
        super().__init__()
    def seleccionada(self):
        print('bishop')

class King (Pieza):
    def __init__(self):
        super().__init__()
    def seleccionada(self):
        print ('king')
class Rook (Pieza):
    def __init__(self):
        super().__init__()
    def seleccionada(self):
        print('rook')

class Pawn (Pieza):
    def __init__(self):
        super().__init__()
    def seleccionada(self):
        print('pawn')

    
class Queen(Pieza):
    def __init__(self):
        super().__init__()
    def seleccionada(self):
        print('queen')

class Knight(Pieza):
    def __init__(self):
        super().__init__()
    def seleccionada(self):
        print('knight')"""
        


mascara_piezas = [Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook]+8*[Pawn]
pos_blancas = list(zip(list(range(8))+list(range(8)),[0]*8+[1]*8))
pos_negras = list(zip(list(range(8))+list(range(8)),[6]*8+[7]*8))
pos_actual = (0,0)
ix_ficha = [ix for ix,val in enumerate(pos_blancas) if val==pos_actual]
if ix_ficha!=[]:
    mascara_piezas[0]().seleccionada()
    