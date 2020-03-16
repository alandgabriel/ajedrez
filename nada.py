#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 15:53:12 2020

@author: bridget
"""


    #def:
        
#def refresh:
        """[[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]"""
       
       """
       self.tablero[0][0] = Rook(  ('A', 0), "b")
       self.tablero[0][1] = Knight(('B', 1), "b")
       self.tablero[0][2] = Bishop(('C', 2), "b")
       self.tablero[0][3] = Queen(D, 3, "b" )
       self.tablero[0][4] = King(E, 4, "b"  )
       self.tablero[0][5] = Bishop(0, 5, "b")
       self.tablero[0][6] = Knight(0, 6, "b")
       self.tablero[0][7] = Rook(0, 7, "b"  )

       self.tablero[1][0] = Pawn(1, 0, "b")
       self.tablero[1][1] = Pawn(1, 1, "b")
       self.tablero[1][2] = Pawn(1, 2, "b")
       self.tablero[1][3] = Pawn(1, 3, "b")
       self.tablero[1][4] = Pawn(1, 4, "b")
       self.tablero[1][5] = Pawn(1, 5, "b")
       self.tablero[1][6] = Pawn(1, 6, "b")
       self.tablero[1][7] = Pawn(1, 7, "b")

       self.tablero[7][0] = Rook(7, 0, "w"  )
       self.tablero[7][1] = Knight(7, 1, "w")
       self.tablero[7][2] = Bishop(7, 2, "w")
       self.tablero[7][3] = Queen(7, 3, "w" )
       self.tablero[7][4] = King(7, 4, "w"  )
       self.tablero[7][5] = Bishop(7, 5, "w")
       self.tablero[7][6] = Knight(7, 6, "w")
       self.tablero[7][7] = Rook(7, 7, "w"  )

       self.tablero[6][0] = Pawn(6, 0, "w")
       self.tablero[6][1] = Pawn(6, 1, "w")
       self.tablero[6][2] = Pawn(6, 2, "w")
       self.tablero[6][3] = Pawn(6, 3, "w")
       self.tablero[6][4] = Pawn(6, 4, "w")
       self.tablero[6][5] = Pawn(6, 5, "w")
       self.tablero[6][6] = Pawn(6, 6, "w")
       self.tablero[6][7] = Pawn(6, 7, "w")
    """
    #def update = 
    self.tablero[0][0] = Rook(0, 0, "b"  )
        self.tablero[0][1] = Knight(0, 1, "b")
        self.tablero[0][2] = Bishop(0, 2, "b")
        self.tablero[0][3] = Queen(0, 3, "b" )
        self.tablero[0][4] = King(0, 4, "b"  )
        self.tablero[0][5] = Bishop(0, 5, "b")
        self.tablero[0][6] = Knight(0, 6, "b")
        self.tablero[0][7] = Rook(0, 7, "b"  )
        
        self.tablero[1][0] = Pawn(1, 0, "b")
        self.tablero[1][1] = Pawn(1, 1, "b")
        self.tablero[1][2] = Pawn(1, 2, "b")
        self.tablero[1][3] = Pawn(1, 3, "b")
        self.tablero[1][4] = Pawn(1, 4, "b")
        self.tablero[1][5] = Pawn(1, 5, "b")
        self.tablero[1][6] = Pawn(1, 6, "b")
        self.tablero[1][7] = Pawn(1, 7, "b")

        self.tablero[7][0] = Rook(7, 0,   "w")
        self.tablero[7][1] = Knight(7, 1, "w")
        self.tablero[7][2] = Bishop(7, 2, "w")
        self.tablero[7][3] = Queen(7, 3,  "w")
        self.tablero[7][4] = King(7, 4,   "w")
        self.tablero[7][5] = Bishop(7, 5, "w")
        self.tablero[7][6] = Knight(7, 6, "w")
        self.tablero[7][7] = Rook(7, 7,   "w")
        
        self.tablero[6][0] = Pawn(6, 0, "w")
        self.tablero[6][1] = Pawn(6, 1, "w")
        self.tablero[6][2] = Pawn(6, 2, "w")
        self.tablero[6][3] = Pawn(6, 3, "w")
        self.tablero[6][4] = Pawn(6, 4, "w")
        self.tablero[6][5] = Pawn(6, 5, "w")
        self.tablero[6][6] = Pawn(6, 6, "w")
        self.tablero[6][7] = Pawn(6, 7, "w")
          
          self.tablero =  [[0 for x in range(8)] for y in range(8)]
          #self.tablero =  [(x, y) for x in range(self.cols) for y in range(self.rows)]
    
#%%
"""Aquí se cargan las imágenes que representarán las piezas utilizando pygame"""
"""
b_alfil   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img/black_bishop.png'))
b_rey     = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img/black_king.png'  ))
b_caballo = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img/black_knight.png'))
b_peon    = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img/black_pawn.png'  ))
b_reina   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img/black_queen.png' ))
b_torre   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img/black_rook.png'  ))

w_alfil   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img/white_bishop.png'))
w_rey     = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img/white_king.png'  ))
w_caballo = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img/white_knight.png'))
w_peon    = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img/white_pawn.png'  ))
w_reina   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img/white_queen.png' ))
w_torre   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img/white_rook.png'  ))
"""
"""Se obtiene una lista de las imágenes"""
#Surface objects

b = [b_alfil, b_rey, b_caballo, b_peon, b_reina, b_torre]
w = [w_alfil, w_rey, w_caballo, w_peon, w_reina, w_torre]

"""Se hace una comprehensionlist de las imágenes escaladas"""
B = [pygame.transform.scale(img, (55, 55)) for img in b]
W = [pygame.transform.scale(img, (55, 55)) for img in w]
#%%
"""     
if isinstance(x[1], int)== True :
    print ("entero")
else:
   print(ord(x[1])-65)
 win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess Game")
menu_screen(win, name) partida





#%%
# cambia el color de relleno de la pantalla o surface
fill_color = (0, 130, 200)
screen.fill(fill_color)
pygame.display.flip()

#pygame.draw.rect(screen, (255, 0,0 ), (x, y, width, height))
#pygame.display.update() #refresh


        self.b_alfil   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/blackb.png'))
        self.b_rey     = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/blackk.png'))
        self.b_caballo = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/blackn.png'))
        self.b_peon    = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/blackp.png'))
        self.b_reina   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/blackq.png'))
        self.b_torre   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/blackr.png'))
        
        self.w_alfil   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/whiteb.png'))
        self.w_rey     = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/whitek.png'))
        self.w_caballo = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/whiten.png'))
        self.w_peon    = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/whitep.png'))
        self.w_reina   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/whiteq.png'))
        self.w_torre   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/whiter.png'))
        
        """Se obtiene una lista de las imágenes"""
        #Surface objects
        b = [self.b_alfil, self.b_rey, self.b_caballo, self.b_peon, self.b_reina, self.b_torre]
        w = [self.w_alfil, self.w_rey, self.w_caballo, self.w_peon, self.w_reina, self.w_torre]
        
        """Se hace una comprehensionlist de las imágenes escaladas"""
        B = [pygame.transform.scale(img, (self.width, self.height)) for img in b]
        W = [pygame.transform.scale(img, (self.width, self.height)) for img in w]
        """
        
#pygame.sprite.Sprite #Simple base class for visible game objects.
#%%

"""Otras imágenes"""



#b_alfil   = pygame.image.load(os.path.join("img1","BlackBishop.png"))
"""b_alfil   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/BlackBishop.png'))
b_rey     = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/BlackKing.png'  ))
b_caballo = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/BlackKnight.png'))
b_peon    = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/BlackPawn.png'  ))
b_reina   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/BlackQueen.png' ))
b_torre   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/BlackRook.png'  ))

w_alfil   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/WhiteBishop.png'))
w_rey     = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/WhiteKing.png'  ))
w_caballo = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/WhiteKnight.png'))
w_peon    = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/WhitePawn.png'  ))
w_reina   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/WhiteQueen.png' ))
w_torre   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/WhiteRook.png'  ))
"""
    #%% Jugador
 #       self.turno = self.playerA # Inicializa el turno con el jugador A 
 import numpy as np
 import matplotlib.pyplot as plt
 
 chessboard = np.zeros((8,8))
 chessboard[1::2, 0::2] = 1
 chessboard[0::2, 1::2] = 1
 
 plt.imshow(chessboard, cmap = 'binary')
 plt.show
#%%
 
        screen.blit(B[5], (x, y))
        screen.blit(B[2], (x+increment, y))
        screen.blit(B[0], (x+2*increment, y))
        screen.blit(B[1], (x+3*increment, y))
        screen.blit(B[4], (x+4*increment, y))
        screen.blit(B[0], (x+5*increment, y))
        screen.blit(B[2], (x+6*increment, y))
        screen.blit(B[5], (x+7*increment, y))
        
        screen.blit(B[3], (x, y+increment))
        screen.blit(B[3], (x+increment, y+increment))
        screen.blit(B[3], (x+2*increment, y+increment))
        screen.blit(B[3], (x+3*increment, y+increment))
        screen.blit(B[3], (x+4*increment, y+increment))
        screen.blit(B[3], (x+5*increment, y+increment))
        screen.blit(B[3], (x+6*increment, y+increment))
        screen.blit(B[3], (x+7*increment, y+increment))
        
        screen.blit(W[5], (x, y+7*increment))
        screen.blit(W[2], (x+increment, y+7*increment))
        screen.blit(W[0], (x+2*increment, y+7*increment))
        screen.blit(W[1], (x+3*increment, y+7*increment))
        screen.blit(W[4], (x+4*increment, y+7*increment))
        screen.blit(W[0], (x+5*increment, y+7*increment))
        screen.blit(W[2], (x+6*increment, y+7*increment))
        screen.blit(W[5], (x+7*increment, y+7*increment))
        
        screen.blit(W[3], (x, y+6*increment))
        screen.blit(W[3], (x+increment, y+6*increment))
        screen.blit(W[3], (x+2*increment, y+6*increment))
        screen.blit(W[3], (x+3*increment, y+6*increment))
        screen.blit(W[3], (x+4*increment, y+6*increment))
        screen.blit(W[3], (x+5*increment, y+6*increment))
        screen.blit(W[3], (x+6*increment, y+6*increment))
        screen.blit(W[3], (x+7*increment, y+6*increment))

  #%%
        
import matplotlib.pyplot as plt
import numpy as np

# Make a 9x9 grid...
nrows, ncols = 9,9
image = np.zeros(nrows*ncols)

# Set every other cell to a random number (this would be your data)
image[::2] = np.random.random(nrows*ncols//2 + 1)

# Reshape things into a 9x9 grid.
image = image.reshape((nrows, ncols))

row_labels = range(1,nrows+1)
col_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
plt.matshow(image)
plt.xticks(range(ncols), col_labels)
plt.yticks(range(nrows), row_labels)
plt.show()
#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas 
from matplotlib.table import Table

def main():
    data = pandas.DataFrame(np.random.random((8,8)), 
                columns=['A','B','C','D','E','F','G','H'])
    checkerboard_table(data)
    plt.show()

def checkerboard_table(data, fmt='{:.2f}', bkg_colors=['black', 'white']):
    fig, ax = plt.subplots()
    ax.set_axis_off()
    tb = Table(ax, bbox=[0,0,1,1])

    nrows, ncols = data.shape
    width, height = 1.0 / ncols, 1.0 / nrows

    # Add cells
    for (i,j), val in np.ndenumerate(data):
        # Index either the first or second item of bkg_colors based on
        # a checker board pattern
        idx = [j % 2, (j + 1) % 2][i % 2]
        color = bkg_colors[idx]

        tb.add_cell(i, j, width, height, text=fmt.format(val), 
                    loc='center', facecolor=color)

    # Row Labels...
    for i, label in enumerate(data.index+1): #data.index+1
        tb.add_cell(i, -1, width, height, text=label, loc='right', 
                    edgecolor='none', facecolor='none')
    # Column Labels...
    for j, label in enumerate(data.columns):
        tb.add_cell(-1, j, width, height/2, text=label, loc='center', 
                           edgecolor='none', facecolor='none')
    ax.add_table(tb)
    return fig

if __name__ == '__main__':
    main()
    
    
    
    #%%
    
    
    

import pygame
import os
from pygame import image
from pygame.transform import scale
from pygame.locals import *


class Imagen():
    """"Clase que incluye las imgágenes de las piezas que se usarán al programa"""
    def __init__(self):
        self.width = 65
        self.height= 65
        self.B = []
        self.W = []
        
    def importar(self):
        """Aquí se cargan las imágenes que representarán las piezas utilizando pygame"""
        b_alfil   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/blackb.png'))
        b_rey     = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/blackk.png'))
        b_caballo = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/blackn.png'))
        b_peon    = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/blackp.png'))
        b_reina   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/blackq.png'))
        b_torre   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/blackr.png'))
        
        w_alfil   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/whiteb.png'))
        w_rey     = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/whitek.png'))
        w_caballo = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/whiten.png'))
        w_peon    = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/whitep.png'))
        w_reina   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/whiteq.png'))
        w_torre   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/whiter.png'))
                
        """Se obtiene una lista de las imágenes"""
        #Surface objects
        b = [b_alfil, b_rey, b_caballo, b_peon, b_reina, b_torre]
        w = [w_alfil, w_rey, w_caballo, w_peon, w_reina, w_torre]
        
        """Se hace una comprehensionlist de las imágenes escaladas"""
        self.B = [pygame.transform.scale(img, (self.width, self.height)) for img in b]
        self.W = [pygame.transform.scale(img, (self.width, self.height)) for img in w]

        
        """Se hacen transparentes los bordes de las imágenes
        en una lista"""
        
        self.B = [img.convert_alpha() for img in self.B]
        self.W = [img.convert_alpha() for img in self.W]
        return self.B, self.W

class Pieza:
    """Clase piezas"""
    def __init__(self, pos, color):
        self.row= pos[1]
        self.col =pos[0]
        self.color = color
        #self.img = self.img
        self.selected = False
        self.B, self.W = Imagen().importar() #lista de imagenes
        
        self.movelist = []

        self.x = (640-60) / 16
        self.y = (640-60) / 16
        self.width =65
        self.height=65
        self.increment = (640-60) / 8 
    
    def dibujar(self,img): #color w y
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
        xpositioni = 33
        ypositioni = 33
        print("\nPresiona las flechas para mover el recuadro y colócalo en la posición de la pieza que deseas mover, cuando termines presiona la barra espaciadora\n")
        run = True
        p = False
        while run:
            pygame.time.delay(100)#?? things is just dont happen super quick, this is kind of like the clock in the game ??
            for event in pygame.event.get():
                if event.type == pygame.QUIT:## hasta que check mate sea verdadero
                    run = False #sys.exit()
            
                keys = pygame.key.get_pressed()
                
                
                if keys[pygame.K_LEFT] and xpositioni > 30 + width:
                    xpositioni-=increment
                if keys[pygame.K_RIGHT] and xpositioni < 640 - width -increment:
                    xpositioni+=increment
                if keys[pygame.K_UP] and ypositioni > increment:
                    ypositioni-=increment
                if keys[pygame.K_DOWN] and ypositioni < 640 - height - increment: 
                    ypositioni+=increment
                
                # Dibuja la superficie con la posicion de las "Surface" sobre la ventana
                #screen.fill((0,0,0))
                screen.blit(fondo, (0, 0)) #col fila
                pygame.draw.rect(screen, (0,0,255), (xpositioni, ypositioni, increment, increment), (216, 191, 216))
                #pygame.draw.rect(screen, (255, 0,0 ), (33, 33, increment, increment)) #(x, y, width, height)) tamaño del rectángulo para la posición
                # pygame.draw.rect(screen, (255, 0,0 ), (30, 30, SCREEN_WIDTH-60, SCREEN_HEIGHT-60)) #(x, y, width, height)) tamaño del rectángulo central del ajedrez para limitar el mov de la pieza
                
        
                screen.blit(tB, (x, y)) ## debe llamar a todas las piezas con su posición actual
                pygame.display.update() # allows to update a portion of the screen, instead of the entire area of the screen. Passing no arguments, updates the entire display
                if keys[pygame.K_SPACE]:
                    pass
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


 
    def validarmovimientos(self, tablero):#lista de movimientos
        self.movelist = self.valid_moves(tablero)
        
    
    
    def cambiarpos (self): #actualiza la posición
        self.row = posición[0]
        self.col = posición[1]



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
        
    
    
    """PIEZA"""
    

import pygame
import os
from pygame import image
from pygame.transform import scale

from pygame.locals import *


b_alfil   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/blackb.png'))
b_rey     = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/blackk.png'))
b_caballo = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/blackn.png'))
b_peon    = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/blackp.png'))
b_reina   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/blackq.png'))
b_torre   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/blackr.png'))

w_alfil   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/whiteb.png'))
w_rey     = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/whitek.png'))
w_caballo = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/whiten.png'))
w_peon    = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/whitep.png'))
w_reina   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/whiteq.png'))
w_torre   = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/img1/whiter.png'))
        
"""Se obtiene una lista de las imágenes"""
#Surface objects
b = [b_alfil, b_rey, b_caballo, b_peon, b_reina, b_torre]
w = [w_alfil, w_rey, w_caballo, w_peon, w_reina, w_torre]

"""Se hace una comprehensionlist de las imágenes escaladas"""
B = [pygame.transform.scale(img, (65, 65)) for img in b]
W = [pygame.transform.scale(img, (65, 65)) for img in w]

"""Se hacen transparentes los bordes de las imágenes
B = [img.convert_alpha() for img in B]
W = [img.convert_alpha() for img in W]
"""

#%%
#SISIRVE

#import sys

# -----------
# Constantes
# -----------
# Atributos de la pantalla
pygame.init() 
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640

#Atributos del tablero
#xposition = 0
#yposition = 0
#width =
#height=
#velocity = 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ajedrez")

#atributos de la figura /pieza (inicializar)
x = (SCREEN_WIDTH-60) / 16
y = (SCREEN_HEIGHT-60) / 16
width =65
height=65
increment = (SCREEN_WIDTH-60) / 8 #increment
#velocity = 


#Atributos del tablero
#xposition = 0
#yposition = 0
#widthtab  = SCREEN_WIDTH 
#heighttab =SCREEN_HEIGHT

#xpositioni = 30
#ypositioni = 30
#widthtabint  = SCREEN_WIDTH - 2*xposition 
#heighttabint =SCREEN_HEIGHT - 2*xposition

#cargar las imágenes usamos pygame.image.load(), con ello se crea un objeto que contiene la superficie de la imagen (aun no la muestra). 
fondo = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/tableros/tablero-marron-notacion.png'  )).convert()
tor = b_peon.convert_alpha()

#modificar tamaño
fondo = pygame.transform.scale(fondo, (640, 640))
tB = pygame.transform.scale(tor, (width, height))



run = True
while run:
    pygame.time.delay(100)#?? things is just dont happen super quick, this is kind of like the clock in the game ??
    for event in pygame.event.get():
        if event.type == pygame.QUIT:## hasta que check mate sea verdadero
            run = False #sys.exit()
    
        keys = pygame.key.get_pressed()
        
        
        if keys[pygame.K_LEFT] and x > 30 + width:
            x-=increment
        if keys[pygame.K_RIGHT] and x < 640 - width -increment:
            x+=increment
        if keys[pygame.K_UP] and y > increment:
            y-=increment
        if keys[pygame.K_DOWN] and y < 640 - height - increment: 
            y+=increment
        
        # Dibuja la superficie con la posicion de las "Surface" sobre la ventana
        #screen.fill((0,0,0))
        screen.blit(fondo, (0, 0)) #col fila
        pygame.draw.rect(screen, (255, 0,0 ), (33, 33, increment, increment)) #(x, y, width, height)) tamaño del rectángulo para la posición
        # pygame.draw.rect(screen, (255, 0,0 ), (30, 30, SCREEN_WIDTH-60, SCREEN_HEIGHT-60)) #(x, y, width, height)) tamaño del rectángulo central del ajedrez para limitar el mov de la pieza
        screen.blit(tB, (x, y))
        pygame.display.update() # allows to update a portion of the screen, instead of the entire area of the screen. Passing no arguments, updates the entire display
        #pygame.display.flip() # will update the contents of the entire display
            
pygame.quit()




#%%

from pygame.locals import *
#import sys

# -----------
# Constantes
# -----------
# Atributos de la pantalla

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640

"""MOVERPIEZA"""
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ajedrez")



#atributos de la figura /pieza (inicializar)
x = (SCREEN_WIDTH-60) / 16
y = (SCREEN_HEIGHT-60) / 16
width =65
height=65
increment = (SCREEN_WIDTH-60) / 8 #increment

#Atributos del tablero
xposition = 0
yposition = 0
widthtab  = SCREEN_WIDTH 
heighttab =SCREEN_HEIGHT

xpositioni = 33
ypositioni = 33
#widthtabint  = SCREEN_WIDTH - 2*xposition 
#heighttabint =SCREEN_HEIGHT - 2*xposition

#cargar las imágenes usamos pygame.image.load(), con ello se crea un objeto que contiene la superficie de la imagen (aun no la muestra). 
fondo = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/tableros/tablero-marron-notacion.png'  )).convert()
tor = b_peon.convert_alpha()

#modificar tamaño
fondo = pygame.transform.scale(fondo, (widthtab, heighttab))
tB = pygame.transform.scale(tor, (width, height))

"""mover pieza"""

run = True
while run:
    pygame.time.delay(100)#?? things is just dont happen super quick, this is kind of like the clock in the game ??
    for event in pygame.event.get():
        if event.type == pygame.QUIT:## hasta que check mate sea verdadero
            run = False #sys.exit()
    
        keys = pygame.key.get_pressed()
        
        
        if keys[pygame.K_LEFT] and x > 30 + width:
            x-=increment
        if keys[pygame.K_RIGHT] and x < 640 - width -increment:
            x+=increment
        if keys[pygame.K_UP] and y > increment:
            y-=increment
        if keys[pygame.K_DOWN] and y < 640 - height - increment: 
            y+=increment
        
        # Dibuja la superficie con la posicion de las "Surface" sobre la ventana
        #screen.fill((0,0,0))
        screen.blit(fondo, (0, 0)) #col fila
        pygame.draw.rect(screen, (0,0,255), (xpositioni, ypositioni, increment, increment), 1)
        #pygame.draw.rect(screen, (255, 0,0 ), (33, 33, increment, increment)) #(x, y, width, height)) tamaño del rectángulo para la posición
        # pygame.draw.rect(screen, (255, 0,0 ), (30, 30, SCREEN_WIDTH-60, SCREEN_HEIGHT-60)) #(x, y, width, height)) tamaño del rectángulo central del ajedrez para limitar el mov de la pieza
        screen.blit(tB, (x, y))
        pygame.display.update() # allows to update a portion of the screen, instead of the entire area of the screen. Passing no arguments, updates the entire display
        #pygame.display.flip() # will update the contents of the entire display
        
pygame.quit()"""
#%%






# esto es lo que va a estar en tablero
#img = Imagen()
B, W = Imagen().importar()

#x3 = Bishop((0,0), "w").dibujar()
#x4 = Pieza((0,0), "w").dibujar()
# Atributos de la pantalla
pygame.init() 
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640

#Atributos del tablero
xposition = 0
yposition = 0
widthtab  = SCREEN_WIDTH 
heighttab =SCREEN_HEIGHT




xpositioni = 33
ypositioni = 33
#widthtabint  = (SCREEN_WIDTH - 2*xposition) /8
#heighttabint = (SCREEN_HEIGHT - 2*xposition)/8


#atributos de la figura /pieza (inicializar)
x = (SCREEN_WIDTH-60) / 16
y = (SCREEN_HEIGHT-60) / 16
width =65
height=65
increment = (SCREEN_WIDTH-60) / 8 #increment
#velocity = 


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ajedrez")

#cargar las imágenes usamos pygame.image.load(), con ello se crea un objeto que contiene la superficie de la imagen (aun no la muestra). 
fondo = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/tableros/tablero-marron-notacion.png'  )).convert()
fondo = pygame.transform.scale(fondo, (widthtab, heighttab))


"""seleccionar pieza"""
print("\nPresiona las flechas para mover el recuadro y colócalo en la posición de la pieza que deseas mover, cuando termines presiona la barra espaciadora\n")
#pygame.init()
run = True
while run:
    pygame.time.delay(100)#?? things is just dont happen super quick, this is kind of like the clock in the game ??
    for event in pygame.event.get():
        if event.type == pygame.QUIT:## hasta que check mate sea verdadero
            run = False #sys.exit()
    
        keys = pygame.key.get_pressed()
        
        
        if keys[pygame.K_LEFT] and xpositioni > 30 + width:
            xpositioni-=increment
        if keys[pygame.K_RIGHT] and xpositioni < 640 - width -increment:
            xpositioni+=increment
        if keys[pygame.K_UP] and ypositioni > increment:
            ypositioni-=increment
        if keys[pygame.K_DOWN] and ypositioni < 640 - height - increment: 
            ypositioni+=increment
        
        # Dibuja la superficie con la posicion de las "Surface" sobre la ventana
        #screen.fill((0,0,0))
        screen.blit(fondo, (0, 0)) #col fila
        pygame.draw.rect(screen, (220, 20, 60), (xpositioni, ypositioni, increment, increment))
        #pygame.draw.rect(screen, (255, 0,0 ), (33, 33, increment, increment)) #(x, y, width, height)) tamaño del rectángulo para la posición
        # pygame.draw.rect(screen, (255, 0,0 ), (30, 30, SCREEN_WIDTH-60, SCREEN_HEIGHT-60)) #(x, y, width, height)) tamaño del rectángulo central del ajedrez para limitar el mov de la pieza
        
        screen.blit (Bishop((0,0), "w").dibujar()[0],
                    Bishop((0,0), "w").dibujar()[1])
        print(Bishop((0,0), "w").dibujar()[0],
                    Bishop((0,0), "w").dibujar()[1])
        
        """screen.blit(B[5], (x, y))
        screen.blit(B[2], (x+increment, y))
        screen.blit(B[0], (x+2*increment, y))
        screen.blit(B[1], (x+3*increment, y))
        screen.blit(B[4], (x+4*increment, y))
        screen.blit(B[0], (x+5*increment, y))
        screen.blit(B[2], (x+6*increment, y))
        screen.blit(B[5], (x+7*increment, y))
        
        screen.blit(B[3], (x, y+increment))
        screen.blit(B[3], (x+increment, y+increment))
        screen.blit(B[3], (x+2*increment, y+increment))
        screen.blit(B[3], (x+3*increment, y+increment))
        screen.blit(B[3], (x+4*increment, y+increment))
        screen.blit(B[3], (x+5*increment, y+increment))
        screen.blit(B[3], (x+6*increment, y+increment))
        screen.blit(B[3], (x+7*increment, y+increment))
        
        screen.blit(W[5], (x, y+7*increment))
        screen.blit(W[2], (x+increment, y+7*increment))
        screen.blit(W[0], (x+2*increment, y+7*increment))
        screen.blit(W[1], (x+3*increment, y+7*increment))
        screen.blit(W[4], (x+4*increment, y+7*increment))
        screen.blit(W[0], (x+5*increment, y+7*increment)) 
        screen.blit(W[2], (x+6*increment, y+7*increment))
        screen.blit(W[5], (x+7*increment, y+7*increment))
        
        screen.blit(W[3], (x, y+6*increment))
        screen.blit(W[3], (x+increment, y+6*increment))
        screen.blit(W[3], (x+2*increment, y+6*increment))
        screen.blit(W[3], (x+3*increment, y+6*increment))
        screen.blit(W[3], (x+4*increment, y+6*increment))
        screen.blit(W[3], (x+5*increment, y+6*increment))
        screen.blit(W[3], (x+6*increment, y+6*increment))
        screen.blit(W[3], (x+7*increment, y+6*increment))"""

        pygame.display.update() # allows to update a portion of the screen, instead of the entire area of the screen. Passing no arguments, updates the entire display
        #pygame.display.flip() # will update the contents of the entire display
pygame.quit()

#Atributos del tablero
#xposition = 0
#yposition = 0
#widthtab  = SCREEN_WIDTH 
#heighttab =SCREEN_HEIGHT

#xpositioni = 30
#ypositioni = 30
#widthtabint  = SCREEN_WIDTH - 2*xposition 
#heighttabint =SCREEN_HEIGHT - 2*xposition
#%%
screen.blit(B[5], (x, y))
screen.blit(B[2], (x+increment, y))
#%%

"""SELECCINAR PIEZA"""


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ajedrez")



#atributos de la figura /pieza (inicializar)
x = (SCREEN_WIDTH-60) / 16
y = (SCREEN_HEIGHT-60) / 16
width =65
height=65
increment = (SCREEN_WIDTH-60) / 8 #increment

#Atributos del tablero
xposition = 0
yposition = 0
widthtab  = SCREEN_WIDTH 
heighttab =SCREEN_HEIGHT

xpositioni = 33
ypositioni = 33
#widthtabint  = (SCREEN_WIDTH - 2*xposition) /8
#heighttabint = (SCREEN_HEIGHT - 2*xposition)/8

#cargar las imágenes usamos pygame.image.load(), con ello se crea un objeto que contiene la superficie de la imagen (aun no la muestra). 
fondo = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/tableros/tablero-marron-notacion.png'  )).convert()
tor = b_peon.convert_alpha()

#modificar tamaño
fondo = pygame.transform.scale(fondo, (widthtab, heighttab))
tB = pygame.transform.scale(tor, (width, height))

"""seleccionar pieza"""
print("\nPresiona las flechas para mover el recuadro y colócalo en la posición de la pieza que deseas mover, cuando termines presiona la barra espaciadora\n")

run = True
while run:
    pygame.time.delay(100)#?? things is just dont happen super quick, this is kind of like the clock in the game ??
    for event in pygame.event.get():
        if event.type == pygame.QUIT:## hasta que check mate sea verdadero
            run = False #sys.exit()
    
        keys = pygame.key.get_pressed()
        
        
        if keys[pygame.K_LEFT] and xpositioni > 30 + width:
            xpositioni-=increment
        if keys[pygame.K_RIGHT] and xpositioni < 640 - width -increment:
            xpositioni+=increment
        if keys[pygame.K_UP] and ypositioni > increment:
            ypositioni-=increment
        if keys[pygame.K_DOWN] and ypositioni < 640 - height - increment: 
            ypositioni+=increment
        
        # Dibuja la superficie con la posicion de las "Surface" sobre la ventana
        #screen.fill((0,0,0))
        screen.blit(fondo, (0, 0)) #col fila
        pygame.draw.rect(screen, (220, 20, 60), (xpositioni, ypositioni, increment, increment))
        #pygame.draw.rect(screen, (255, 0,0 ), (33, 33, increment, increment)) #(x, y, width, height)) tamaño del rectángulo para la posición
        # pygame.draw.rect(screen, (255, 0,0 ), (30, 30, SCREEN_WIDTH-60, SCREEN_HEIGHT-60)) #(x, y, width, height)) tamaño del rectángulo central del ajedrez para limitar el mov de la pieza
        
        
        screen.blit(B[5], (x, y))
        screen.blit(B[2], (x+increment, y))
        screen.blit(B[0], (x+2*increment, y))
        screen.blit(B[4], (x+3*increment, y))
        screen.blit(B[1], (x+4*increment, y))
        screen.blit(B[0], (x+5*increment, y))
        screen.blit(B[2], (x+6*increment, y))
        screen.blit(B[5], (x+7*increment, y))
        
        screen.blit(B[3], (x, y+increment))
        screen.blit(B[3], (x+increment, y+increment))
        screen.blit(B[3], (x+2*increment, y+increment))
        screen.blit(B[3], (x+3*increment, y+increment))
        screen.blit(B[3], (x+4*increment, y+increment))
        screen.blit(B[3], (x+5*increment, y+increment))
        screen.blit(B[3], (x+6*increment, y+increment))
        screen.blit(B[3], (x+7*increment, y+increment))
        
        screen.blit(W[5], (x, y+7*increment))
        screen.blit(W[2], (x+increment, y+7*increment))
        screen.blit(W[0], (x+2*increment, y+7*increment))
        screen.blit(W[4], (x+3*increment, y+7*increment))
        screen.blit(W[1], (x+4*increment, y+7*increment))
        screen.blit(W[0], (x+5*increment, y+7*increment)) 
        screen.blit(W[2], (x+6*increment, y+7*increment))
        screen.blit(W[5], (x+7*increment, y+7*increment))
        
        screen.blit(W[3], (x, y+6*increment))
        screen.blit(W[3], (x+increment, y+6*increment))
        screen.blit(W[3], (x+2*increment, y+6*increment))
        screen.blit(W[3], (x+3*increment, y+6*increment))
        screen.blit(W[3], (x+4*increment, y+6*increment))
        screen.blit(W[3], (x+5*increment, y+6*increment))
        screen.blit(W[3], (x+6*increment, y+6*increment))
        screen.blit(W[3], (x+7*increment, y+6*increment))

        pygame.display.update() # allows to update a portion of the screen, instead of the entire area of the screen. Passing no arguments, updates the entire display
        #pygame.display.flip() # will update the contents of the entire display
pygame.quit()
#%%
vel = increment = SCREEN_WIDTH-60 / 8
#%%


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ajedrez")



#atributos de la figura /pieza (inicializar)
x = (SCREEN_WIDTH-60) / 16
y = (SCREEN_HEIGHT-60) / 16
width =65
height=65
increment = (SCREEN_WIDTH-60) / 8 #increment

#Atributos del tablero
xposition = 0
yposition = 0
widthtab  = SCREEN_WIDTH 
heighttab =SCREEN_HEIGHT
#Atributos del recuadro
xpositioni = 33
ypositioni = 33
#widthtabint  = (SCREEN_WIDTH - 2*xposition) /8
#heighttabint = (SCREEN_HEIGHT - 2*xposition)/8

#cargar las imágenes usamos pygame.image.load(), con ello se crea un objeto que contiene la superficie de la imagen (aun no la muestra). 
fondo = pygame.image.load(os.path.join('/home/bridget/Downloads/Trimestre19O/POO/Ajedrez/tableros/tablero-marron-notacion.png'  )).convert()
tor = b_peon.convert_alpha()

#modificar tamaño
fondo = pygame.transform.scale(fondo, (widthtab, heighttab))
tB = pygame.transform.scale(tor, (width, height))


"""seleccionar pieza y moverla"""
print("\nPresiona las flechas para mover el recuadro y colócalo en la posición de la pieza que deseas mover, cuando termines presiona la barra espaciadora\n")
run = True
p = False
while run:
   
    pygame.time.delay(100)#?? things is just dont happen super quick, this is kind of like the clock in the game ??
    for event in pygame.event.get():
        if event.type == pygame.QUIT:## hasta que check mate sea verdadero
            run = False #sys.exit()
    
        keys = pygame.key.get_pressed()
        
        #print("\nPresiona las flechas para mover el recuadro y colócalo en la posición de la pieza que deseas mover, cuando termines presiona la barra espaciadora\n")
        if keys[pygame.K_LEFT] and xpositioni > 30 + width:
            xpositioni-=increment
        if keys[pygame.K_RIGHT] and xpositioni < 640 - width -increment:
            xpositioni+=increment
        if keys[pygame.K_UP] and ypositioni > increment:
            ypositioni-=increment
        if keys[pygame.K_DOWN] and ypositioni < 640 - height - increment: 
            ypositioni+=increment
        
        # Dibuja la superficie con la posicion de las "Surface" sobre la ventana
        #screen.fill((0,0,0))
        screen.blit(fondo, (0, 0)) #col fila
        pygame.draw.rect(screen, (0,0,255), (xpositioni, ypositioni, increment, increment), 1)
        #pygame.draw.rect(screen, (255, 0,0 ), (33, 33, increment, increment)) #(x, y, width, height)) tamaño del rectángulo para la posición
        # pygame.draw.rect(screen, (255, 0,0 ), (30, 30, SCREEN_WIDTH-60, SCREEN_HEIGHT-60)) #(x, y, width, height)) tamaño del rectángulo central del ajedrez para limitar el mov de la pieza
        screen.blit(tB, (x, y))
        pygame.display.update() # allows to update a portion of the screen, instead of the entire area of the screen. Passing no arguments, updates the entire display
        
        #pygame.display.flip() # will update the contents of the entire display
        if keys[pygame.K_SPACE]:
           # print("\n AAAAAAAAAAaaPresiona las flechas para mover el recuadro y colócalo en la posición de la pieza que deseas mover, cuando termines presiona la barra espaciadora\n")

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
                    p = False
                    if p == False:
                        
                # Dibuja la superficie con la posicion de las "Surface" sobre la ventana
                #screen.fill((0,0,0))
                screen.blit(fondo, (0, 0)) #col fila
                #pygame.draw.rect(screen, (0,0,255), (xpositioni, ypositioni, increment, increment), 1)
                #pygame.draw.rect(screen, (255, 0,0 ), (33, 33, increment, increment)) #(x, y, width, height)) tamaño del rectángulo para la posición
                # pygame.draw.rect(screen, (255, 0,0 ), (30, 30, SCREEN_WIDTH-60, SCREEN_HEIGHT-60)) #(x, y, width, height)) tamaño del rectángulo central del ajedrez para limitar el mov de la pieza
                screen.blit(tB, (x, y))
                pygame.display.update() # allows to update a portion of the screen, instead of the entire area of the screen. Passing no arguments, updates the entire display
                #pygame.display.flip() # will update the contents of the entire display
                
            
pygame.quit()
#K_KP_ENTER

#%%
#sustituir codigo por un byte conocido,
# hardware uart en vez de software uart





#%%


#%%


