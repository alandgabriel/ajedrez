#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 12:15:06 2020

@author: bridget
"""

class Jugador():
    """Constructor de la clase"""
    def __init__(self):
        self.color   = ('white', 'black')
        #self.turno = self.playerA# = self.nombrar_jugadores()
        #self.playerB = self.nombrar_jugadores()
        #self.turno   = self.playerA 
        #self.winner = None
        
    def nombrar_jugadores(self):
        self.playerA = input("\nPor favor, \ningresa el nombre del jugador A:")
        self.playerB = input("\nPor favor, \ningresa el nombre del jugador B:")
        playera = (self.color[0], self.playerA )
        playerb = (self.color[1], self.playerB )
        print("\n{} tus piezas son las Blancas".format(self.playerA))
        print("\n{} tus piezas son las Negras\n".format(self.playerB))
        return self.playerA, self.playerB
    
    def cambiar_turno(self):
        """Método para cambiar el turno"""
        if self.turno == self.playerA:
            self.turno = self.playerB
        else:
            self.turno = self.playerA
        return self.turno
    
    #def getwinner
