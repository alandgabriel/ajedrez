#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 12:15:06 2020

@author: bridget
"""
import time

class Jugador():
    """Constructor de la clase"""
    def __init__(self):
        self.turno = 'blanc@'
        self.playerA = ''
        self.playerB = ''


        #self.winner = None

    def nombrar (self):
        """Método para pedir el nombre de los jugadores """
        self.playerA = input("\nPor favor, \ningresa el nombre del jugador A:")
        self.playerB = input("\nPor favor, \ningresa el nombre del jugador B:")
        print("\n{} tus piezas son las Blancas".format(self.playerA))
        print("\n{} tus piezas son las Negras\n".format(self.playerB))
        print("\n{} es tu turno (Blancas)".format(self.playerA))
        #print('\n{} es tu turno'.format(self.turno))




    def cambiar_turno(self):
        """Método para cambiar el turno"""

        if self.turno == 'blanc@':
            self.turno = 'negr@'
            print('\n{} es tu turno (Negras)'.format(self.playerB))

        else:
            self.turno = 'blanc@'
            print('\n{} es tu turno (Blancas)'.format(self.playerA))

    #def getwinner
