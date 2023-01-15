"""
______________________________

Fernando Daniel Monroy Sánchez
A01750536

Chess Game with features
______________________________
"""


import turtle as t
import copy

def initialize():
    # Draw chess board, pieces and assign save their location
    draw.board(themes[theme][0])
    draw.bpieces()
    attachPieceLocationMatrix()
    attachPieceMovesMatrix()
    t.update()  # Show the chess board once it is drawn


class draw:
# Class for all the drawing methods

    def bframe(color):
        # Draws the frame of the chess board given the color. Used in draw.board()
        bdrw.color(color)
        bdrw.seth(90)
        for i in range(4):
            bdrw.begin_fill()
            for j in range(2):
                bdrw.fd(wdw[1]*(1/36))
                bdrw.right(90)
                bdrw.fd(wdw[1]*(8/9+1/36))
                bdrw.right(90)
            bdrw.end_fill()
            bdrw.right(90)
            bdrw.fd(wdw[1]*(8/9))
        # You have to t.update() manually


    def bsqr(color, drawer):
        # Draws the square starting from its bottom left vertex given the color. Used in draw.board()
        # Size is 1/9 x 1/9 of the window's height
        drawer.color(color)
        drawer.seth(0)
        drawer.pu()
        drawer.begin_fill()  # No need to pen down
        for i in range(4):
            drawer.fd(wdw[1]*(1/9))  # 1/9 of the window's height
            drawer.lt(90)
        drawer.end_fill()
        # Process how it will draw:
        # Bottom left --> right --> top --> left --> bottom left
        

    def bpieces():
        # Draws the initial location of all pieces on the board. Used in initialize()
        # More info in drawers list
        for i in range(len(drawers)):  # For each team of white / black
            for j in range(len(drawers[i])):  # For each piece type in every team
                for k in range(len(drawers[i][j])):  # For each individual piece in each piece type
                    drawers[i][j][k][0] = t.Turtle()  # The first item in the individual piece list will be the drawer
                    drawers[i][j][k][0].ht()  # Hide turtle
                    drawers[i][j][k][0].speed(-1)  # Instantaneous drawing
                    drawers[i][j][k][0].pen(pencolor="#000000")  # Black pen stroke
                    if i == 0: offset = 1  # When the piece is a pawn it is drawn 1 row further from the edge (2 and 7)
                    else: offset = -1  # Any other piece is drawn in the edge row (1 and 8)
                    # Draw each piece according to its type, using the column information in the 2nd item of the individual piece list
                    if j == 0: draw.pawn(drawers[i][j][k][0], corners[i][0] + wdw[1]*(drawers[i][j][k][1]/9), corners[i][1] + (wdw[1]*(2/9))*offset, team[i])
                    if j == 1: draw.knight(drawers[i][j][k][0], corners[i][0] + wdw[1]*(drawers[i][j][k][1]/9), corners[i][1] + (wdw[1]*(1/9))*offset, team[i])
                    elif j == 2: draw.bishop(drawers[i][j][k][0], corners[i][0] + wdw[1]*(drawers[i][j][k][1]/9), corners[i][1] + (wdw[1]*(1/9))*offset, team[i])
                    elif j == 3: draw.rook(drawers[i][j][k][0], corners[i][0] + wdw[1]*(drawers[i][j][k][1]/9), corners[i][1] + (wdw[1]*(1/9))*offset, team[i])
                    elif j == 4: draw.queen(drawers[i][j][k][0], corners[i][0] + wdw[1]*(drawers[i][j][k][1]/9), corners[i][1] + (wdw[1]*(1/9))*offset, team[i])
                    elif j == 5: draw.king(drawers[i][j][k][0], corners[i][0] + wdw[1]*(drawers[i][j][k][1]/9), corners[i][1] + (wdw[1]*(1/9))*offset, team[i])


    def board(theme):
        # Draws the entire board. Used in initialized()

        # ------- Settings --------
        bdrw.pu()  # Pen up
        bdrw.speed(-1)  # Instant drawings
        bdrw.setpos(corners[0][0]+(wdw[1]*(1/18)), corners[0][1]+(wdw[1]*(1/18)))
        # Get to the bottom down corner coordinates and get 1/9% apart from them when 100% is the window's height
        # -------------------------
        
        for i in range(1, 9):
            # The rows from 1 to 8
            if i % 2 == 0: pattern = range(2, 10)  # The pattern for rows 1, 3, 5, and 7 will be a dark starting square  
            else: pattern = range(1, 9)  # and 2, 4, 6, and 8 will start with a light square
            
            for j in pattern:
                # The columns from a to h. If pattern starts in an even number then it will start with a light square, odd = start dark.
                if j % 2 == 0:
                    draw.bsqr(theme[0], bdrw)  # Draw light square
                else:
                    draw.bsqr(theme[1], bdrw)  # Draw dark square
                bdrw.fd(wdw[1]*(1/9))  # Go to the bottom right square corner to be ready to draw the next square
            # When you finish drawing a row get ready to draw the next one by going to the top left corner of the row
            bdrw.left(180)
            bdrw.fd(wdw[1]*(8/9))
            bdrw.right(90)
            bdrw.fd(wdw[1]*(1/9))
        # Calls the frame drawer function using the color theme
        draw.bframe(theme[2])
        

    def pawn(drawer, x, y, color):
        
        center = (x, y)
        
        def startPoint():
            drawer.pu()
            drawer.seth(0)
            drawer.goto(center)
            drawer.fd(wdw[1]*(1/60))
            drawer.lt(90)
            drawer.fd(wdw[1]*(1/60))
        
        def outline():
            drawer.circle(wdw[1]*(1/60), 55, steps)
            drawer.circle(wdw[1]*(1/60), 235, steps)
            drawer.seth(90)
            drawer.circle(wdw[1]*(1/36), -40, steps)
            drawer.right(180)
            drawer.circle(wdw[1]*(1/36), 30, steps)
            drawer.seth(270)
            drawer.fd(wdw[1]*(1/240))
            drawer.seth(345)
            drawer.circle(wdw[1]*(1/12), 30.7, steps)
            drawer.seth(90)
            drawer.fd(wdw[1]*(1/240))
            drawer.seth(100)
            drawer.circle(wdw[1]*(1/36), 30, steps)
            drawer.seth(310)
            drawer.circle(wdw[1]*(1/36), -40, steps)

        
        startPoint()
        drawer.circle(wdw[1]*(1/60), -55, steps)
        drawer.pen(pendown=False, fillcolor=color["dark"])
        drawer.begin_fill()
        outline()
        drawer.end_fill()
        
        startPoint()
        drawer.circle(wdw[1]*(1/60), 90, steps)
        drawer.seth(230)
        drawer.pen(pendown=False, fillcolor=color["light"])
        drawer.begin_fill()
        drawer.circle(wdw[1]*(1/40), 70, steps)
        drawer.seth(90)
        drawer.circle(wdw[1]*(1/20), -20, steps)
        drawer.rt(180)
        drawer.circle(wdw[1]*(1/20), 25, steps)
        drawer.seth(354)
        drawer.circle(wdw[1]*(1/12), 21, steps)
        drawer.seth(90)
        drawer.fd(wdw[1]*(1/240))
        drawer.seth(100)
        drawer.circle(wdw[1]*(1/36), 30, steps)
        drawer.seth(310)
        drawer.circle(wdw[1]*(1/36), -40, steps)
        drawer.seth(35)
        drawer.circle(wdw[1]*(1/60), 145, steps)
        drawer.end_fill()

        startPoint()
        drawer.circle(wdw[1]*(1/60), -55, steps)
        drawer.pen(pendown=True, pensize=(4.5*wdw[1]/720))  # Original pensize for pieces is 5 at 1280x720
        outline()
        drawer.pu()

        # Position difference from beggining and end of drawing:
        # (0.67%, 0.88%)
        
    
    def knight(drawer, x, y, color):
        
        center = (x, y-(wdw[1]*(1/216)))
        
        def startPoint():
            drawer.pu()
            drawer.goto(center)
            drawer.seth(90)
            drawer.fd(wdw[1]*((1/27)-(1/216)))  # 2/3rds up the center of the square


        def outline():
            drawer.fd(wdw[1]*(1/108))
            drawer.lt(75)
            drawer.circle(wdw[1]*(1/10), -10, steps)
            drawer.rt(5)
            drawer.circle(wdw[1]*(1/33), -75, steps)
            drawer.circle(wdw[1]*(1/10), -10, steps)
            drawer.rt(180)
            drawer.circle(wdw[1]*(1/48), 50, steps)
            drawer.seth(20)
            drawer.circle(wdw[1]*(1/12), -35, steps)
            drawer.seth(270)
            drawer.circle(wdw[1]*(1/28), -65, steps)
            drawer.rt(180)
            drawer.circle(wdw[1]*(1/20), 20, steps)
            drawer.seth(45)
            drawer.circle(wdw[1]*(1/60), -60, steps)
            drawer.rt(180)
            drawer.circle(wdw[1]*(1/60), 50, steps)
            drawer.seth(125)
            drawer.fd(wdw[1]*(1/70))
            drawer.goto(center[0], center[1] + wdw[1]*((1/27)-(1/216)))


        startPoint()
        drawer.pen(pendown=False, fillcolor=color["light"])
        drawer.begin_fill()
        outline()
        drawer.end_fill()
        
        startPoint()
        drawer.pen(pendown=False, fillcolor=color["dark"])
        drawer.begin_fill()
        drawer.fd(wdw[1]*(1/108))
        drawer.lt(75)
        drawer.seth(310)
        drawer.fd(wdw[1]*(1/80))
        drawer.rt(180)
        drawer.circle(wdw[1]*(1/175), -100, steps)
        drawer.rt(180)
        drawer.fd(wdw[1]*(1/27))
        drawer.seth(125)
        drawer.fd(wdw[1]*(1/125))
        drawer.goto(center[0], center[1] + wdw[1]*((1/27)-(1/216)))
        drawer.end_fill()

        drawer.pu()
        drawer.goto(center)
        drawer.seth(90)
        drawer.fd(wdw[1]*(1/216))
        drawer.rt(90)
        drawer.fd(wdw[1]*(2/216))
        drawer.seth(235)
        drawer.pen(pendown=False, fillcolor=color["dark"])
        drawer.begin_fill()
        drawer.fd(wdw[1]*((1/50)))
        drawer.circle(wdw[1]*(1/24), 36, steps)
        drawer.seth(357)
        drawer.circle(wdw[1]*(1/12), -11, steps)
        drawer.seth(270)
        drawer.circle(wdw[1]*(1/28), -65, steps)
        drawer.rt(180)
        drawer.circle(wdw[1]*(1/20), 20, steps)
        drawer.end_fill()

        startPoint()
        drawer.pen(pendown=True, pensize=(4.5*wdw[1]/720))
        outline()
        drawer.pu()
        drawer.goto(center)
        drawer.seth(90)
        drawer.fd(wdw[1]*((1/27)-(4/216)))
        drawer.dot((5*wdw[1]/720))
        drawer.goto(center)
        drawer.seth(90)
        drawer.fd(wdw[1]*((1/27)-(1/216)))
        drawer.fd(wdw[1]*(1/108))
        drawer.lt(75)
        drawer.circle(wdw[1]*(1/10), -10, steps)
        drawer.rt(5)
        drawer.circle(wdw[1]*(1/33), -75, steps)
        drawer.circle(wdw[1]*(1/10), -10, steps)
        drawer.rt(180)
        drawer.circle(wdw[1]*(1/48), 15, steps)
        drawer.pd()
        drawer.seth(20)
        drawer.circle(wdw[1]*(1/12), -30, steps)
        drawer.pu()
        
        
    def bishop(drawer, x, y, color):
        
        center = (x, y)
        
        def startPoint():
            drawer.pu()
            drawer.goto(center)
            drawer.seth(90)
            drawer.fd(wdw[1]*(1/36))


        def complementary():
            drawer.seth(259)
            drawer.circle(wdw[1]*(1/40), -23, steps)
            drawer.rt(180)
            drawer.circle(wdw[1]*(1/15), 18, steps)
            drawer.circle(wdw[1]*(1/40), 55, steps)
            drawer.lt(75)
            drawer.circle(wdw[1]*(1/30), 55, steps)
            drawer.seth(274)
            drawer.circle(wdw[1]*(1/19), -38, steps)
            drawer.goto(center[0], center[1]+wdw[1]*(1/36))


        def outline(pendown, pensize, fillcolor):
            startPoint()
            drawer.seth(205)
            drawer.pen(pendown=pendown, pensize=pensize, fillcolor=fillcolor)
            drawer.begin_fill()
            drawer.circle(wdw[1]*(1/15), 23, steps)
            drawer.circle(wdw[1]*(1/40), 55, steps)
            drawer.circle(wdw[1]*(1/15), 18, steps)
            drawer.rt(180)
            drawer.circle(wdw[1]*(1/40), -23, steps)
            drawer.seth(349)
            drawer.circle(wdw[1]*(1/12), 20, steps)
            complementary()
            drawer.pu()
            drawer.end_fill()


        outline(False, None, color["dark"])
        
        startPoint()
        drawer.seth(270)
        drawer.fd(wdw[1]*(1/300))
        drawer.seth(233)
        drawer.pen(pendown=False, fillcolor=color["light"])
        drawer.begin_fill()
        drawer.circle(wdw[1]*(1/15), 25, steps)
        drawer.circle(wdw[1]*(1/60), 20, steps)
        drawer.circle(wdw[1]*(1/10), 12, steps)
        drawer.rt(180)
        drawer.circle(wdw[1]*(1/60), -43, steps)
        drawer.seth(356)
        drawer.circle(wdw[1]*(1/12), 14, steps)
        complementary()
        drawer.seth(0)
        drawer.circle(wdw[1]*(1/140), 360, steps)
        drawer.end_fill()
        
        outline(True, 4.5*wdw[1]/720, None)
        drawer.seth(0)
        drawer.pd()
        drawer.circle(wdw[1]*(1/140), 360, steps)
        drawer.pu()
        drawer.goto(center[0]-wdw[1]*(1/50), center[1]-wdw[1]*(1/38))
        drawer.pd()
        drawer.seth(344)
        drawer.circle(wdw[1]*(1/14), 31, steps)
        drawer.pu()

        
    def rook(drawer, x, y, color):
        
        center = (x, y)
        
        def complementary(offset):
            drawer.rt(90*offset)
            drawer.fd(wdw[1]*(1/72))
            drawer.rt(90*offset)
            drawer.fd(wdw[1]*(1/180))
            drawer.rt(90*offset)
            drawer.fd(wdw[1]*(1/72))
            drawer.rt(90*offset)
            drawer.fd(wdw[1]*(1/180))
        
        
        def complementary2():
            drawer.seth(76)
            drawer.circle(wdw[1]*(1/40), 25, steps)
            drawer.circle(wdw[1]*(1/10), 10, steps)
            drawer.rt(180)
            drawer.circle(wdw[1]*(1/30), -43, steps)
            drawer.rt(180)
            drawer.circle(wdw[1]*(1/10), 10, steps)
            drawer.circle(wdw[1]*(1/30), 12, steps)
            drawer.lt(90)
            drawer.fd(wdw[1]*(1/35))
            drawer.pu()
            drawer.end_fill()


        def startPoint():
            drawer.pu()
            drawer.goto(center)
            drawer.seth(90)
            drawer.fd(wdw[1]*(1/29))
            
        
        def outline(pendown, pensize, fillcolor):
            startPoint()
            drawer.pen(pendown=pendown, pensize=pensize, fillcolor=fillcolor)
            drawer.begin_fill()
            drawer.seth(180)
            drawer.fd(wdw[1]*(1/35))
            drawer.lt(90)
            drawer.circle(wdw[1]*(1/30), 12, steps)
            drawer.circle(wdw[1]*(1/10), 10, steps)
            drawer.rt(180)
            drawer.circle(wdw[1]*(1/30), -43, steps)
            drawer.rt(180)
            drawer.circle(wdw[1]*(1/10), 10, steps)
            drawer.circle(wdw[1]*(1/40), 25, steps)
            drawer.seth(0)
            drawer.fd(wdw[1]*(2/35))
            complementary2()

        
        outline(False, None, color["dark"])
        
        startPoint()
        drawer.lt(90)
        drawer.pen(pendown=False, pensize=None, fillcolor=color["light"])
        drawer.fd(wdw[1]*(1/120))
        drawer.lt(80)
        drawer.begin_fill()
        drawer.circle(wdw[1]*(1/10), 20, steps)
        drawer.rt(180)
        drawer.circle(wdw[1]*(1/30), -25, steps)
        drawer.rt(180)
        drawer.circle(wdw[1]*(1/10), 15, steps)
        drawer.seth(0)
        drawer.fd(wdw[1]*(1/23.5))
        complementary2()
        
        outline(True, 4.5*wdw[1]/720, None)
        drawer.goto(center[0]-wdw[1]*(1/50), center[1]+wdw[1]*(1/140))
        drawer.seth(0)
        drawer.pd()
        drawer.fd(wdw[1]*(1/25))
        drawer.pu()
        drawer.goto(center[0]-wdw[1]*(1/40), center[1]-wdw[1]*(1/36))
        drawer.pd()
        drawer.fd(wdw[1]*(1/20))
        startPoint()
        drawer.pen(pendown=True, pensize=1*wdw[1]/720, fillcolor="#000000")
        drawer.begin_fill()
        drawer.rt(90)
        drawer.fd(wdw[1]*(1/65))
        complementary(1)
        drawer.lt(180)
        drawer.fd(wdw[1]*(1/36))
        complementary(-1)
        drawer.pu()
        drawer.end_fill()
        
        
    def queen(drawer, x, y, color):
        
        center = (x, y)
        
        def startPoint1():
            drawer.pu()
            drawer.goto(center)
            drawer.seth(270)
            drawer.fd(wdw[1]*(1/24.2))


        def outline1(pendown, pensize, fillcolor):
            startPoint1()
            drawer.seth(0)
            drawer.pen(pendown=pendown, pensize=pensize, fillcolor=fillcolor)
            drawer.begin_fill()
            drawer.fd(wdw[1]*(1/40))
            drawer.seth(307)
            drawer.circle(wdw[1]*(1/58), -73, steps)
            drawer.seth(180)
            drawer.fd(wdw[1]*(1/21))
            drawer.seth(126)
            drawer.circle(wdw[1]*(1/58), -73, steps)
            drawer.seth(0)
            drawer.fd(wdw[1]*(1/40))
            drawer.pu()
            drawer.end_fill()
            
        
        def startPoint2():
            drawer.pu()
            drawer.goto(center[0]+wdw[1]*(1/1100), center[1])
            drawer.seth(90)
            drawer.fd(wdw[1]*(1/130))
            
            
        def outline2(pendown, pensize, fillcolor):
            startPoint2()
            drawer.seth(360)
            drawer.pen(pendown=pendown, pensize=pensize, fillcolor=fillcolor)
            drawer.begin_fill()
            drawer.circle(wdw[1]*(1/300), -49, steps)
            drawer.circle(wdw[1]*(1/22), -33, steps)
            drawer.seth(106)
            drawer.circle(wdw[1]*(1/22), -36, steps)
            drawer.circle(wdw[1]*(1/300), -103, steps)
            drawer.circle(wdw[1]*(1/26), -35, steps)
            drawer.seth(287.5)
            drawer.fd(wdw[1]*(1/28))
            drawer.circle(wdw[1]*(1/98), 70, steps)
            drawer.seth(0)
            drawer.fd(wdw[1]*(1/38))
            drawer.circle(wdw[1]*(1/98), 72, steps)
            drawer.fd(wdw[1]*(1/28))
            drawer.seth(68)
            drawer.circle(wdw[1]*(1/26), -33, steps)
            drawer.circle(wdw[1]*(1/300), -103, steps)
            drawer.circle(wdw[1]*(1/22), -36, steps)
            drawer.seth(85)
            drawer.circle(wdw[1]*(1/22), -33, steps)
            drawer.circle(wdw[1]*(1/300), -49, steps)
            drawer.pu()
            drawer.end_fill()


        def crownCircle():
            drawer.seth(0)
            drawer.pen(pendown=True, pensize=4.5*wdw[1]/720, fillcolor=color["light"])
            drawer.begin_fill()
            drawer.circle(wdw[1]*(1/180), 360, steps)
            drawer.pu()
            drawer.end_fill()
            

        outline1(False, 0, color["light"])
        
        outline2(False, 0, color["light"])
        
        startPoint2()
        drawer.seth(360)
        drawer.circle(wdw[1]*(1/300), -49, steps)
        drawer.circle(wdw[1]*(1/22), -33, steps)
        drawer.seth(106)
        drawer.circle(wdw[1]*(1/22), -36, steps)
        drawer.circle(wdw[1]*(1/300), -60, steps)
        drawer.seth(280)
        drawer.pen(pendown=False, fillcolor=color["dark"])
        drawer.begin_fill()
        drawer.circle(wdw[1]*(1/30), 28, steps)
        drawer.circle(wdw[1]*(1/80), 60, steps)
        drawer.seth(270)
        drawer.fd(wdw[1]*(1/330))
        drawer.seth(180)
        drawer.fd(wdw[1]*(1/70))
        drawer.rt(180)
        drawer.circle(wdw[1]*(1/98), -72, steps)
        drawer.rt(180)
        drawer.fd(wdw[1]*(1/28))
        drawer.seth(292)
        drawer.circle(wdw[1]*(1/26), 33, steps)
        drawer.circle(wdw[1]*(1/300), 50, steps)
        drawer.end_fill()
        
        startPoint1()
        drawer.seth(180)
        drawer.fd(wdw[1]*(1/100))
        drawer.seth(54)
        drawer.pen(pendown=False, fillcolor=color["dark"])
        drawer.begin_fill()
        drawer.circle(wdw[1]*(1/58), 73, steps)
        drawer.seth(180)
        drawer.fd(wdw[1]*(1/90))
        drawer.seth(126)
        drawer.circle(wdw[1]*(1/58), -73, steps)
        drawer.seth(0)
        drawer.fd(wdw[1]*(1/90))
        drawer.end_fill()
        
        outline1(True, 4.5*wdw[1]/720, None)
        
        outline2(True, 4.5*wdw[1]/720, None)
        
        startPoint2()
        drawer.seth(180)
        drawer.fd(wdw[1]*(1/29.5))
        drawer.rt(90)
        drawer.fd(wdw[1]*(1/132))
        crownCircle()
        
        startPoint2()
        drawer.seth(180)
        drawer.fd(wdw[1]*(1/76))
        drawer.rt(90)
        drawer.fd(wdw[1]*(1/53))
        crownCircle()
        
        startPoint2()
        drawer.seth(0)
        drawer.fd(wdw[1]*(1/76))
        drawer.lt(90)
        drawer.fd(wdw[1]*(1/53))
        crownCircle()
        
        startPoint2()
        drawer.seth(0)
        drawer.fd(wdw[1]*(1/29.5))
        drawer.lt(90)
        drawer.fd(wdw[1]*(1/132))
        crownCircle()
        
        startPoint1()
        drawer.seth(0)
        drawer.fd(wdw[1]*(1/40))
        drawer.seth(307)
        drawer.circle(wdw[1]*(1/58), -36.5, steps)
        drawer.seth(180)
        drawer.pen(pendown=True, pensize=4.5*wdw[1]/720)
        drawer.fd(wdw[1]*(1/25))
        drawer.pu()
        
        
    def king(drawer, x, y, color):
        
        center = (x, y)
        
        def startPoint():
            drawer.pu()
            drawer.goto(center)
            drawer.seth(0)
            drawer.fd(wdw[1]*(1/1000))
            drawer.seth(270)
            drawer.fd(wdw[1]*(1/52))
            
        
        def outline1(pendown, fillcolor):
            startPoint()
            drawer.seth(180)
            drawer.pen(pendown=pendown, fillcolor=fillcolor)
            drawer.begin_fill()
            drawer.fd(wdw[1]*(1/35))
            drawer.circle(2.25*wdw[1]/720, 90, steps)
            drawer.fd(wdw[1]*(1/120))
            drawer.circle(2.25*wdw[1]/720, 90, steps)
            drawer.fd(wdw[1]*(2/35))
            drawer.circle(2.25*wdw[1]/720, 90, steps)
            drawer.fd(wdw[1]*(1/120))
            drawer.circle(2.25*wdw[1]/720, 90, steps)
            drawer.fd(wdw[1]*(1/35))
            drawer.end_fill()
            drawer.pu()
            
        def outline2(reverse, extent, length, pendown, fillcolor):
            rev = 1
            if reverse == True: rev = -1
            startPoint()
            drawer.rt(rev*90)
            drawer.fd(extent)
            drawer.lt(rev*140)
            if reverse == True: drawer.rt(180)
            drawer.pen(pendown=pendown, fillcolor=fillcolor)
            drawer.begin_fill()
            drawer.circle(length, rev*-26, steps)
            drawer.circle(wdw[1]*(1/75), rev*-185, steps)
            drawer.seth(270)
            drawer.fd(wdw[1]*(1/40))
            drawer.pu()
            drawer.end_fill()
            
        def outline3(pendown, fillcolor):
            startPoint()
            drawer.seth(270)
            drawer.fd(wdw[1]*(1/70))
            drawer.pen(pendown=pendown, fillcolor=fillcolor)
            drawer.begin_fill()
            drawer.seth(180)
            drawer.fd(wdw[1]*(1/38))
            drawer.circle(2.25*wdw[1]/720, 90, steps)
            drawer.fd(wdw[1]*(1/270))
            drawer.circle(2.25*wdw[1]/720, 90, steps)
            drawer.fd(wdw[1]*(2/38))
            drawer.circle(2.25*wdw[1]/720, 90, steps)
            drawer.fd(wdw[1]*(1/270))
            drawer.circle(2.25*wdw[1]/720, 90, steps)
            drawer.fd(wdw[1]*(1/39))
            drawer.pu()
            drawer.end_fill()
            
        def complementary1(pendown, fillcolor):
            startPoint()
            drawer.rt(90)
            drawer.fd(wdw[1]*(1/85))
            drawer.lt(140)
            drawer.pen(pendown=pendown, fillcolor=fillcolor)
            drawer.circle(wdw[1]*(1/21), -26, steps)
            drawer.circle(wdw[1]*(1/75), -133, steps)
            drawer.begin_fill()
            drawer.seth(68)
            drawer.fd(wdw[1]*(1/135))
            drawer.rt(180)
            drawer.circle(3.25*wdw[1]/720, -68, steps)
            drawer.rt(180)
            
        def complementary2():
            drawer.rt(180)
            drawer.circle(3.25*wdw[1]/720, -68, steps)
            drawer.rt(180)
            drawer.fd(wdw[1]*(1/200))
            
        def complementary3(length):
            startPoint()
            drawer.seth(180)
            drawer.pen(pendown=True, pencolor="#000000", pensize=4.5*wdw[1]/720)
            drawer.fd(length)
            drawer.seth(295)
            drawer.fd(wdw[1]*(1/70))
            drawer.pu()
        
            
        complementary1(False, color["light"])
        drawer.fd(wdw[1]*(2/700))
        complementary2()
        drawer.rt(30)
        drawer.fd(wdw[1]*(1/100))
        drawer.end_fill()

        drawer.pen(pensize=4.5*wdw[1]/720)
        
        outline2(False, wdw[1]*(1/38), wdw[1]*(1/22), False, color["dark"])
        outline2(False, wdw[1]*(1/38), wdw[1]*(1/22), True, None)
        
        outline2(True, wdw[1]*(1/38), wdw[1]*(1/22), False, color["dark"])
        startPoint()
        drawer.seth(0)
        drawer.fd(wdw[1]*(1/60))
        drawer.seth(270)
        drawer.pen(pendown=False, fillcolor=color["light"])
        drawer.begin_fill()
        drawer.circle(wdw[1]*((1/30)), -65, steps)
        drawer.seth(120)
        drawer.circle(wdw[1]*(1/75), -40, steps)
        drawer.circle(wdw[1]*(1/22), -32, steps)
        drawer.end_fill()
        outline2(True, wdw[1]*(1/38), wdw[1]*(1/22), True, None)
        
        outline2(False, wdw[1]*(1/85), wdw[1]*(1/21), False, color["dark"])
        complementary1(False, None)
        drawer.pen(pendown=False, fillcolor= color["light"])
        drawer.begin_fill()
        drawer.seth(210)
        drawer.circle(wdw[1]*(1/40), 140, steps)
        drawer.end_fill()
        outline2(False, wdw[1]*(1/85), wdw[1]*(1/21), True, None)
        
        outline2(True, wdw[1]*(1/85), wdw[1]*(1/21), False, color["light"])
        startPoint()
        drawer.pen(pendown=False, fillcolor=color["dark"])
        drawer.begin_fill()
        drawer.seth(90)
        drawer.fd(wdw[1]*(1/36))
        drawer.seth(251)
        drawer.circle(wdw[1]*(1/85), -115, steps)
        drawer.seth(180)
        drawer.circle(wdw[1]*(1/110), 90, steps)
        drawer.seth(259)
        drawer.circle(wdw[1]*(1/10), 13, steps)
        drawer.end_fill()
        outline2(True, wdw[1]*(1/85), wdw[1]*(1/21), True, None)

        complementary1(True, None)
        drawer.fd(wdw[1]*(1/700))
        drawer.lt(90)
        drawer.fd(wdw[1]*(1/55))
        drawer.pu()
        drawer.fd(wdw[1]*(1/750))
        drawer.circle(wdw[1]*(1/110), -90, steps)
        drawer.fd(wdw[1]*(1/750))
        drawer.pd()
        drawer.fd(wdw[1]*((1/55)-(2/750)))
        drawer.pu()
        drawer.fd(wdw[1]*(3/750))
        drawer.seth(90)
        drawer.circle(wdw[1]*((1/110)+(1/750)), -90, steps)
        drawer.pd()
        complementary2()
        
        complementary3(wdw[1]*(1/50))
        complementary3(wdw[1]*(1/270))
        complementary3(-wdw[1]*(1/78))
        
        outline1(False, color["light"])
        outline1(True, None)
        outline3(False, color["dark"])
        outline3(True, None)
        

    def possibleMoves():
         for l in range(8):
             for m in range(8):
                 if pieces[pdi[0]][pdi[1]][pdi[2]][2][l][m] == 1:
                    check_piece_matrix = copy.deepcopy(board_matrix)
                    check_piece_matrix[l][m] = 1
                    if pieceDetector(check_piece_matrix)[0]:
                        possible_moves_drw.goto(corners[0][0] + wdw[1]*((m+1)/9) - wdw[1]*(1/18), corners[0][1] + wdw[1]*((l+1)/9) - wdw[1]*(1/18))
                        possible_moves_drw.seth(0)
                        if (m % 2 == 0 and l % 2 == 0) or (m % 2 == 1 and l % 2 == 1):
                            possible_moves_drw.pen(pendown=True, pencolor=themes[theme][1][1], pensize=6*wdw[1]/720)
                        elif (m % 2 == 1 and l % 2 == 0) or (m % 2 == 0 and l % 2 == 1):
                            possible_moves_drw.pen(pendown=True, pencolor=themes[theme][1][0], pensize=6*wdw[1]/720)
                        
                        for i in range(4):
                            possible_moves_drw.fd(wdw[1]*(1/9))
                            possible_moves_drw.lt(90)
                        
                    else:
                        possible_moves_drw.goto(corners[0][0] + wdw[1]*((m+1)/9), corners[0][1] + wdw[1]*((l+1)/9))
                        if (m % 2 == 0 and l % 2 == 0) or (m % 2 == 1 and l % 2 == 1):
                            possible_moves_drw.dot(20*wdw[1]/720, themes[theme][1][1])
                        elif (m % 2 == 1 and l % 2 == 0) or (m % 2 == 0 and l % 2 == 1):
                            possible_moves_drw.dot(20*wdw[1]/720, themes[theme][1][0])

                    possible_moves_drw.pu()
                
            




    
    
def clickDetection(x, y):
    # Called by t.onscreenclick() everytime there is a click.
    # x, y = coordinates for the click
    global clicks_done, first_click_matrix, second_click_matrix, pdi, i1, j1, moving_team, opponent_team, moves, defended_matrices
    for i in range(1, 9):
        # For each column in the board (a to h)
        for j in range (1, 9):
            # For each row in the board (1 to 8)
            if (x > corners[0][0] + wdw[1]*(i/9) - wdw[1]*(1/18) and x < corners[0][0] + wdw[1]*(i/9) + wdw[1]*(1/18)) and (y > corners[0][1] + wdw[1]*(j/9) - wdw[1]*(1/18) and y < corners[0][1] + wdw[1]*(j/9) + wdw[1]*(1/18)):
            # Go through each square (1, 1) --> (1, 8) --> (2, 1) --> (2, 8), until it meets the condition that the click was inside the area of the analyzed square.
            # If it returns True, it means it was clicked inside the board and it will be storing in what column / x in i, and what row / y in j.
                if clicks_done == 0:
                    # If there wasn't a piece selected before.
                    i1 = i-1  # The x index of the board matrix location where we clicked. Same as the visual column - 1
                    j1 = j-1  # Y index. Same as the visual row - 1
                    first_click_matrix = copy.deepcopy(board_matrix)
                    first_click_matrix[j1][i1] = 1
                    # In the matrix we go through each square in the opposite way of how we detect above: first input what row (y), once selected what column (x). That is [y][x].
                    # Save the location in which we clicked in an empty board matrix
                    
                    if pieceDetector(first_click_matrix)[0] == True:
                        # If it detects there is a piece in the square clicked the piece is selected to move
                        pdi = pieceDetector(first_click_matrix)[1]  # Save what piece was clicked
                        moving_team = pdi[0]  # Save the team of the piece clicked
                        if moving_team == 0: opponent_team = 1
                        elif moving_team == 1: opponent_team = 0
                        clicks_done += 1  # Since a piece was succesfully selected next step is the algorithm to move it
                        drawers[pdi[0]][pdi[1]][pdi[2]][0].clear()  # Erase the piece
                        selectedPieceSquareDraw(i, j)  # Draw the selected piece square with shade
                        redrawSelectedPiece()  # Draw the piece back
                        draw.possibleMoves()
                        t.update()
                        return
                    else:
                        # If there is no piece in the square clicked
                        first_click_matrix = copy.deepcopy(board_matrix)
                        # Erase the click location and end. 
                        return
                    
                elif clicks_done == 1:
                    # If we had already selected a piece to move.
                    i2 = i-1  # The x index of the board matrix location where we want to move the piece. Same as the visual column - 1
                    j2 = j-1  # Y index. Same as the visual row - 1
                    second_click_matrix = copy.deepcopy(board_matrix)
                    second_click_matrix[j2][i2] = 1
                    first_click_matrix = copy.deepcopy(board_matrix)
                    # Always with the 2nd click we reset the first click location
                    # Save the 2nd click location in an empty board matrix.
                    
                    if (i-1) == i1 and (j-1) == j1:
                        # If we 2nd clicked in the same spot as the first click we cancel the move action and the selected piece
                        clicks_done = 0  # Restart the "has clicked" status
                        sel_sqr_drw[0][0].clear()
                        possible_moves_drw.clear()
                        # Always with the 2nd click the selected piece square shade disapears, no matter where we click
                        t.update()  # Update the drawing so that shade is removed

                    elif pieceDetector(second_click_matrix)[0] == True and moving_team == pieceDetector(second_click_matrix)[1][0]:
                        # There's a piece in the selected square, now, of what team? (can I move into it?)
                        # The selected piece is of the same team as the moved piece.
                        # This means that we cannot move into it and thus we will just change the piece selected to be moved to the new one.
                        i1 = i-1  # Change the 1st click x index location to be the new one
                        j1 = j-1  # "" with the y location
                        sel_sqr_drw[0][0].clear()  # Removes the selected square shade
                        possible_moves_drw.clear()  # Removes the piece's possible moves dots
                        first_click_matrix[j-1][i-1] = 1  # Changes the first click selection to the new square
                        pdi = pieceDetector(first_click_matrix)[1]  # Changes the piece selected
                        draw.possibleMoves()  # Draws possible moves for new piece
                        selectedPieceSquareDraw(i, j)  # Draws the selected square shade
                        redrawSelectedPiece()  # Draws the piece above the shade
                        clicks_done = 1  # Enables the piece to be moved in the next click

                    elif second_click_matrix[j2][i2] == pieces[pdi[0]][pdi[1]][pdi[2]][2][j2][i2]:
                        # That (the 2nd click location == a possible move for the selected piece (sp) and sp wasn't king) or if sp is a king       ""                 ==           ""         and also has to be moving to a not-defended-location of the other team.
                        # If 1 (the matrix location of the click) == 1 (a possible move matrix location of the selected piece)
                        
                        if pieceDetector(second_click_matrix)[0] == False:
                            # No piece in the selected square = procede to move
                            if pieceMover(pdi, i2, j2, i1, j1):  # Pass the selected piece indices and the desired move location indices
                                pieces[pdi[0]][pdi[1]][pdi[2]][4] = True
                                attachPieceMovesMatrix()  # Update the possible moves for all pieces
                                sel_sqr_drw[0][0].clear()
                                possible_moves_drw.clear()
                                clicks_done = 0  # Restart the click status so you can choose a new piece to move
                                
                            attachPieceMovesMatrix()
                            t.update()
                        
                        elif pieceDetector(second_click_matrix)[0] == True and moving_team != pieceDetector(second_click_matrix)[1][0]:
                            # When there is a piece in the selected square and it's from the other team you need to eat it.
                            i = pieceDetector(second_click_matrix)[1][0]  # Team of the piece to eat
                            j = pieceDetector(second_click_matrix)[1][1]  # Type of piece of the piece to eat
                            k = pieceDetector(second_click_matrix)[1][2]  # Individual piece to eat
                            pieces[i][j][k][1] = copy.deepcopy(board_matrix)  # Removes the saved position of the eaten piece
                            pieces[i][j][k][2] = copy.deepcopy(board_matrix)  # Removes the possible moves of the eaten piece
                            pieces[i][j][k][3] = False  # Changes status to piece not alive
                            if pieceMover(pdi, i2, j2, i1, j1):
                                # If your king is not in check after moving the piece then it moves the piece
                                sel_sqr_drw[0][0].clear()
                                possible_moves_drw.clear()
                                drawers[i][j][k][0].clear()
                                pieces[pdi[0]][pdi[1]][pdi[2]][4] = True  # Changes piece moved status to "has moved"
                                clicks_done = 0  # Restarts so that you can select a new piece to move
                            else:
                                # You cannot move and eat the piece (because you let your king in check)
                                pieces[i][j][k][1][j2][i2] = 1  # Re-attaches the position of the selected piece to move
                                pieces[i][j][k][3] = True  # Re-attaches its "alive" status
                            attachPieceMovesMatrix()
                            t.update()
                            
                    return
                            
                    
                    
            elif x < (corners[0][0] + wdw[1]*(1/9) - wdw[1]*(1/18)) or x > (corners[0][0] + wdw[1]*(8/9) + wdw[1]*(1/18)) or y < (corners[0][1] + wdw[1]*(1/9) - wdw[1]*(1/18)) or y > (corners[0][1] + wdw[1]*(8/9) + wdw[1]*(1/18)):
                # If the click is outside the board then the selection is restarted / you can't move the piece
                if clicks_done == 0:
                    first_click_matrix = copy.deepcopy(board_matrix)  # Erase the selected location of the click
                if clicks_done == 1:
                    first_click_matrix = copy.deepcopy(board_matrix)
                    clicks_done = 0
                    sel_sqr_drw[0][0].clear()
                    possible_moves_drw.clear()
                    t.update()
                return


def pieceDetector(board_matrix):
    # Function to detect if there is a piece in the exact point of an imported matrix.
    # Matrix must have only one "1" as the click location and the rest indeces as "0"
    for i in range(len(pieces)):
        for j in range(len(pieces[i])):
            for k in range(len(pieces[i][j])):
                if pieces[i][j][k][1] == board_matrix:
                    return True, (i,j,k)  # If it detects a piece then it returns True and what piece is in that matrix position
    return False, None  # If there isn't any piece then it returns False


def kingMovesCheckDetector():
    # Function to check if the king is in check in each of its possible moves for the current board state
    # Since the pawns don't eat as they move then we only have to check for the pawn diagonal movement:
    for i in range(len(pieces)):
        if i == 0:  # If we are checking the white king moves then we check the black pawns which move down, direction = -1
            opponent = 1
            direction = -1
        elif i == 1: # We check black king moves so we get the white pawns eating moves that are up, direction = 1
            opponent = 0
            direction = 1

        for k in range(len(pieces[opponent][0])):
            for l in range(len(pieces[opponent][0][k][1])):
                for m in range(len(pieces[opponent][0][k][1][l])):
                    # Check every piece and its location from the opposite team
                    if pieces[opponent][0][k][1][l][m] == 1:
                        # If there is an enemy pawn stop exactly at its position in matrix
                        for x in range(-1, 2, 2):
                            # The pawn moves diagonal which means x - 1 and x + 1
                            if (m + x) < 8 and (m + x) > -1 and (l + direction) < 8 and (l + direction) > -1:
                                # Checks for all the eat moves of all enemy pawns
                                pieces[i][5][0][2][l + direction][m + x] = 0
                                    # Turns all enemy pawns eat squares negative to move into by the analyzed king
                            
        for j in range(1, len(pieces[opponent])):
            for k in range(len(pieces[opponent][j])):
                for l in range(len(pieces[opponent][j][k][2])):
                    for m in range(len(pieces[opponent][j][k][2][l])):
                        # Checks every opponent piece possible moves matrix excluding the pawns (analyzed before)
                        if pieces[opponent][j][k][2][l][m] == pieces[i][5][0][2][l][m] == 1:
                            # If a possible move for an enemy piece is a possible move for the analyzed king then:
                              pieces[i][5][0][2][l][m] = 0
                                  # Remove the square as a possible move for the king (it would be in check)
                                
        for l in range(len(defended_matrices[opponent])):
            for m in range(len(defended_matrices[opponent][l])):
                # Check the matrices of defended pieces in the board.
                if defended_matrices[opponent][l][m] == pieces[i][5][0][2][l][m] == 1:
                    # If there is a piece DEFENDED BY ITS TEAM that the king has a possible move into (to eat) then:
                    pieces[i][5][0][2][l][m] = 0
                        # Remove the position as a possible move for the king (it would be in check)


def checkDetector(team):
    # Function to check if the king (of the team "team") is in check
    if team == 0:
        opponent = 1
        direction = -1
    elif team == 1:
        opponent = 0
        direction = 1
    
    # Similar code as kingMovesCheckDetector() to check for pawn moves
    for k in range(len(pieces[opponent][0])):
            for l in range(len(pieces[opponent][0][k][1])):
                for m in range(len(pieces[opponent][0][k][1][l])):
                    if pieces[opponent][0][k][1][l][m] == 1:
                        for x in range(-1, 2, 2):
                            if (m + x) < 8 and (m + x) > -1 and (l + direction) < 8 and (l + direction) > -1:
                                if pieces[opponent][0][k][2][l+direction][m+x] == pieces[team][5][0][1][l+direction][m+x] == 1:
                                    # If there is an enemy pawn located in a position where it is threatening the king then:
                                    return True  # Return true (king is in check)
    
    # Similar code as kingMovesCheckDetector() to check for all other types of pieces moves
    for j in range(1, len(pieces[opponent])):
        for k in range(len(pieces[opponent][j])):
            for l in range(len(pieces[opponent][j][k][2])):
                for m in range(len(pieces[opponent][j][k][2][l])):
                    if pieces[opponent][j][k][2][l][m] == pieces[team][5][0][1][l][m] == 1:
                        # If there is an enemy piece threatening the king then:
                        return True  # King is in check
    return False  # Return false (king is not in check)


def pieceMover(pdi, i2, j2, i1, j1):  # pdi = piece detected indices
    # Function that makes the required changes in data and visuals to move a piece from a square to another.
    # Checks if the king of the team of the piece to be moved is in check so it can stop the move from happening
    
    pieces[pdi[0]][pdi[1]][pdi[2]][1] = copy.deepcopy(board_matrix)  # Remove the location of the selected piece
    pieces[pdi[0]][pdi[1]][pdi[2]][1][j2][i2] = 1  # Store new location in matrix
    attachPieceMovesMatrix()  # Give every piece its possible after the piece has been moved

    if checkDetector(pdi[0]):
        # If the king of the team that is moving is in check it will undo and give the piece its location back
        pieces[pdi[0]][pdi[1]][pdi[2]][1][j2][i2] = 0
        pieces[pdi[0]][pdi[1]][pdi[2]][1][j1][i1] = 1
        return False # Will not move (king would be in check)
    
    # Only runs if the king isn't in check
    drawers[pdi[0]][pdi[1]][pdi[2]][0].clear()  # Erase selected piece drawing
    check_sqr_drw.clear()  # Erase selected square shade
    # Draw piece according to its type and team
    if pdi[1] == 0: draw.pawn(drawers[pdi[0]][pdi[1]][pdi[2]][0], corners[0][0] + wdw[1]*((i2+1)/9), corners[0][1] + (wdw[1]*((j2+1)/9)), team[pdi[0]]) 
    elif pdi[1] == 1: draw.knight(drawers[pdi[0]][pdi[1]][pdi[2]][0], corners[0][0] + wdw[1]*((i2+1)/9), corners[0][1] + (wdw[1]*((j2+1)/9)), team[pdi[0]])
    elif pdi[1] == 2: draw.bishop(drawers[pdi[0]][pdi[1]][pdi[2]][0], corners[0][0] + wdw[1]*((i2+1)/9), corners[0][1] + (wdw[1]*((j2+1)/9)), team[pdi[0]])
    elif pdi[1] == 3: draw.rook(drawers[pdi[0]][pdi[1]][pdi[2]][0], corners[0][0] + wdw[1]*((i2+1)/9), corners[0][1] + (wdw[1]*((j2+1)/9)), team[pdi[0]])
    elif pdi[1] == 4: draw.queen(drawers[pdi[0]][pdi[1]][pdi[2]][0], corners[0][0] + wdw[1]*((i2+1)/9), corners[0][1] + (wdw[1]*((j2+1)/9)), team[pdi[0]])
    elif pdi[1] == 5: draw.king(drawers[pdi[0]][pdi[1]][pdi[2]][0], corners[0][0] + wdw[1]*((i2+1)/9), corners[0][1] + (wdw[1]*((j2+1)/9)), team[pdi[0]])
    
    if checkDetector(opponent_team):
        # If after doing the move the opponent team's king is in check
        drawers[opponent_team][5][0][0].clear()  # Erase the opponent's king drawing
        for l in range(len(pieces[opponent_team][5][0][1])):
            for m in range(len(pieces[opponent_team][5][0][1][l])):
                if pieces[opponent_team][5][0][1][l][m] == 1:
                    # Get the exact matrix indices of the opponent's king so it can draw a "checked shade" and redraw it above it
                    checkedKingSquareDraw(m+1, l+1)
                    draw.king(drawers[opponent_team][5][0][0], corners[0][0] + wdw[1]*((m+1)/9), corners[0][1] + (wdw[1]*((l+1)/9)), team[opponent_team])
    else:
        # It will constantly delete the check square shade everytime the opponent team is not in check (even if it's already deleted)
        check_sqr_drw.clear()
    
    # Code to be able to do a short castling
    if pdi[0] == 0: row = 0  # If we selected a white piece then the row where the king is located is the first
    elif pdi[0] == 1: row = 7  # If black then it is in row 8
    if pdi[1] == 5 and pieces[pdi[0]][5][0][4] == False and pieces[pdi[0]][pdi[1]][pdi[2]][1][row][1] == 1:
        # If the piece selected is a king and the rook hasn't moved and it meets the castling requirements (king hasn't moved, rook hasn't moved, no pieces in the middle and king not in check when it after moving)
        pieces[pdi[0]][3][0][1] = copy.deepcopy(board_matrix)  # Erase the location of the rook
        pieces[pdi[0]][3][0][1][row][2] = 1  # Change its position
        drawers[pdi[0]][3][0][0].clear()  # Erase its visual position
        draw.rook(drawers[pdi[0]][3][0][0], corners[0][0] + wdw[1]*(3/9), corners[0][1] + (wdw[1]*((row+1)/9)), team[pdi[0]])  # Draw the rook in the new position
        
    return True  # King is not in check

def attachPieceLocationMatrix():
    # Function to attach the piece location matrix to each piece.
    # It runs at the start of the match to give each piece its default location
    for i in range(len(pieces)):
        for j in range(len(pieces[i])):
            for k in range(len(pieces[i][j])):
                # Analyze all the pieces
                if i == 0: row = 1  # If the team analyzed is white then default position of all pieces except pawns is row 1
                elif i == 1: row = 8  # Black = row 8
                pieces[i][j][k][1] = copy.deepcopy(board_matrix)  # Erase the piece's position matrix
                if pieces[i][j] == pieces[0][0]: row += 1  # If the piece is a pawn and team is white then row is 1 higher
                elif pieces[i][j] == pieces[1][0]: row -= 1  # If pawn and black then row is 1 lower
                pieces[i][j][k][1][row-1][drawers[i][j][k][1]-1] = 1  # Give every piece its location from its row and the column location in the drawers list
                pieces[i][j][k][3] = True  # Set the piece as status alive


def attachPieceMovesMatrix():
    # Function to attach the possible moves matrices to each piece.
    # This function is called every time there is a change in the position and state of the game to refresh all the piece's moves
    global defended_matrices  # Edits the global variable defended_matrices so the edited data can be used on another function
    defended_matrices = [copy.deepcopy(board_matrix), copy.deepcopy(board_matrix)]
    for i in range(len(pieces)):
        for j in range(len(pieces[i])):
            for k in range(len(pieces[i][j])):
                for l in range(len(pieces[i][j][k][1])):
                    for m in range(len(pieces[i][j][k][1][l])):
                        if pieces[i][j][k][1][l][m] == 1 and (j == 0 or j == 1 or j == 2 or j == 3 or j == 4 or j == 5):
                            # Checks each piece and retrives the indices of its location
                            index_y_piece = l  # first index, the row / y
                            index_x_piece = m  # second index, the column / x
                
                if pieces[i][j][k][3] == True:
                    # It only attaches possible moves to the piece if it is "alive"
                    possible_moves_matrix = copy.deepcopy(board_matrix)  # Creates a temporal matrix to add the possible moves into and will be attached in the end of the analysis
                    if j == 0:
                        # If the piece is a pawn
                        if i == 0: y = 1
                        elif i == 1: y = -1
                        # White pawns move up and black pawns move down
                        for x in range(-1, 2, 2):
                            # Combinations will be: [(-1, 1), (1, 1)] when team = 0, [(-1, -1), (1, -1)] when team = 1.
                            if (index_x_piece + x) > 7 or (index_x_piece + x) < 0 or (index_y_piece + y) > 7 or (index_y_piece + y) < 0:
                                # If the move to be checked is outside the matrix (outside the board) then it breaks
                                break
                            move_check_matrix = copy.deepcopy(board_matrix)
                            move_check_matrix[index_y_piece + y][index_x_piece + x] = 1
                            if pieceDetector(move_check_matrix)[0] == True:
                                if pieceDetector(move_check_matrix)[1][0] == i:
                                    defended_matrices[i][index_y_piece + y][index_x_piece + x] = 1
                                elif pieceDetector(move_check_matrix)[1][0] != i:
                                    possible_moves_matrix[index_y_piece + y][index_x_piece + x] = 1
                        if (index_y_piece + y) > 7 or (index_y_piece + y) < 0:
                            break
                        move_check_matrix = copy.deepcopy(board_matrix)
                        move_check_matrix[index_y_piece + y][index_x_piece] = 1
                        if pieceDetector(move_check_matrix)[0] == False:
                            possible_moves_matrix[index_y_piece + y][index_x_piece] = 1
                            if pieces[i][j][k][4] == False:
                                possible_moves_matrix[index_y_piece + 2 * y][index_x_piece] = 1
                                
                    elif j == 1:
                        for repeat in range(2):
                            # 2 repetitions. In the 1st x will be (1, -1) and y (2, -2). In the 2nd viceversa.
                            for coord1 in range(-1, 2, 2):
                                # Combinations will be (-1, 1)
                                for coord2 in range(-2, 3, 4):
                                    # Combinations will be (-2, 2):
                                    if repeat == 0: x = coord1; y = coord2
                                    elif repeat == 1: x = coord2; y = coord1
                                    # First iteration will be: repeat = 0, so x = -1, y = -2
                                    # This means it will first check for the square of the bottom left.
                                    if (index_x_piece + x) < 8 and (index_x_piece + x) > -1 and (index_y_piece + y) < 8 and (index_y_piece + y) > -1:
                                        move_check_matrix = copy.deepcopy(board_matrix)
                                        move_check_matrix[index_y_piece + y][index_x_piece + x] = 1
                                        if pieceDetector(move_check_matrix)[0] == True:
                                            if pieceDetector(move_check_matrix)[1][0] == i:
                                                defended_matrices[i][index_y_piece + y][index_x_piece + x] = 1
                                            elif pieceDetector(move_check_matrix)[1][0] != i:
                                                possible_moves_matrix[index_y_piece + y][index_x_piece + x] = 1
                                        elif pieceDetector(move_check_matrix)[0] == False:
                                            possible_moves_matrix[index_y_piece + y][index_x_piece + x] = 1

                    elif j == 2:
                        for x in range(-1, 2, 2):  # (-1, 1)
                            for y in range(-1, 2, 2):  # (-1, 1)
                                # Combinations will be: [(-1, -1), (-1, 1), (1, -1), (1, 1)]
                                index_y = copy.deepcopy(index_y_piece)
                                index_x = copy.deepcopy(index_x_piece)
                                while True:  # You are inside the board matrix and thus inside the board
#                                     print(f"Using ({index_x+x+1}, {index_y+y+1}) for bishop {k} of team {i}")
                                    if (index_x + x) > 7 or (index_x + x) < 0 or (index_y + y) > 7 or (index_y + y) < 0:
#                                         print("Stopped loop: Outside of Board")
                                        break
                                    move_check_matrix = copy.deepcopy(board_matrix)
                                    move_check_matrix[index_y + y][index_x + x] = 1
                                    if pieceDetector(move_check_matrix)[0] == True:  # If the check is true there is a piece, now, of what team? (can i eat it?)
                                    # Check in the matrices of all pieces the exact point [index + j][index + i], where index is the current position of the bishop.
                                        if pieceDetector(move_check_matrix)[1][0] == i:  # Team piece
                                            # Position not posible to move into
                                            defended_matrices[i][index_y + y][index_x + x] = 1
#                                           # Add the matrix location as a defended location
                                        elif pieceDetector(move_check_matrix)[1][0] != i:  # Enemy piece
                                            possible_moves_matrix[index_y + y][index_x + x] = 1  # Position posible to move into
#                                             print("Stopped loop: Enemy piece")
                                        break
                                    elif pieceDetector(move_check_matrix)[0] == False:  # If false, the space is possible to move into and we have to check for more
                                        possible_moves_matrix[index_y + y][index_x + x] = 1  # Position posible to move into
#                                         print(f"Posible to move to ({index_x + x + 1}, {index_y + y + 1})")
                                        index_y += y
                                        index_x += x
                    
                    elif j == 3:
                        for coordinate in range(2):
                            for offset in range(-1, 2, 2):  # (-1, 1)
                                # Combinations will be: [(-1, 0), (1, 0)] for x
                                if coordinate == 0:
                                    y = 0  # First repetition will be to check moves in row / x, thus always in same y
                                    x = offset
                                elif coordinate == 1:
                                    x = 0  # Second for column / y, thus always in same x
                                    y = offset
                                index_x = copy.deepcopy(index_x_piece)
                                index_y = copy.deepcopy(index_y_piece)
                                while True:
                                    if (index_x + x) > 7 or (index_x + x) < 0 or (index_y + y) > 7 or (index_y + y) < 0:
                                        break
                                    move_check_matrix = copy.deepcopy(board_matrix)
                                    move_check_matrix[index_y + y][index_x + x] = 1
                                    if pieceDetector(move_check_matrix)[0] == True:
                                        if pieceDetector(move_check_matrix)[1][0] == i:
                                            defended_matrices[i][index_y + y][index_x + x] = 1
                                        elif pieceDetector(move_check_matrix)[1][0] != i:
                                            possible_moves_matrix[index_y + y][index_x + x] = 1
                                        break
                                    elif pieceDetector(move_check_matrix)[0] == False:
                                        possible_moves_matrix[index_y + y][index_x + x] = 1
                                        index_x += x
                                        index_y += y
                    
                    elif j == 4:
                        # Same code to check for bishops
                        for x in range(-1, 2, 2):
                            for y in range(-1, 2, 2):
                                index_y = copy.deepcopy(index_y_piece)
                                index_x = copy.deepcopy(index_x_piece)
                                while True:
                                    if (index_x + x) > 7 or (index_x + x) < 0 or (index_y + y) > 7 or (index_y + y) < 0:
                                        break
                                    move_check_matrix = copy.deepcopy(board_matrix)
                                    move_check_matrix[index_y + y][index_x + x] = 1
                                    if pieceDetector(move_check_matrix)[0] == True:
                                        if pieceDetector(move_check_matrix)[1][0] == i:
                                            defended_matrices[i][index_y + y][index_x + x] = 1
                                        elif pieceDetector(move_check_matrix)[1][0] != i:
                                            possible_moves_matrix[index_y + y][index_x + x] = 1
                                        break
                                    elif pieceDetector(move_check_matrix)[0] == False:
                                        possible_moves_matrix[index_y + y][index_x + x] = 1
                                        index_y += y
                                        index_x += x
                        
                        # Same code to check for rooks
                        for coordinate in range(2):
                            for offset in range(-1, 2, 2):
                                if coordinate == 0: y = 0; x = offset
                                elif coordinate == 1: x = 0; y = offset
                                index_x = copy.deepcopy(index_x_piece)
                                index_y = copy.deepcopy(index_y_piece)
                                while True:
                                    if (index_x + x) > 7 or (index_x + x) < 0 or (index_y + y) > 7 or (index_y + y) < 0:
                                        break
                                    move_check_matrix = copy.deepcopy(board_matrix)
                                    move_check_matrix[index_y + y][index_x + x] = 1
                                    if pieceDetector(move_check_matrix)[0] == True:
                                        if pieceDetector(move_check_matrix)[1][0] == i:
                                            defended_matrices[i][index_y + y][index_x + x] = 1
                                        elif pieceDetector(move_check_matrix)[1][0] != i:
                                            possible_moves_matrix[index_y + y][index_x + x] = 1
                                        break
                                    elif pieceDetector(move_check_matrix)[0] == False:
                                        possible_moves_matrix[index_y + y][index_x + x] = 1
                                        index_x += x
                                        index_y += y
                    
                    elif j == 5:
                        for x in range(-1, 2, 2):
                            for y in range(-1, 2, 2):
                                if (index_x_piece + x) < 8 and (index_x_piece + x) > -1 and (index_y_piece + y) < 8 and (index_y_piece + y) > -1:
                                    move_check_matrix = copy.deepcopy(board_matrix)
                                    move_check_matrix[index_y_piece + y][index_x_piece + x] = 1
                                    if pieceDetector(move_check_matrix)[0] == True:
                                        if pieceDetector(move_check_matrix)[1][0] == i:
                                            defended_matrices[i][index_y_piece + y][index_x_piece + x] = 1
                                        elif pieceDetector(move_check_matrix)[1][0] != i:
                                            possible_moves_matrix[index_y_piece + y][index_x_piece + x] = 1
                                    elif pieceDetector(move_check_matrix)[0] == False:
                                        possible_moves_matrix[index_y_piece + y][index_x_piece + x] = 1
                                                
                        for repeat in range(2):
                            for coordinate in range(-1, 2, 2):
                                if repeat == 0: y = 0; x = coordinate
                                elif repeat == 1: x = 0; y = coordinate
                                if (index_x_piece + x) < 8 and (index_x_piece + x) > -1 and (index_y_piece + y) < 8 and (index_y_piece + y) > -1:
                                    move_check_matrix = copy.deepcopy(board_matrix)
                                    move_check_matrix[index_y_piece + y][index_x_piece + x] = 1
                                    if pieceDetector(move_check_matrix)[0] == True:
                                        if pieceDetector(move_check_matrix)[1][0] == i:
                                            defended_matrices[i][index_y_piece + y][index_x_piece + x] = 1
                                        elif pieceDetector(move_check_matrix)[1][0] != i:
                                            possible_moves_matrix[index_y_piece + y][index_x_piece + x] = 1
                                    elif pieceDetector(move_check_matrix)[0] == False:
                                        possible_moves_matrix[index_y_piece + y][index_x_piece + x] = 1
                        
                        if i == 0: row = 0
                        elif i == 1: row = 7
                        castling_check_matrix = copy.deepcopy(board_matrix)
                        castling_check_matrix[row][1] = 1
                        castling_check_matrix_2 = copy.deepcopy(board_matrix)
                        castling_check_matrix_2[row][2] = 1
                        
                        if pieces[i][5][0][4] == False and pieces[i][3][0][4] == False and not pieceDetector(castling_check_matrix)[0] and not pieceDetector(castling_check_matrix_2)[0]:
                            king_save_matrix = copy.deepcopy(pieces[i][5][0][1])
                            pieces[i][5][0][1] = copy.deepcopy(board_matrix)
                            pieces[i][5][0][1][row][1] = 1
                            if not checkDetector(i):
                                possible_moves_matrix[row][1] = 1
                            pieces[i][5][0][1] = copy.deepcopy(board_matrix)
                            pieces[i][5][0][1] = king_save_matrix
                                
                    pieces[i][j][k][2] = possible_moves_matrix
                
                elif pieces[i][j][k][3] == False:
                    pieces[i][j][k][2] = copy.deepcopy(board_matrix)
                    pieces[i][j][k][1] = copy.deepcopy(board_matrix)

    kingMovesCheckDetector()
    
                            
def redrawSelectedPiece():
    # Function to redraw a piece that has been deselected
    if pdi[1] == 0: draw.pawn(drawers[pdi[0]][pdi[1]][pdi[2]][0], corners[0][0] + wdw[1]*((i1+1)/9), corners[0][1] + (wdw[1]*((j1+1)/9)), team[pdi[0]]) 
    elif pdi[1] == 1: draw.knight(drawers[pdi[0]][pdi[1]][pdi[2]][0], corners[0][0] + wdw[1]*((i1+1)/9), corners[0][1] + (wdw[1]*((j1+1)/9)), team[pdi[0]])
    elif pdi[1] == 2: draw.bishop(drawers[pdi[0]][pdi[1]][pdi[2]][0], corners[0][0] + wdw[1]*((i1+1)/9), corners[0][1] + (wdw[1]*((j1+1)/9)), team[pdi[0]])
    elif pdi[1] == 3: draw.rook(drawers[pdi[0]][pdi[1]][pdi[2]][0], corners[0][0] + wdw[1]*((i1+1)/9), corners[0][1] + (wdw[1]*((j1+1)/9)), team[pdi[0]])
    elif pdi[1] == 4: draw.queen(drawers[pdi[0]][pdi[1]][pdi[2]][0], corners[0][0] + wdw[1]*((i1+1)/9), corners[0][1] + (wdw[1]*((j1+1)/9)), team[pdi[0]])
    elif pdi[1] == 5: draw.king(drawers[pdi[0]][pdi[1]][pdi[2]][0], corners[0][0] + wdw[1]*((i1+1)/9), corners[0][1] + (wdw[1]*((j1+1)/9)), team[pdi[0]])


def selectedPieceSquareDraw(i, j):
    # Function to draw the selected square shade
    sel_sqr_drw[0][0].goto((corners[0][0] + wdw[1]*(i/9) - wdw[1]*(1/18)), (corners[0][1] + wdw[1]*(j/9) - wdw[1]*(1/18)))  # Go to position to add the shade of the selected piece square
    if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1): draw.bsqr(themes[theme][1][1], sel_sqr_drw[0][0])  # Draw dark square with selected square shade
    elif (i % 2 == 1 and j % 2 == 0) or (i % 2 == 0 and j % 2 == 1): draw.bsqr(themes[theme][1][0], sel_sqr_drw[0][0])  # Draw light square with selected square shade


def checkedKingSquareDraw(i, j):
    # Function to draw the check square shade
    check_sqr_drw.goto((corners[0][0] + wdw[1]*(i/9) - wdw[1]*(1/18)), (corners[0][1] + wdw[1]*(j/9) - wdw[1]*(1/18)))  # Go to position to add the shade of the checked king square
    if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1): draw.bsqr(themes[theme][2][1], check_sqr_drw)  # Draw dark square with selected square shade
    elif (i % 2 == 1 and j % 2 == 0) or (i % 2 == 0 and j % 2 == 1): draw.bsqr(themes[theme][2][0], check_sqr_drw)  # Draw light square with selected square shade
                
board_matrix =   [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]]

first_click_matrix = copy.deepcopy(board_matrix)
second_click_matrix = copy.deepcopy(board_matrix)
defended_matrices = [copy.deepcopy(board_matrix), copy.deepcopy(board_matrix)]

wdw = (500, 500)  # Window size for future input or custom size settings
# This tuple is very important for everything visual. Each distance is a fraction of the window's height.
# This means that you can change the resolution of the window and the chess will be drawn depending on its height.

# Coordinates of the 4 corners of the window.
corners = [(-1*wdw[0]/2, -1*wdw[1]/2), (-1*wdw[0]/2, wdw[1]/2), (wdw[0]/2, wdw[1]/2), (wdw[0]/2, -1*wdw[1]/2)]
          #      Bottom left [0]             Top left [1]           Top right [2]         Bottom right [3]       

t.setup(wdw[0], wdw[1])
t.title("Welcome to Chess by Pez")  # Title of the window
# Color themes for the chess board. Classic ([0]) or custom ([1]) color shadings.

clicks_done = 0
# Record number of clicks in the board.

pdi = ()
# Piece detected indices:
    # [0] = What team? (0 = white, 1 = black)
    # [1] = What type of piece? (0 = pawn, 1 = knight, etc.)
    # [2] = What individual piece? (0 = 1st pawn, 1 = 2nd pawn, etc.)

i1 = 0
# The row index location of the selected piece to move in the board matrix

j1 = 0
# The column index location of the selected piece to move in the board matrix

moving_team = 0
# The team of the selected piece to move

opponent_team = 0
# The team opposite of the selected piece

steps = 12
# Number of edges of the circles of the pieces. Lower = faster graphics, low quality. Higher = slower graphics, higher quality.

themes = {  # Color themes for the board drawings 
    "classic":
       #   Light      Dark       Edge
        [["#f1d9b5","#b58863", "#5b4432"],  # Normal square color
         ["#cdd277", "#aaa245", "#666129"],  # Selected square color
         ["#f9a89a", "#e08676", "#7f3123"]],  # Checked square color  
    "custom":
        [(0,0,0),(0,0,0),(0,0,0)]}

team = [  # Dictionary with color palette of the pieces of each team
    {"light": "#ffffff", "dark": "#cccccc"},  # Dark = shadows of the piece
    {"light": "#808080", "dark": "#4d4d4d"}]  # Light = original color of the piece


drawers = [  #All
    [  # White
        [  # Pawns
            [1, 1],  # Pawn 1 drawer, Starting x square 1
            [2, 2],
            [3, 3],
            [4, 4],
            [5, 5],
            [6, 6],
            [7, 7],
            [8, 8]],  
        [  # Knights
            [1, 2],  # Knight 1 drawer, Starting at x square 2
            [2, 7]],
        [  # Bishops
            [1, 3],  # Bishop 1 drawer, Starting at x square 3
            [2, 6]],  # Bishops
        [  # Rooks
            [1, 1],  # Rook 1 drawer, Starting at x square 1
            [2, 8]],
        [  # Queen
            [1, 5]],  # Drawer, Starting at x square 4
        [  # King
            [1, 4]]  # Drawer, Starting at x square 5
    ],
    [  # Black
        [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],  # Pawns
        [[1, 2], [2, 7]],  # Knights
        [[1, 3], [2, 6]],  # Bishops
        [[1, 1], [2, 8]],  # Rooks
        [[1, 5]],  # Queen
        [[1, 4]]  # King
    ]
]


pieces = [  # All
    [  # Team [white, black]
        [  # Piece type [pawns, knights, bishops, rooks, queen, king]
            [  # Individual piece [pawn 1, pawn 2, pawn 3, ...]
                1,  # Properties [number of piece, piece location matrix, piece moves matrix, piece alive status, piece defended status]
                [],
                [],
                bool(),
                False],  
            [2,[],[],bool(),False],
            [3,[],[],bool(),False],
            [4,[],[],bool(),False],
            [5,[],[],bool(),False],
            [6,[],[],bool(),False],
            [7,[],[],bool(),False],
            [8,[],[],bool(),False]],  
        [  # Knights
            [1,[],[],bool(),bool()],  # Knight 1 drawer, Starting at x square 2
            [2,[],[],bool(),bool()]],
        [  # Bishops
            [1,[],[],bool(),bool()],  # Bishop 1 drawer, Starting at x square 3
            [2,[],[],bool(),bool()]],  # Bishops
        [  # Rooks
            [1,[],[],bool(),False],  # Rook 1 drawer, Starting at x square 1.
            [2,[],[],bool(),False]],
        [  # Queen
            [1,[],[],bool(),bool()]],  # Drawer, Starting at x square 4
        [  # King
            [1,[],[],bool(),False]]  # Drawer, Starting at x square 5
    ],
    [  # Black
        [[1,[],[],bool(),False], [2,[],[],bool(),False], [3,[],[],bool(),False], [4,[],[],bool(),False], [5,[],[],bool(),False], [6,[],[],bool(),False], [7,[],[],bool(),False], [8,[],[],bool(),False]],  # Pawns
        [[1,[],[],bool(),bool()], [2,[],[],bool(),bool()]],  # Knights
        [[1,[],[],bool(),bool()], [2,[],[],bool(),bool()]],  # Bishops
        [[1,[],[],bool(),False], [2,[],[],bool(),False]],  # Rooks
        [[1,[],[],bool(),bool()]],  # Queen
        [[1,[],[],bool(),False]]  # King
    ]
]

theme = "classic"

t.tracer(0, 0)  # (no screen updates, no delay for screen updates) = Instantaneous drawing when t.update()
bdrw = t.Turtle()  # Board drawer turtle. b = board, drw = drawer.
bdrw.ht()  # Hides the bdrw (board drawer) instance turtle
bdrw.speed(-1)  # Instantaneous drawing

check_sqr_drw = t.Turtle()
# Turtle to draw the checked square shade
check_sqr_drw.ht()
check_sqr_drw.speed(-1)
check_sqr_drw.pu()

possible_moves_drw = t.Turtle()
# Turtle to draw the possible moves dots
possible_moves_drw.ht()
possible_moves_drw.speed(-1)
possible_moves_drw.pen(pendown=False, pensize=2.25*wdw[1]/720)

sel_sqr_drw = [[0, 1],[0, 1]]
# We were originally planning to have different colors for each team's selected square shades + have different colors for origin square and destination square.

for i in range(len(sel_sqr_drw)):
    for j in range(len(sel_sqr_drw[i])):
        sel_sqr_drw[i][j] = t.Turtle()
        # 4 turtles: origin and destination shades for white, origin and destination shades for black
        sel_sqr_drw[i][j].pu()
        sel_sqr_drw[i][j].ht()
        sel_sqr_drw[i][j].speed(-1)

initialize()
# Call the starting status of the game

t.onscreenclick(clickDetection)
# Start detectin clicks
t.done()
# Avoid window crash errors























