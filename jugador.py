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
        self.turno = ''
        self.playerA = ''
        self.playerB = ''


        #self.winner = None

    def nombrar (self):
        """Método para pedir el nombre de los jugadores """
        self.playerA = input("\nPor favor, \ningresa el nombre del jugador A:")
        self.playerB = input("\nPor favor, \ningresa el nombre del jugador B:")
        print("\n{} tus piezas son las Blancas".format(self.playerA))
        print("\n{} tus piezas son las Negras\n".format(self.playerB))
        self.turno = self.playerA
        #print('\n{} es tu turno'.format(self.turno))




    def cambiar_turno(self):
        """Método para cambiar el turno"""

        if self.turno == self.playerA:
            print('\n{} es tu turno (Blancas)'.format(self.turno))
            self.turno = self.playerB
        else:
            print('\n{} es tu turno (Negras)'.format(self.turno))
            self.turno = self.playerA

    #def getwinner
