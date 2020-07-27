import pygame  #import the package
import random
pygame.init()  #intialize the package

#varaiable frame is created
#pygame.time.Clock() allow us to change the frame/second
frame=pygame.time.Clock()

#the following code is to mix the color.
white= (255,255,255)  #color (red, green, blue)
black= (0,0,0)
red = (255, 0,0)
green= (0,155,0)
blue=()
purple=(155,0,155)


#new variable for the width and height
display_width=800
display_height=600
fps=10

#call the font, not a specific font, 25 size
font=pygame.font.SysFont(None,20)


def text_objects(text,color):
    textSurface = font.render(text,True,color)
    return textSurface, textSurface.get_rect()
#define a function that has the parameter msg and color
#display it on the screen
def message_to_screen(msg,color):
    textSurf, textRect = text_objects(msg,color)
    textRect.center = (display_width / 2), (display_height / 2)
    gamedisplay.blit(textSurf,textRect)
    #text=font.render (msg, True, color)
    #gamedisplay.blit(text, [display_width/2,display_height/2])



gamedisplay=pygame.display.set_mode((display_width,display_height))  #set the frame of the game (the size of it in pixel)

pygame.display.update()  #update the information now

#all the codes are under the update
pygame.display.set_caption("Slither")  #game title

block_size=10

#call the sname function in order to let the length of the snake grow)
def snake(block_size, snakeList):
    #loop to add the length of the snake
    for XnY in snakeList:

    #pygame.draw.rect draws a rectangle inside the () it has (where we want to draw it, what color, and a list [x,y,width of rect, length of rect]
            pygame.draw.rect(gamedisplay,purple,[XnY[0],XnY[1],block_size,block_size])  #draws the snake


#define the function. the whole game loop is the function
def gameLoop():

    gameExit = False
    # gameExit is quitting the game
    gameAgain= False
    #gameAgain is for the game to play again
    # create a block for the "snake game"
    # The size of the block, the starting point for the game!!! in the middle!!!
    x_block = display_width / 2
    y_block = display_height / 2
    x_block_change = 0
    y_block_change = 0


    #a list for the let the snake grow longer
    snakeList = []

    #let the snake lengthbe 1
    snakeLength=1

    #used import random to random the position of the apple on x and y direction
    randAppleX=round((random.randrange(0,display_width-block_size))/10)*10
    randAppleY=round((random.randrange(0,display_height-block_size))/10)*10

    while not gameExit:  #the while loop for this code (the game loop)

        #create the new game loop for playing the game again
        while gameAgain == True: #while I can gamePlay loop is true
            gamedisplay.fill(white)
            message_to_screen("Game over. Press Q to quit the game, press A to play again!!!", red)
            pygame.display.update()
            #add the pygame event module
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    #if they press q, game exit play again is false
                    if event.key==pygame.K_q:
                        gameExit=True
                        gameAgain=False
                    if event.key==pygame.K_a:
                        #if they press g, run the game loop again
                        gameLoop()



        for event in pygame.event.get(): ##add the pygame.event module
            #This creates a path to close the game using the close button for the game
            if event.type==pygame.QUIT:
                gameExit=True

            #keydown and K_(direction) can use the arrow to move around
            #The reason to have x and y frame is because it will go dianolly.
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_block_change=-block_size
                    y_block_change=0

                elif event.key==pygame.K_RIGHT:
                    x_block_change=block_size
                    y_block_change=0

                elif event.key==pygame.K_UP:
                    y_block_change=-block_size
                    x_block_change=0

                elif event.key==pygame.K_DOWN:
                    y_block_change=block_size
                    x_block_change=0


        if x_block >= display_width-block_size or x_block < 0-15 or y_block >= display_height-block_size  or y_block < 0-15:
            gameAgain = True

        x_block+=x_block_change
        y_block+=y_block_change


        #gamedisplay is where we set the backgroud for the game. It sets for the size of the window.
        #use .fill can change the background color. However, it needs to update once it change.
        gamedisplay.fill(white)

        # pygame.draw.rect draws a rectangle inside the () it has (where we want to draw it, what color, and a list [x,y,width of rect, length of rect]
        pygame.draw.rect(gamedisplay,red,[randAppleX,randAppleY,block_size,block_size])  #draws the apple


        #create a snakeHead list to store value every time it eats
        #add x and y. and add snakeHead to snakeList
        snakeHead=[]
        snakeHead.append(x_block)
        snakeHead.append(y_block)
        snakeList.append(snakeHead)


        #keep the snake length the same while moving
        if len(snakeList)> snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if snakeHead==eachSegment:
                gameAgain=True
        snake(block_size,snakeList)
        pygame.display.update()


        #the name "frame" . tick can change the frame of the game
        frame.tick(fps)
        pygame.display.update()

        #round the apple to another location and add the length of the snake
        if x_block==randAppleX and y_block==randAppleY:
            randAppleX = round((random.randrange(0, display_width - block_size)) / 10) * 10
            randAppleY = round((random.randrange(0, display_height - block_size)) / 10) * 10
            #if snake head meets with the apple, add one length of snake
            snakeLength+=1

        pygame.display.update()

    pygame.quit()  #quit the game
    quit()  #
gameLoop()
