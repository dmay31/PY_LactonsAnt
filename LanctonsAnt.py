#Lancton's ANT
#CopyRight Ben and Dale May 2020

from tkinter import *
import time

WIDTH  = 100
HEIGHT = 100
SQUARE_SIDE = 8
WHITE  = 'white'
BLACK  = 'black'
UP     = 100
LEFT   = 200
DOWN   = 300
RIGHT  = 400

class Square:
    def __init__(self, canvas, x_index=0, y_index=0, color=WHITE):
        self.canvas = canvas
        self.x = x_index * SQUARE_SIDE
        self.y = y_index * SQUARE_SIDE
        self.color = color
        self.dir = UP

        
        self.r = self.canvas.create_rectangle(self.x, self.y, self.x+SQUARE_SIDE, self.y+SQUARE_SIDE,
             fill=color, width=1)

    def changeColor(self, color ):
        canvas.itemconfigure( self.r, fill=color )
        self.color = color

    def swapColor( self ):
        if( self.color == WHITE ):
            self.color = BLACK
        elif( self.color == BLACK ):
            self.color = WHITE
            
        canvas.itemconfigure( self.r, fill=self.color )

    def getColor(self):
        return self.color


class Ant:
    def __init__(self, canvas, x_index, y_index ):
        self.canvas = canvas
        self.dir = UP
        
        diameter = SQUARE_SIDE / 2
        self.x = x_index * SQUARE_SIDE + diameter/2
        self.y = y_index * SQUARE_SIDE + diameter/2

        self.c = canvas.create_oval( self.x, self.y, self.x+diameter, self.y+diameter, fill='red')

    def move( self, x,y ):
        print( self.c )
        self.canvas.move(self.c, x*SQUARE_SIDE,y*SQUARE_SIDE)

    def moveForward( self ):
        x = 0
        y = 0
        if( self.dir == UP ):
            x = -SQUARE_SIDE
        elif( self.dir == RIGHT ):
            y = SQUARE_SIDE
        elif( self.dir == DOWN ):
            x = SQUARE_SIDE
        elif( self.dir == LEFT ):
            y = -SQUARE_SIDE
        else:
            pass

        sX,sY = self.getSquare()
        if( sX < HEIGHT-1 and sY < WIDTH-1 and sX > 0 and sY > 0 ):
            self.canvas.move( self.c, x, y )
            return True
        else:
            return False

    def turn( self, dir ):
        if( dir == RIGHT ):
            if( self.dir == UP ):
                self.dir = RIGHT
            elif( self.dir == RIGHT ):
                self.dir = DOWN
            elif( self.dir == DOWN ):
                self.dir = LEFT
            elif( self.dir == LEFT ):
                self.dir = UP
            else:
                pass
        if( dir == LEFT ):
            if( self.dir == UP ):
                self.dir = LEFT
            elif( self.dir == LEFT ):
                self.dir = DOWN
            elif( self.dir == DOWN ):
                self.dir = RIGHT
            elif( self.dir == RIGHT ):
                self.dir = UP
            else:
                pass

    def turnByColor( self, squareMap ):
        x,y = self.getSquare()
        aSquare = squareMap[x][y]
        squareColor = aSquare.getColor()

        if( squareColor == WHITE ):
            self.turn( LEFT )
        elif( squareColor == BLACK):
            self.turn( RIGHT )
        else:
            print( "Don't know that color!" )

        return aSquare
            

    def getSquare( self ):
        pos = self.canvas.coords( self.c )
        x = int((pos[1]-(SQUARE_SIDE/4))/SQUARE_SIDE)
        y = int((pos[0]-(SQUARE_SIDE/4))/SQUARE_SIDE)
        return x,y
        
        


tk = Tk()
tk.title("lanctons ant")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

windowWidth = (WIDTH*SQUARE_SIDE)
windowHeight = (HEIGHT*SQUARE_SIDE)
canvas = Canvas(tk, width=windowWidth, height=windowHeight, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

theSquares = []

for j in range(0,WIDTH):
    row = []
    for i in range(0,HEIGHT):     
        row.append( Square(canvas, i, j, WHITE) )
    theSquares.append( row )

cx = int(WIDTH/2)
cy = int(HEIGHT/2)-10
theAnt = Ant(canvas, cx,cy)
#theSquares[50][50].changeColor('black')

num = 1

while 1:
    result = theAnt.moveForward()
    if( not result ):
        print("Reached the edge of the screen!")
        break;
    
    theSquare = theAnt.turnByColor( theSquares )
    theSquare.swapColor()

    #print("Iteration: %d" % num )
              
    tk.update_idletasks()
    tk.update()
    #time.sleep(1)
    num = num + 1
      

    

