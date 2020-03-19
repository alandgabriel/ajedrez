#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 12:15:06 2020

@author: bridget
"""

class Jugador():
    """Constructor de la clase"""
    def __init__(self):
        self.turno = ''
        self.playerA = ''
        self.playerB = ''
        #self.winner = None

    def nombrar (self):
        self.playerA = input("\nPor favor, \ningresa el nombre del jugador A:")
        self.playerB = input("\nPor favor, \ningresa el nombre del jugador B:")
        print("\n{} tus piezas son las Blancas".format(self.playerA))
        print("\n{} tus piezas son las Negras\n".format(self.playerB))
        self.turno = self.playerA
        print('\n{} es tu turno'.format(self.turno))




    def cambiar_turno(self):
        """Método para cambiar el turno"""
        if self.turno == self.playerA:
            self.turno = self.playerB
            print('\n{} es tu turno'.format(self.turno))
        else:
            self.turno = self.playerA
            print('\n{} es tu turno'.format(self.turno))

    #def getwinner
