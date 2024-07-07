import pygame
import pygame.display
import pygame.draw
import pygame.rect

def main():
    Active = True

    while Active == True:
        pygame.init()
        mainWindow = pygame.display.set_mode((900,900))
        pygame.display.set_caption("Chess Game")
        BGColour = (128, 128, 128)
        mainWindow.fill(BGColour)

        displayWindow(mainWindow)

        pygame.display.flip()
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                Active = False
        
def displayWindow(mainWindow):
    displayArray = [(30, 30, 100, 100), (130, 30, 100, 100),(230, 30, 100, 100),(330, 30, 100, 100), (430, 30, 100, 100), (530, 30, 100, 100), (630, 30, 100, 100), (730, 30, 100, 100), (30, 130, 100, 100), (130, 130, 100, 100),(230, 130, 100, 100),(330, 130, 100, 100), (430, 130, 100, 100), (530, 130, 100, 100), (630, 130, 100, 100), (730, 130, 100, 100), (30, 230, 100, 100), (130, 230, 100, 100),(230, 230, 100, 100),(330, 230, 100, 100), (430, 230, 100, 100), (530, 230, 100, 100), (630, 230, 100, 100), (730, 230, 100, 100)]

    for i in range(len(displayArray)):
        if i % 2 == 0:
            pygame.draw.rect(mainWindow, "white", displayArray[i])
        else:
            pygame.draw.rect(mainWindow, "black", displayArray[i])      

main()


