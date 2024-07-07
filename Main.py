import pygame
import pygame.display
import pygame.draw
import pygame.rect

def main():
    Active = True

    while Active == True:
        pygame.init()



        mainWindow = displayMainWindow()
        displayBoard(mainWindow)

        pygame.display.flip()
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                Active = False

def displayMainWindow():
        mainWindow = pygame.display.set_mode((900,900))
        pygame.display.set_caption("Chess Game")
        BGColour = (128, 128, 128)
        mainWindow.fill(BGColour) 

        return mainWindow  

def displayMenuWindow():
    

def displayBoard(mainWindow):
    displayArray = [(30, 30, 100, 100), (130, 30, 100, 100),(230, 30, 100, 100),(330, 30, 100, 100), (430, 30, 100, 100), (530, 30, 100, 100), (630, 30, 100, 100), (730, 30, 100, 100), (30, 130, 100, 100), (130, 130, 100, 100),(230, 130, 100, 100),(330, 130, 100, 100), (430, 130, 100, 100), (530, 130, 100, 100), (630, 130, 100, 100), (730, 130, 100, 100), (30, 230, 100, 100), (130, 230, 100, 100),(230, 230, 100, 100),(330, 230, 100, 100), (430, 230, 100, 100), (530, 230, 100, 100), (630, 230, 100, 100), (730, 230, 100, 100), (30, 330, 100, 100), (130, 330, 100, 100),(230, 330, 100, 100),(330, 330, 100, 100), (430, 330, 100, 100), (530, 330, 100, 100), (630, 330, 100, 100), (730, 330, 100, 100), (30, 430, 100, 100), (130, 430, 100, 100),(230, 430, 100, 100),(330, 430, 100, 100), (430, 430, 100, 100), (530, 430, 100, 100), (630, 430, 100, 100), (730, 430, 100, 100), (30, 530, 100, 100), (130, 530, 100, 100),(230, 530, 100, 100),(330, 530, 100, 100), (430, 530, 100, 100), (530, 530, 100, 100), (630, 530, 100, 100), (730, 530, 100, 100), (30, 630, 100, 100), (130, 630, 100, 100),(230, 630, 100, 100),(330, 630, 100, 100), (430, 630, 100, 100), (530, 630, 100, 100), (630, 630, 100, 100), (730, 630, 100, 100), (30, 730, 100, 100), (130, 730, 100, 100),(230, 730, 100, 100),(330, 730, 100, 100), (430, 730, 100, 100), (530, 730, 100, 100), (630, 730, 100, 100), (730, 730, 100, 100)]
    colourArray = ["white", "black", "white", "black", "white", "black", "white", "black", "black", "white", "black", "white", "black", "white", "black", "white", "white", "black", "white", "black", "white", "black", "white", "black", "black", "white", "black", "white", "black", "white", "black", "white", "white", "black","white", "black","white", "black","white", "black","black","white","black","white","black","white","black","white","white","black","white","black","white","black","white","black","black","white","black","white","black","white","black","white"]

    for i in range(len(displayArray)):
        if i % 2 == 0:
            pygame.draw.rect(mainWindow, colourArray[i], displayArray[i])
        else:
            pygame.draw.rect(mainWindow, colourArray[i], displayArray[i])

def selectColour(mainWindow):
    pass


main()


