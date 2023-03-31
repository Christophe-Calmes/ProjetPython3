import pygame

# Initialisation de Pygame
pygame.init()

# Création d'une fenêtre de 600 x 600 pixels
fenetre = pygame.display.set_mode((600, 600))

# Boucle principale
while True:
    # Traitement des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Fermeture de la fenêtre
            pygame.quit()
            exit()
