# il faut installer pygame avec terminal
import math
import pygame
from game import Game
from projectile import Projectile
from monstre import Monstre

pygame.init()
# la fenetre de jeu
# le titre
pygame.display.set_caption("Comet fall game")

# la dimension
surface =pygame.display.set_mode((1240,720))

# importer l'arriere plan de notre jeu
bg=pygame.image.load("PygameAssets-main/vvv.jpg")
# importer notre banniere
banner=pygame.image.load("PygameAssets-main/banner.png")
# importer le button
button=pygame.image.load("PygameAssets-main/button.png")
# redémensionner l'image
banner=pygame.transform.scale(banner,(500,500))
button=pygame.transform.scale(button,(400,150))
play_button_rectangle=button.get_rect() # le rectangle du bouton
play_button_rectangle.x=math.ceil(surface.get_width()/3.1)
play_button_rectangle.y=math.ceil(surface.get_height()/1.34)

# charger notre jeu
game1=Game()
running=True
while running==True:

     # je vais dessiner sur la surface l'arrière plan
   surface.blit(bg,(0,0))
     # vérifier si le jeu à été bien commencé
   if game1.is_playing:
        game1.update(surface)

   else:
       #ajouter l'ecran bienvenue
     surface.blit(banner,(surface.get_width()/4+30,surface.get_height()/6))
       #ajouter le button
     surface.blit(button,play_button_rectangle)


   #mettre à jour l'écran
   pygame.display.flip()

    #si le joueur fait des évenements sur cette fenetre
   for event in pygame.event.get():

    # si l'évenement est la fermeture
     if event.type==pygame.QUIT:
        running==False
        pygame.quit()
     #si un joueur lache une au clavier (elif : seconde condition)
     elif event.type==pygame.KEYDOWN:

         game1.pressed[event.key] = True  # enregistrer la touche
     elif event.type == pygame.K_SPACE:
         game1.pressed[event.key] = True

     elif event.type==pygame.KEYUP:
         game1.pressed[event.key]=False

     elif event.type == pygame.MOUSEBUTTONDOWN:
         #verification si la souris est en collision avec le bouton jouer il faudra
         #récuperer le rectangle du bouton
        if play_button_rectangle.collidepoint(event.pos):# si la personne clique sur une parite du btn
           game1.start()






